#!D:\Python\python27
# -*- coding:utf-8 -*-
str1=raw_input('请输入：')
print str1

str=input('请输入：')
print str

#打开关闭文件

fo=open('foo.txt','wb')
print '文件名',fo.name
print '是否已关闭',fo.closed
print '访问模式',fo.mode
fo.write('www.baidu.com\nvery good\n')
fo.close()
print '是否已关闭',fo.closed
fo=open('foo.txt','r+')
str=fo.read(10)
print str
fo.close()

#文件定位tell seek()

fo=open('foo.txt','r+')
str=fo.read(10)
print '读取的字符串：',str

#查找当前位置

position=fo.tell()
print '当前文件位置',position

#把指针重新定位到文件开头

position=fo.seek(0,0)
str=fo.read(10)
print '重新读取字符串',str
fo.close()

#异常

def tem_convert(var):
    try:
        # print '没有异常'
        return int(var)
        # print '没有异常'
    except ValueError,argument:
        print '参数没有包含数字\n',argument
    else:
        print '没有异常'

tem_convert(str1)