#!D:\Python\python27
# -*- coding:utf-8 -*-
num=6
if num==3:
    print 'boss'
elif num==2:
    print 'user'
elif num==1:
    print 'worker'
elif num<0:
    print 'error'
else:
    print 'roadman'

#if语句多个条件
num=4
if num>=0 and num<=10:
    print 'hello'
else:
    print 'false'

# num=8
if (num>=0 and num<=5)or(num>=10 and num<=15):
    print 'hello'
else:
    print 'false'

#while 循环
count=0
while(count<9):
    print 'the count is :',count
    count+=1

i=1
while i<10:
    i+=1
    if i%2>0:
        continue
    print i

i=1
while i:
    print i
    i+=1
    if i>10:
        break

#通过索引迭代
fruits=['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果：',fruits[index]

for num in range(10,20):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print '%d 等于 %d * %d' % (num,i,j)
            break
    else:
        print num,'是一个质素'

#嵌套循环
i=2
while(i<100):
    j=2
    while(j<=(i/j)):
        if not(i%j): break
        j=j+1
    if(j>i/j): print i,'是素数'
    i+=1

print 'good bye'

#break
for letter in 'python':
    if letter == 'h':
        break
    print '当前字母:',letter

#continum
for letter in 'python':
    if letter =='h':
        continue
    print '当前字母：',letter

var=99
if (var==99): print '变量是99'

print 'byebye'

#字符串更新
var1='hello world'
print '更新字符串:',var1[:6]+'heaven'
#格式字符串
print 'my name is %s and weight is %d kg!'%('kiki', 70)
#删除列表
list1=['ddd', 'gggg', 'rrrr', 'jjjj']
del list1[2]
print list1
#列表截取
print list1[1]
list1[-1]
print list1
list1[2]
list1[-2]
print list1[1:]