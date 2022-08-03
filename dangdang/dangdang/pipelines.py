# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DangdangPipeline:

    def open_spider(self,spider):
        self.fp = open('book.json','a',encoding='utf-8')

    # item 就是 yield 后面的book 对象
    def process_item(self, item, spider):
        # 下载数据
        # write() 必须是一个字符串，不能是对象
        # w 模式会每次都打开一次文件，覆盖前面数据
        # 每传来一个对象就操作一次文件，不推荐
        # with open('book.json','a',encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item


    def close_spider(self,spider):
        self.fp.close()

import urllib.request

# 多条管道同时开启 ， 下载图片
# 1，定义管道类
# 2，setting中开启管道
# 'dangdang.pipelines.DangPicturePipline': 301,
class DangPicturePipline:
    def process_item(self,item,spider):
        url = "http:"+item.get('src')
        filename = "./books/"+item.get('title')+'.jpg'
        urllib.request.urlretrieve(url=url,filename=filename)
        return item