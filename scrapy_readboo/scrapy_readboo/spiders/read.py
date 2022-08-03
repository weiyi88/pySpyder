import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['http://www.dushu.com/']

    # rules = (
    #     Rule(LinkExtractor(
    #         allow=r'/book/1188_\d+\.html'),
    #         callback='parse_item',
    #         follow=False),
    # )

    def parse_item(self, response):
        item = {}
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
