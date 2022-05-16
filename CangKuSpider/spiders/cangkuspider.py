import csv
import json

import scrapy
from scrapy import Request
from CangKuSpider.items import CangkuspiderItem
import pandas as pd



class CangkuSpider(scrapy.Spider):
    name = 'cangku'

    def start_requests(self):
        start_urls = ['https://cangku.io/api/v1/post/list?page={}&per_page=18&with[]=user&with[]=categories&include=user,categories:simple&simple=1'.format(str(i)) for i in range(1, 2045,1)]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
        }
        cookies = {
            'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': '你的token',
            'XSRF-TOKEN': '你的XSRF-TOKEN',
            'cangku_laravel_session': '你的SESSION'}
        for url in start_urls:
            yield scrapy.Request(url=url, cookies=cookies, headers=headers, callback=self.parse)


    def parse(self, response, **kwargs):
        rs = json.loads(response.text)
        if rs.get('message') == 'success':
            data = rs.get('data')
            for data_detail in data:
                item = CangkuspiderItem()
                item['classify'] = data_detail.get('title')[0:5:]
                item['title'] = data_detail.get('title')[6::]
                item['imageurl'] = data_detail.get('thumb')
                item['author'] = data_detail.get('user').get('nickname')
                item['uploadtime'] = data_detail.get('created_at')
                item['contexturl'] = str(data_detail.get('id'))
                yield item

