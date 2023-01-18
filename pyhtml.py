from requests  import *
import sys
from html.parser import HTMLParser
class readhtml(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("起始标签:", tag)

    def handle_endtag(self, tag):
        print("结束标签 :", tag)

    def handle_data(self, data):
        print("数据:", data)

def web(resp,user):
    #获取网页
    if resp[0:7]!="http://" or resp[0:8]!="https://": #自动添加 https:// 防止报错
        resp="https://"+resp
    websize=get(resp,headers=user[1],cookies=user[2]) #get访问
    return websize
 
def main():
    url=sys.argv[1]                #获取访问网址
    ua=sys.argv[2]                 #获取用户信息
    cookies=sys.argv[3]
    about_user=[ua,cookies]
    resp=web(url,about_user)
    html=resp.text
    page=readhtml(html)
    page.feed(html)

main()
    