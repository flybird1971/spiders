# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class BsbdjItem(Item):
    name = Field()
    url = Field()

class SpidersItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CSDNItem(Item):
    name = Field()
    url = Field()

class DemoItem(Item):
    title = Field()
    href = Field()
    desc = Field()
    pass


class StackOverflowItem(Item):
    title = Field()
    tags = Field()
    body = Field()
    href = Field()
    pass
