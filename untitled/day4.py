#!D:\Python\python27
# -*- coding:utf-8 -*-
list01=['kiki', 5676, 3.44, 'john', 50.3]
list02=[123, 'john']

print list01
print list02

#列表截取

print list01[0]
print list01[-1]
print list01[0:3]

#列表重复

print list01*2

#列表组合

print list01+list02

#获取类别长度

print len(list01)

#删除类别元素

del list02[0]
print list02

#元素是否存在列表中

print 'john' in list02

#迭代

for i in list01:
    print  i

#比较两个列表的元素

print cmp(list01,list02)

#列表最大\最小

print max([0, 1, 3, 5, 23])

#将元组转换为列表

aTuple=(1, 2, 3, 4)
list03=list(aTuple)
print list03

#在列表末尾添加新的元素

list03.append(5)
print  list03

#用新列表扩展原来的列表

list03.extend(list01)
print list03

#统计某个元素在列表中出现的次数

print list03.count(1)

#从列表中找出某个值第一个匹配项的索引位置

print list03.index('john')

#将对象插入列表

list03.insert(1,'hello222')
print list03

#移除列表中的一个元素（最后一个），并且返回改元素的值

print list03.pop()
print list03

#移除列表中的第一个匹配项

list03.remove(5)
print list03

#反向列表中的元素

list03.reverse()
print list03

#对原列表进行排序

list03.sort()
print list03

#元组中只包含一个元素时，需要在元素后面添加逗号

tup1=(5,)

#访问字典里的值

dict={'name': 'zara', 'age': 45, 'class': 4}
print dict['name']

dict['age']=10
dict['school']='dps school'
print dict

#删除字典元素

del dict['name'] #删除健name的条目
dict.clear() #清空词典所有条目
del  dict #删除词典
print dict

#字典中键的特性，键必须唯一；键必须不可变，可以是数字，字符串或元组，不能是列表

dict={['name']: 'zara', 3: 4}



