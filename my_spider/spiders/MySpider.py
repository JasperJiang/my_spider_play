# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.loader import ItemLoader
from my_spider.items import AppItem


class MyspiderSpider(scrapy.Spider):
    name = 'MySpider'
    allowed_domains = ['xclient.info']
    start_urls = ['http://xclient.info/s/?_=c2335e20cbef5f6d203d582cac8eff50']

    def parse(self, response):

        for div in response.xpath('//li/div[@class="main"]'):
            appItem = AppItem()
            appItem['url'] = div.xpath('a/img/@src').extract()
            appItem['name'] = div.xpath('a/@title').extract()
            yield appItem

