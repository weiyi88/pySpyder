import scrapy
from dangdang.items import DangdangItem

class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['book.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%BF%C6%BB%C3&act=input']
    # http: // search.dangdang.com /?key = % BF % C6 % BB % C3 & act = input & page_index = 3
    base_url = 'http://search.dangdang.com/?key=%BF%C6%BB%C3&act=input'
    page = 1
    def parse(self, response):
        # pipline 下载数据
        # item    数据结构

        data_list = response.xpath('//div[@id="search_nature_rg"]/ul/li')

        for data in data_list:
            src = data.xpath('./a/img/@data-original').extract_first()
            # 第一张图片 和其他图片是不一样，第一张直接获取，其他图片懒加载
            if src:
                src = src
            else:
                src = data.xpath('./a/img/@src').extract_first()
            title = data.xpath('./a/@title').extract_first()
            price = data.xpath('.//span[@class="search_now_price"]/text()').extract_first()
            book = DangdangItem(src=src,title=title,price=price)
            # yield 相当于异步中断，return 一个返回值
            # 获取一个book 就交给 piplines
            yield book

            # 每页爬取，规格一致，多页爬取
            if self.page < 100:
                self.page = self.page+1
                url = self.base_url +"&page_index="+str(self.page)
                print("+======================"+url)
                # 调用 parse方法，
                # scrapy.Request() 就是scrapy都get请求
                yield scrapy.Request(url=url,callback=self.parse)

