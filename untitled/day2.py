#!D:\Python\python27
# -*- coding:utf-8 -*-
for letter in'pathon':
    print '当前字母',letter

fruits=['apple', 'banana', 'orange']
for frute in fruits:
    print frute

# import pdb
# pdb.set_trace()
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

# 冒泡排序# 定义列表 list
#内置函数 len() 和 range(),函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数
arays = [1,8,2,6,3,9,4]
for i in range(len(arays)):
    for j in range(i+1):
        if arays[i] < arays[j]:
            # 实现连个变量的互换
            arays[i],arays[j] = arays[j],arays[i]
print arays

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print i, " 是素数"
    i = i + 1

print "Good bye!"

import time;  # 引入time模块

ticks = time.time()
print "当前时间戳为:", ticks
localtime = time.localtime(time.time())
print "本地时间为 :", localtime
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime