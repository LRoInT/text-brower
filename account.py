from lib import *
import os
import ast
def signin():
    #登录模块
    account=open("account/user",mode="r")
    account_user=account.read()
    account_user=account_user[0:len(account_user)-1]
    account_user="{%s}"%(account_user)
    account_user=ast.literal_eval(account_user)
    user=input("输入你要登录的用户名：")
    if account_user[user] != 'None':
        sin=False
        password=input("请输入密码：")
        while sin==False:
            if sha(password)==account_user[user]:
                #密码哈希是否与储存哈希相同
                sin=True
                print("----------登录成功----------")
            else:
                password=input("----------请重新输入----------\n密码:")
    elif account_user[user]=='None':
        #没有密码，直接登录
        print("----------登录成功----------")
    ua=open("account/{}/ua".format(user),mode="a")
    cookies=open("account/{}/cookies".format(user),mode="a")
    about_user=[ua,cookies]
    account.close()
def new_account():
    account=open("account/user",mode="w+")
    newname=input("设置新账户名称:")
    newpassword=input("设置新账户密码:")
    if len(account.read())!=0:
        account.seek(len(account.read())-1)
    if newpassword=="":
        #不设置密码的情况
        newuser='"{}","None"'.format(newname)
        account.write(account.read()+newuser+",")
    else:
        newuser='"{}":"{}"'.format(newname,sha(newpassword))
        account.write(account.read()+newuser+",")
    os.mkdir("account/{}/".format(newname)) #创建账户信息目录
    open("account/{}/ua".format(newname),mode="a") #创建ua信息存储文件
    open("account/{}/cookies".format(newname),mode="a")
    print("新账户的名称为:{}\n新账户的密码为:{}".format(newname,newpassword))
    account.close()