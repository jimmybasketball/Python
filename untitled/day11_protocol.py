#!D:\Python\python27
# -*- coding:utf-8 -*-
def checkIndex(key):
    if not isinstance(key,(int,long)):raise  TypeError
    if key<0:raise IndexError

class AitSequence:
    def __init__(self,start=0,step=1):
        self.start=start
        self.step=step
        self.changed={}

    def __getitem__(self, key):
        checkIndex(key)

        try: return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
         checkIndex(key)

         self.changed[key]=value


s=AitSequence(1,2)
print s[4]

#迭代器
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs1=Fibs()
for i in fibs1:
    if i>100:
        print i
        break

#生成器,包含yield语句的函数称为生成器，Yield的用法有点像return,除了它返回的是一个生成器
nested=[[1,2],[3,4],[5]]
def flatten(nested):
    for sublist in nested:
        for elemet in sublist:
            yield elemet

for num in flatten(nested):
    print  num

#冲突函数
def conflict(state,nextX):
    nextY=len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):#在一条对角线
            return True
    return  False

#八皇后问题
def queens(num=8,state=()):
        for pos in range(num):
            if not conflict(state, pos):
                if len(state) == num-1:
                    yield (pos,)
                else:
                    for result in queens(num, state+(pos,)):
                        yield (pos,)+result

for solution in queens(8):
    print solution

def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. '*(pos)+'X '+'. '*(length-pos-1)
    for pos in solution:
        print line(pos)

import random
prettyprint(random.choice(list(queens(8))))
