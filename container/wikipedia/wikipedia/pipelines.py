# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WikipediaPipeline(object):
    def process_item(self, item, spider):
        if item['R']:
            text = item['R'].strip()
            text = text.replace('"', '')
            text = text.upper()
            item['R'] = text
        if item['R']:
            return item
        
class SaveDataPipeline(object):
    def open_spider(self, spider):
        self.dataFile = open("data.txt", "x")
    def process_item(self, item, spider):
        self.dataFile.write(item['R'] + '\n')
        return item
    def close_spider(self, spider):
        self.dataFile.close()
