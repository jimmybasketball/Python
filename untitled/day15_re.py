#!D:\Python\python27
# -*- coding:utf-8 -*-
import re
def validateEmailFront(addr):
   if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',addr):
       print 'ok'
       return True
   else:
    print 'false'


validateEmailFront('someone@gmail.com')
# assert validateEmailFront('bob#example.com')
assert validateEmailFront('mr-bob@example.com')

def nameOfEmail(addr):
    m = re.search('[a-zA-Z0-9_-]+@', addr)
    name=m.group()
    name[:-1]
    print name[:-1]
    return None
nameOfEmail('jimmy@qq.com')
