#!D:\Python\python27
# -*- coding:utf-8 -*-
def printme(str):
    '说明：这是一个打印函数'
    print str
    return

printme('00000')

#参数传递

#传不可变的对象

def changeInt(a):
    a=10

b=2
changeInt(b)
printme(b)

#传可变的对象
def changeMe(mylist):
    '修改传入的列表'
    mylist.append([1, 2, 3, 4])
    print '函数内取值',mylist
    return

list00=[10, 20, 30]
changeMe(list00)
print '函数外取值',list00

#关键字参数顺序可以调换

def printinfo(name, age):
    print 'name:',name
    print 'age',age
    return

printinfo(age=33, name='kiki')

#缺省参数

def printinfo(age=50, name='ll'):
    print 'name:',name
    print 'age:', age
    return

printinfo(age=20, name='cici')
printinfo(name='pipi')
printinfo(90)

#不定长参数

def printinfo(arg1, *vartuple):
    print '输出'
    print arg1
    for var in vartuple:print  var
    return

printinfo(22)
printinfo(10, 20, 30, 'lol')

#函数的返回
total=2
def sum(arg1, arg2):
    total=arg1+arg2
    print total #局部变量
    return total

ll=sum(22, 33)
print ll
print total #全局变量

