
import  requests

url  = 'http://www.baidu.com'

reponse = requests.get(url=url)


a:int = 123
b:str = 'string'

def add(val:int ,val1:int)->int:
    return val+val1