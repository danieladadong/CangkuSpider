import json
from CangKuSpider.items import CangkucontentItem
import scrapy
import pandas as pd
df = pd.read_csv('cangku.csv',encoding='utf-8 sig')
urls = list(df['contexturl'])
class ContentSpider(scrapy.Spider):
    name = 'content'
    def start_requests(self):
        start_url = ['https://cangku.io/api/v1/post/info?id={}&include=user,tags,categories,favorited,upvoted'.format(str(i)) for i in urls]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
        }
        cookies = {
            'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': '你的token',
            'XSRF-TOKEN': '你的XSRF-TOKEN',
            'cangku_laravel_session': '你的SESSION'}
        for url in start_url:
            yield scrapy.Request(url=url, cookies=cookies, headers=headers, callback=self.parse)
    def parse(self, response, **kwargs):
        rs = json.loads(response.text)
        if rs.get('message') == 'success':
            data = rs.get('data')
            item = CangkucontentItem()
            item['contentid'] = data['id']
            item['title'] = data['title'][6::]
            item['content'] = data['content']
            item['uploadtime'] = data['created_at']
            yield item
