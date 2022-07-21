import scrapy


class Tc58Spider(scrapy.Spider):
    name = 'tc58'
    allowed_domains = ['https://gz.58.com/job/?key=%E5%90%8E%E7%AB%AF&classpolicy=strategy,job_B,uuid_d50ae09b7ae144bd815e75e0f6ccaa77,displocalid_3,from_9224,to_jump,tradeline_job,classify_C&final=1']
    start_urls = ['https://gz.58.com/job/?key=%E5%90%8E%E7%AB%AF&classpolicy=strategy,job_B,uuid_d50ae09b7ae144bd815e75e0f6ccaa77,displocalid_3,from_9224,to_jump,tradeline_job,classify_C&final=1']

    def parse(self, response):
        print('爬了58')
        pass
