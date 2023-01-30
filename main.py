import sys
from lib import *
from pyhtml import rqurl
over=False
about_user=[{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70"},{"cookies":""}]
"""
while True:
    
    登录模块，由于ua，cookies加密存储和账户文件验证没有解决只能暂时注释掉
    command=input("登录账户 | 创建账户\n选项:")
    if command=="登录账户":
        about_user=signin()
        break
    elif command=="创建账户":
        new_account()
        break
    else:
        print("-----------错误-----------")
        command=input("登录账户 | 创建账户\n选项:")
"""

while True:
    command=input("准备执行命令:")
    if command[0:5]==r"%url%":
        url=command[6:]
        rqurl(url,about_user)
    elif command==r"%exit%":
        sys.exit()
