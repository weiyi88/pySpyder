import urllib.request
import urllib.parse

def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&'
    data = {
        'start':(page-1)*20,
        'limit':20
    }

    data = urllib.parse.urlencode(data)
    url = base_url+data
    print(url)
    return url

def make_request(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    return content

def make_file(content,page):
    with open('douban/film_'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page,end_page):

        make_file(make_request(create_request(page)),page)