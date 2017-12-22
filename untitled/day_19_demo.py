#!D:\Python\python27
# -*- coding:utf-8 -*-
import re

def httpvalidate1(file):
    http = []
    with open(file) as ft:
        for line in ft.readlines():
         m = re.search('((http[s]{0,1})://[\d\w\.\/\-\?\=]+)',line)
         http.append(m.group())
    return http


print httpvalidate1('f:\demofile.txt')



