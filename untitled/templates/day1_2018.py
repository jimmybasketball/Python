#!D:\Python\python27
# -*- coding:utf-8 -*-
a=[]
for i in range(90,64,-1):
    a.append(chr(i))
for j in range(122,96,-1):
    a.append(chr(j))

print "".join(a)
for i in range(122,96,-1):
    print chr(i) + chr(i-32)