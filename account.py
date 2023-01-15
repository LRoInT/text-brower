from lib import *
def signin():
    account=open("account/user",mode="r")
    account_user=account.read()
    a0=account_user
    t0=type(account_user)
    account_user=account_user.split(",")
    a1=account_user
    t1=type(account_user)
    account_user=account_user[0:len(account_user)-1]
    a2=account_user
    t2=type(account_user)
    account_user=tuple(account_user)
    account_user=account_user[0:len(account_user)]
    a3=account_user
    account_user=dict(account_user)
    user=input("输入你要登录的用户名：")
    if account_user[user] != 'None':
        sin=False
        password=input("请输入密码")
        while sin==False:
            if sha(password)==account_user[user]:
                sin=True
                print("----------登录成功----------")
            else:
                password=input("----------请重新输入----------\n密码:")
    elif account_user[user]=='None':
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
        newuser="['{}','None']".format(newname)
        account.write(account.read()+newuser+",")
    else:
        newuser="['{}','{}']".format(newname,sha(newpassword))
        account.write(account.read()+newuser+",")
    print("新账户的名称为:{}\n新账户的密码为:{}".format(newname,newpassword))
    account.close()