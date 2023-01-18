from requests  import *
import sys
from html.parser import HTMLParser
class readhtml(self):
    def handle_starttag(self, tag, attrs):
        print("起始标签:", tag)

    def handle_endtag(self, tag):
        print("结束标签 :", tag)

    def handle_data(self, data):
        print("数据:", data)

def web(resp,user):
    #获取网页
    if url[0:7]!="http://" or url[0:8]!="https://": #自动添加 https:// 防止报错
        url="https://"+resp
    websize=get(url,headers=user[1],cookies=user[2]) #get访问
    return websize
 
def main():
    url=sys.argv[1]                #获取访问网址
    about_user=sys.argv[2]         #获取用户信息
    #字符串(命令行参数)转列表
    about_user=about_user.replace("[","")
    about_user=about_user.replace("]","")
    about_user=about_user.replace("'","")
    about_user=about_user.replace('"',"")
    about_user=about_user.split(", ")
    resp=web(url,about_user)
    html=resp.text
    page=readhtml(html)
    return {}
    