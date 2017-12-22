#!D:\Python\python27
# -*- coding:utf-8 -*-
def story(**kwds):
    return  'once upon a time, there was a '\
            '%(job)s called %(name)s.'%kwds

def power(x,y,*others):
    if others:
        print 'received redundant paramenters:',others
    return pow(x,y)

def interval(start,stop=None,step=1):
    'imitates range () for step>0'
    if stop is None:#如果没有为stop提供值
        start,stop=0,start
    result=[]
    i=start
    while i<stop:
        result.append(i)
        i+=step
    return result

print story(job='king',name='gubmy')#函数的关键字参数不论位置
print story(name='kiki',job='king2')

params={'job':'language','name':'python'}
print story(**params)#调用函数使用星号搜集参数
del params['job']
print story(job='stoke of genius',**params)
print power(2,3)
print power(3,2)#位置参数
print power(x=2,y=3)
params=(5,)*2
print  params
print power(*params)
power(3,3,'hello world')

print interval(10)
print interval(1,5)
print interval(3,12,4)
print power(*interval(3,7))#首先去调interval函数，return【3,4,5,6】，然后前两位幂运算，后面的当字符处理

#函数内部访问全局变量;
parameter='berry'
def combine(parameter):
    print parameter + globals()['parameter']

combine('kiki')

#函数内部定义全局变量,如果不添加global函数内部的变量都是局部变量
x=1
def change_global():
    global x
    x=x+1

change_global()
print x

#二元查找
def search(sequence,number,lower,upper):
    if lower==upper:
        assert number==sequence[upper]
    else:
        middle=(lower+upper)//2
        print middle
        if number>sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,upper)

print search([1,2,3,4,5,6,7,10,23],3)#没看懂