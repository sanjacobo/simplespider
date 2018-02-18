import scrapy
import datetime
from spider_test.items import SpiderTestItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    ITEM_PIPELINES = {
        'spider_test.pipelines.SpiderTestPipeline': 300,
    }

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        url = response.url
        status = response.status
        robot = response.css('meta[name=robots]').xpath('@content').extract()

        item = SpiderTestItem()

        item['url'] = url
        item['status'] = status
        item['robot'] = robot[0] if robot else robot

        yield item
