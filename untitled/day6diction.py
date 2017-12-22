#!D:\Python\python27
# -*- coding:utf-8 -*-
people={
    'Alice'.lower():{
        'phone':'2341',
        'addr':'Foo drive 23'
    },
    'Beth'.lower():{
        'phone':'3333',
        'addr':'Bar street 42'
    },
    'Cecil'.lower():{
        'phone':'0009',
        'addr':'Baz avenue 90'
    }
}

labels={
    'phone':'phone number',
    'addr':'address'
}

name=raw_input('Name:').lower()
request=raw_input('phone number(p) or address(a):')
#如果请求非法
key=request
if request=='p':key='phone'
if request == 'a':key='addr'

# if name in people: print "%s's %s is %s"%(name,labels[key],people[name][key])

#使用get方法来处理异常

person=people.get(name,{})
label=labels.get(key,key)
result=person.get(key,'not availabel')
print "%s's %s is %s"%(name,label,result)
#把lower（）方法加到name.lower(）中就有error？
# import day4_def
# day4_def.sum(2,3)

# phonebook={'alice':'1111', 'beth':'2222','cici':'3333'}
# print "cici's phone number is %s"%phonebook['cici']
# #另一种字典格式化,在转换格式符（%）后加上键（用圆括号括起来）再更上说明元素（比如字符s，数字d）
# print "cici's phone number is %(cici)s"%phonebook

#检查字典中是否含有给出的键值
d={}
d.has_key('name')

#items iteritems 将字典项返回
print people.items()

#pop 将键值对应的项删除
d={'x':1, 'y':2}
d.pop('x')
print d

#popitem 删除弹出的随机项

#setdefault 设定默认值

d={}
d.setdefault('name','N/A')
print d

#update 可以利用一个字典项更新另外一个字典
x={'title':'hhh'}
d.update(x)
#values 已列表的形式返回字典的值

print d.values()