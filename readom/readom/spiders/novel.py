import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NovelSpider(CrawlSpider):
    name = 'novel'
    allowed_domains = ['allworldbeauty.com']
    start_urls = ['http://allworldbeauty.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        yield
