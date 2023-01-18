import sys
from requests import *
from lib import *
from account import *
import subprocess
about_user=[]
over=False
while True:
    command=input("登录账户 | 创建账户\n选项:")
    if command=="登录账户":
        signin()
        break
    elif command=="创建账户":
        new_account()
        break
    else:
        print("-----------错误-----------")
        command=input("登录账户 | 创建账户\n选项:")
while over!=True:
    command=input("准备执行命令:")
    if command[0:5]==r"%url%":
        url=command[5:]
        subprocess.Popen(["pyhtml.py",url,about_user[1],about_user[2]])
