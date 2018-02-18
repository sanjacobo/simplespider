import scrapy
import csv
import datetime
from spider_test.items import SpiderTestItem


class RobotSpider(scrapy.Spider):
    name = "robot"

    custom_settings = {
        'ITEM_PIPELINES': {
            'spider_test.pipelines.SpiderTestPipeline': 300,
        }
    }

    def start_requests(self):
        urls = [
            'https://www.orbitz.com/Caribbean.d6022969.Destination-Travel-Guides',
            'https://www.orbitz.com/Destinations-In-Caribbean.d6022969.Flight-Destinations',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.url
        status = response.status
        robot = response.css('meta[name=robots]').xpath('@content').extract()

        item = SpiderTestItem()

        item['url'] = url
        item['status'] = status
        item['robot'] = robot[0] if robot else robot

        yield item
