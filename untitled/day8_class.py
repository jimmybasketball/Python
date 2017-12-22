#!D:\Python\python27
# -*- coding:utf-8 -*-
_metaclass_=type

class Person:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def greet(self):
        print "hello world i'm %s"%self.name

foo=Person()
foo.setName('kiki')
foo.greet()


class Employee:
    '所有员工基类'
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print 'Total employee %d'%Employee.empCount

    def displayEmployee(self):
        print 'name:',self.name,'salary:',self.salary

emp1=Employee('kiki',2000)
emp2=Employee('cici',3000)
emp1.displayEmployee()
emp2.displayCount()
emp1.age=7#还可以添加类的属性，好逆天
print emp1.age
#内置属性

print Employee.__bases__
print Employee.__doc__
print Employee.__dict__
print Employee.__name__

#继承实例
class Parent:
    parentArr=100
    def __init__(self):
        print '调用父类构造函数'

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self,attr):
        Parent.parentArr=attr

    def getAttr(self):
        print '父类属性：',Parent.parentArr

class Child(Parent):
    def __init__(self):
        print '调用子类构造方法'

    def childMethod(self):
        print '调用子类方法'

c=Child() #实例化子类
c.childMethod()
c.parentMethod()
c.setAttr(100)
c.getAttr()