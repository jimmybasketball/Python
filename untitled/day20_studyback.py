#!D:\Python\python27
# -*- coding:utf-8 -*-
from collections import namedtuple
point = namedtuple('point',['x', 'y'])#定义坐标点
p = point(1,2)
print p.x

#base64
import base64

print base64.b64encode(b'dasdasdfa111222')#编码
print base64.b64decode(b'ZGFzZGFzZGZhMTExMjIy')#解码
print base64.urlsafe_b64encode(b'www.baidu.com\html/+')

#哈希算法MD5 SHA1


import hashlib

aa = hashlib.md5()#md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
aa.update('admin'.encode('utf-8'))
#要对哪个字符串进行加密，就放这里
print(aa.hexdigest())#拿到加密字符串


# hashlib简单使用
import sqlite3
def md5(arg):  # 这是加密函数，将传进来的函数加密
    md5_pwd = hashlib.md5('abd'.encode('utf-8'))
    md5_pwd.update(arg.encode('utf-8'))
    return md5_pwd.hexdigest()  # 返回加密的数据


def log(user, pwd):  # 登陆时候时候的函数，由于md5不能反解，因此登陆的时候用正解
    with open(r'f:\user.txt') as f:
        for line in f:
            u, p = line.strip().split('|')
            if u == user and p == md5(pwd):  # 登陆的时候验证用户名以及加密的密码跟之前保存的是否一样
                return True


def register(user, pwd):  # 注册的时候把用户名和加密的密码写进文件，保存起来
    with open(r'f:\user.txt', 'a')as f:
        temp = user + '|' + md5(pwd)
        f.write(temp+'\n')


i = raw_input('1表示登陆，2表示注册：')
if i == '2':
    user = raw_input('用户名：')
    pwd = raw_input('密码：')
    register(user, pwd)
elif i == '1':
    user = user = raw_input('用户名：')
    pwd = raw_input('密码：')
    r = log(user, pwd)  # 验证用户名和密码
    if r == True:
        print('登陆成功')
    else:
        print('登陆失败')
else:
    print('账号不存在')


