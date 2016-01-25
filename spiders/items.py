# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DemoItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    desc = scrapy.Field()
    pass


class StackOverflowItem(scrapy.Item):
    title = scrapy.Field()
    tags = scrapy.Field()
    body = scrapy.Field()
    href = scrapy.Field()
    pass
