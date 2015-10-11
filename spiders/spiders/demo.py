# -*- coding: utf-8 -*-
import scrapy

#print(dir(scrapy))
class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        'http://www.zhihu.com/',
    )

    def parse(self, response):
        print("\n---------------ok-------------\n")
        pass
