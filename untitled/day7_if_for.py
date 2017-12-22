#!D:\Python\python27
# -*- coding:utf-8 -*-
age=9
assert 0< age <10,'设置断言，age必选在0-10之间'
#当age不在范围内时就会弹出assert的断言

#zip打包函数,zip可以作用于任意多的序列，当最短的序列用完就停止
names=['aa','bb','cc','dd','ff']
age=[12,34,23,56]
zip(names,age)
for name,age in zip(names,age):
    print name,'is',age,'years old'