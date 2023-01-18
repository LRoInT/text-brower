from hashlib import *
import rsa
def sha(date):
    #哈希256加密
    hash = sha256()
    date=str(date)
    hash.update(date.encode(encoding='utf-8'))
    shacode = hash.hexdigest()
    del hash
    return shacode

"""
RSA部分是用来加密ua,cookies,历史记录……那些数据的的。但由于私钥过长暂时没办法用上（有人有建议的话可以写在issues里，谢谢）
"""

def rsaEncrypt(date): #RSA加密函数
    key_pub,key_pri = rsa.newkeys(1024)
    crypto = rsa.encrypt(date,key_pub)
    return (crypto,key_pri,key_pub) #密文 & 私钥 & 公钥


def rsaDecrypt(date,key_pri): #RSA解密函数
    #输入密文和私钥
    content = rsa.decrypt(date,key_pri) #明文
    return content.decode('utf-8')