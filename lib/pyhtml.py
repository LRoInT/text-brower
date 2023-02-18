import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
def rqurl(url,user):
    #获取网页
    if url[0:7]!="http://" or url[0:8]!="https://": #自动添加 https:// 防止报错
        url="https://"+url
    url=requests.get(url,headers=user[0]) #get访问
    page=url.text
    #解析html(ChatGPT写的代码还不错)
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.title.string)
    print(soup.get_text())
    link=[]
    img=[]
    date=[link,img]
    for lk in soup.find_all('a'):
        link.append(lk.get('href'))
    for ig in soup.find_all('img'):
        img.append(ig.get('src'))
    return date