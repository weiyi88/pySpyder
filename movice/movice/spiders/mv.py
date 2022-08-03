import scrapy


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['m.dytt8.net']
    start_urls = ['http://m.dytt8.net/']

    def parse(self, response):

        a_list = response.xpath('//div[@class="co_content8"]//table//tr/td[1]/a[2]')

        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href  = a.xpath('./@href').extract_first()

            # https://m.dytt8.net/html/gndy/dyzz/20220801/62849.html
            # /html/gndy/dyzz/20220801/62849.html
            url = "https://m.dytt8.net"+href

            # 对第二页对链接发起访问
            yield scrapy.Request(url=url,callback=self.parse_img)
        print("===================================")
        pass

    def parse_img(self,response):
        img_url = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        print(img_url)