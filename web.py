from requests  import *
def web(url,about_user):
    if url[0:11]!="http://www." or url[0:12]!="https://www.":
        url="https://www."+url
    try:
        page=get(url,headers=about_user[1],cookies=about_user[2])
    except:
        page=post(url,headers=about_user[1],cookies=about_user[2])
