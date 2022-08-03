import time

import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/diandongche/brand-75-146.html']
    start_urls = ['https://car.autohome.com.cn/diandongche/brand-75-146.html']

    def parse(self, response):
        car_list = response.xpath('//div[@class="tab-content fn-visible"]//a[@class="font-bold"]/text()')
        price_list = response.xpath('//div[@class="tab-content fn-visible"]//span[@class="font-arial"]/text()')

        for i in range(len(car_list)):
            print("car: "+car_list[i].extract()+"   price:"+price_list[i].extract())
        print("=====================================")
        # with open('./html/car_'+str(time.localtime()),'w',encoding='utf-8') as fp:
        #     fp.write(car_list)