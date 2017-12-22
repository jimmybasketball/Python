#!D:\Python\python27
# -*- coding:utf-8 -*-
import logging
import re
import os
import json
logging.basicConfig(level=logging.DEBUG)
#封装方法，私有变量，get，set方法
class Student(object):
    def __init__(self,name,gender):
        self.__name = name #私有变量
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender == 'female' or gender == 'male':
            self.__gender=gender
        else:
            raise ValueError('bad gender')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if value>0 and value<100:
            self._score = value
        else:
            raise ValueError('score must be 0-100')



bart = Student('kiki','male')
bart.get_name()
print bart.get_gender()
bart.set_gender('female')
print bart.get_gender()
#动态语言可以随时给实例绑定任何属性和方法
bart.age = 99
print bart.age
bart.score = 66
print bart.score
#继承和多态:继承父类的方法；子类属于多个类型

print type(u'abd')

#调试logging
s = '1'
n = int(s)
logging.info('n = %d'%n)
print 10/n

# re.search()

#操作文件和目录
print os.name
print os.environ
print os.getenv('PATH')
print os.path.abspath('.')
print os.path.join('C:\Users', 'testdir')
os.mkdir('C:/Users/testdir')
os.rmdir('C:/Users/testdir')

#json 序列化
d = dict(name='bobo', age=20, score=80)
jr = json.dumps(d)
print jr
print json.loads(jr)#反序列化得到的是Unicode不是str
print str(json.loads(jr))
print isinstance(str(json.loads(jr)),str)