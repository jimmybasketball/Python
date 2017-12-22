#!D:\Python\python27
# -*- coding:utf-8 -*-
try:
    x=input('enter the first number:')
    y=input('enter the second number:')
    print x/y
except (ZeroDivisionError,TypeError):#可以加入多个异常
    print "the second can't be 0"
except TypeError:
    print 'input the number'
#捕捉异常

try:
    x=input('enter the first number:')
    y=input('enter the second number:')
    print x/y
except (ZeroDivisionError,TypeError),e:
    print e

#全捕捉，这样做很危险，会捕捉函数终止的企图

try:
    x=input('enter the first number:')
    y=input('enter the second number:')
    print x/y
except:
    print 'something is wrong'

#try except else

try:
    print 'A simple task'
except:
    print 'something is wrong'
else:
    print 'it is as planned'
#finally,finally语句肯定会被执行

try:
    1/0
except:
    print 'error'
else:
    print 'that was well'
finally:
    print 'cleaning up'