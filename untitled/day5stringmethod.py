#!D:\Python\python27
# -*- coding:utf-8 -*-
str='my name is cici'
seq=[1,2,3,4,5]
sea=['1','2','3','4']
sep='+'
print str.find('is')
print str.find('ll')
jions=sep.join(sea)
print sep.join(sea) #join连接的必须是两个字符串
print jions.split('+')#split 是join的逆向
dirs='','usr','bin','env'
print '/'.join(dirs)
print 'C:'+'\\'.join(dirs)#加入了一个转义字符‘\‘
name='Kenven'
print name.lower()#小写字母输出
print name.replace('ven','333')#查找并替换
name1=' space '
name1.strip()#去掉字符两侧的空格，主要用于输入框空格的移除
str2="kiki is haha's ppp dfdfd kkkkk ppppp ccccc"
# str2.translate()#需要一个转换表,然后可以多个替换
from string import maketrans
table=maketrans('k','c')
print str2.translate(table," ")#第一个参数是表，第二个参数是删除指定字符

