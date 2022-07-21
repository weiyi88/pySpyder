import requests
from lxml import etree
import urllib.request

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

response  = requests.get(url = url,headers = headers)
content = response.text

tree = etree.HTML(content)
viewstate = tree.xpath('//input[@id="__VIEWSTATE"]/@value')
viewstategenerator = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')

# 验证码
imgCodeSrc = tree.xpath('//img[@id="imgCode"]/@src')
imgCodeUrl = 'https://so.gushiwen.cn'+imgCodeSrc[0]


# 获取验证码图片 有坑，和本次请求的链接不是同一个
# urllib.request.urlretrieve(url=imgCodeUrl,filename='./code.jpg')


session = requests.session()
response_code = session.get(imgCodeUrl)
# 此时要使用二进制数据，因为要使用图片的下载
content_code = response_code.content
# wb 模式就是将二进制数据写入文件
with open('./code1.jpg','wb') as fp:
    fp.write(content_code)

# 模拟输入验证码
code_name = input("请输入你的验证码：")


# 点击登陆
url_post ='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

data_post ={
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': 'tantubuping@163.com',
    'pwd': 'gushiwenwang',
    'code': code_name,
    'denglu': '登录'
}

login_request = requests.post(url=url,headers=headers,data=data_post)
content_post = login_request.text

with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(content_post)