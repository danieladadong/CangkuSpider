# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CangkuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    classify = scrapy.Field()
    title = scrapy.Field()
    imageurl = scrapy.Field()
    author = scrapy.Field()
    uploadtime = scrapy.Field()
    contexturl = scrapy.Field()
    pass


class CangkuImageItem(scrapy.Item):
    pass
class CangkucontentItem(scrapy.Item):
    contentid = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    uploadtime = scrapy.Field()
