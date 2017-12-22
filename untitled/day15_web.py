#!D:\Python\python27
# -*- coding:utf-8 -*-
from urllib import *
import re
webpage = urlopen('http://www.python.org')
print webpage
text = webpage.read()
# print text
m = re.search('<a href="([^"])+" .*?>About</a>',text,re.IGNORECASE)#忽略大小写
print m.group()

# urlretrieve('http://www.python.prg', 'F:\\pythonWebpage.html')
#保存远程文件
