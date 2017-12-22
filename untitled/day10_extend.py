#!D:\Python\python27
# -*- coding:utf-8 -*-
__metaclass__=type
#构造方法__init__(self)，当一个对象被创建后，会立即调用构造方法
#继承,方法重写
class A:
    def hello(self):
        print 'hello he is A'

class B(A):
    def hello(self):
        print 'he is B'

a=A()
b=B()
a.hello()
b.hello()

class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print 'Aaaah,,,'
            self.hungry=False
        else:
            print 'no,thanks'
b=Bird()
b.eat()
b.eat()
# class SongBird(Bird):
#     def __init__(self):
#         self.sound='squawk'
#     def sing(self):
#         print self.sound
#
# sb=SongBird()
# sb.sing()
# sb.eat()#报错，因为songbird的构造方法重写，没有hungry的特性

# class SongBird(Bird):
#     def __init__(self):
#         Bird.__init__(self)  #直接调用类的方法
#         self.sound='squawk'
#     def sing(self):
#         print self.sound
#
# sb=SongBird()
# sb.sing()
# sb.eat()

#方式二，使用super函数

class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound='squawk'
    def sing(self):
        print self.sound

sb=SongBird()
sb.sing()
sb.eat()