#!D:\Python\python27
# -*- coding:utf-8 -*-
#URLLIB
import urllib2

with urllib2.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f
    # print ('Status:',f.status, f.reason)
    print f
