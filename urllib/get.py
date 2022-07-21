import urllib.request

url = 'http://www.baidu.com'
headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# urlopen 方法不能存字典，所以headers不能传递进去
# 请求对象定制
# 参数顺序，不能直传参数

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)
