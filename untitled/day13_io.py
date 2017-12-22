#!D:\Python\python27
# -*- coding:utf-8 -*-
from pprint import pprint
import fileinput
import time
f = open(r'f:\somefile.txt')
pprint(f.read())
f.close()

f = open('f:\somefile.txt', 'w')
f.write('continue+3333\r\nhello\r\nworld\r\njimmy')
f.close()
f = open('f:\somefile.txt', 'r')
pprint(f.read())
f.close()

f = open(r'f:\somefile.txt')
for i in range(4):
    print str(i) + ':' + f.readline()
pprint(open(r'f:\somefile.txt').readlines())

f = open(r'f:\somefile.txt','w')
f.write('this\nis\nno\nhaiku')
f.close()

f = open(r'f:\somefile.txt')
lines=f.readlines()
f.close()
lines[1] = "isn't a\n"
f = open(r'f:\somefile.txt','w')
f.writelines(lines)
f.close()

f = open(r'f:\somefile.txt')
while True:
    line = f.readline()
    if not line:break
    pprint(line)
f.close()
#懒惰迭代，实现上面这个while循环
for line in fileinput.input('f:\somefile.txt'):
    pprint(line)

str ='mingjie@gutou.com'
pprint(sorted(str))
s=''.join(sorted(list('mingjei@gutou.com')))
pprint(s)

print time.time()