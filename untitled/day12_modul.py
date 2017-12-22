#!D:\Python\python27
# -*- coding:utf-8 -*-
import copy
print dir(copy)
for n in dir(copy):
    if not n.startswith('_'):
        print n

#sys 标准模块
import sys
args=sys.argv[1:]
args.reverse()
print ''.join(args)

a=set([1,2,3])
b=set([2,3,4])
print a.union(b)
c=set()
d=set()
# c.add(d)
c.add(frozenset(d))
#集合本身只能包含不可变的值，frozenset创建给定集合的副本

from heapq import *
from random import shuffle
data = range(10)
shuffle(data)
heap = []
for n in data:
    heappush(heap,n)

print heap

#随机数
from random import randrange
num = input('How many dice?')
sides = input('How many sides per die?')
sum = 0
for i in range(num):sum += randrange(sides) + 1
print 'Result is :',sum

#给自己发牌
values = range(1,11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v,s) for v in values for s in suits]
from pprint import pprint
shuffle(deck)
pprint(deck[:12])
while deck:raw_input(deck.pop())
