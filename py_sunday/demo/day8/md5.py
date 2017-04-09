# -*- coding:utf8 -*-
import hashlib

def get_md5(s):
    md5=hashlib.md5()
    md5.update(s.encode("utf-8"))
    return md5.hexdigest()
db = {}
def register(username,password):
    db[username]=get_md5(password + username +'saltaaa')

def login(username,password):

