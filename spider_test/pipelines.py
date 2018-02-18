# -*- coding: utf-8 -*-
import csv
from spider_test.items import SpiderTestItem
import datetime


class SpiderTestPipeline(object):

    def __init__(self, date):
        self.date = datetime.datetime.now()
        self.item_data = []

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(date=crawler.spider.date)

    def process_item(self, item, spider):
        self.item_data.append(item)

        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        file_name = '{}-{}.csv'.format(spider.name, self.date)
        with open(file_name, 'wb') as f:
            fieldnames = SpiderTestItem.fields.keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for item in self.item_data:
                writer.writerow(item._values)
