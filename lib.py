from hashlib import *
def sha(date):
    #哈希256加密
    hash = sha256()
    date=str(date)
    hash.update(date.encode(encoding='utf-8'))
    shacode = hash.hexdigest()
    del hash
    return shacode