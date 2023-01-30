import requests
import sys
from html.parser import HTMLParser as htmlreader
 
def rqurl(url,user):
    #获取网页
    if url[0:7]!="http://" or url[0:8]!="https://": #自动添加 https:// 防止报错
        url="https://"+url
    url=requests.get(url,headers=user[0]) #get访问
    html=url.text
    page=htmlreader()
    page.feed(html)
    