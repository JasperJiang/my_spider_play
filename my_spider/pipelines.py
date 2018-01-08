# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MySpiderPipeline(object):
    def __init__(self):
        self.fs = open('out/items.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fs.write(str(dict(item)) + "\n")
        return item

    def close_spider(self, spider):
        self.fs.close()
