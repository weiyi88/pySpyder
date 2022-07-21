from lxml import etree

# xpath 解析
# 1，本地文件      etree.parse
# 2，服务器响应数据   etree.HTML

tree = etree.parse("test.html")

# // 不管前面有多少级，直接找对应的标签， /找子节点
# li_tree = tree.xpath('//ul/li')

# 找所有id属性的标签
# li_tree = tree.xpath('//ul/li[@id]')

# text() 获取标签内容     id = 11 的 注意引号问题
li_tree = tree.xpath('//ul/li[@id="11"]/text()')
print(li_tree)