#!D:\Python\python27
# -*- coding:utf-8 -*-
import math
def testabc(a,b,c):
    try:
        x = (math.sqrt(b*b-4*a*c)-b)/2/a
        y = (-math.sqrt(b * b - 4 * a * c) - b) / 2 / a
        return int(x),int(y)
    except:
       print '输入错误，无解'


print testabc(1,6,5)
print testabc(2,4,2)


def product(*number):
    result = 1
    for i in number:
        result = result*i
    return result


print product(2, 3, 4)
print product(5)

str1 = ' sdfasdfa  '
print str1.strip()


def max_value(l):
    max1 = l[0]
    for i in l:
        if i>max1:
            max1 = i
    return max1




print max_value((1,6,3,9,30,9))

#要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做,用列表生成式
aa = [x*x for x in range(1,10)]
print aa
bb = [x*x for x in range(1,10) if x%2 == 0]
print bb
cc = [m+n for m in 'ABC' for n in 'XYZ']
print cc
L = ['Hello', 'World', 18, 'Apple', None]
L1 = [s.lower() for s in L if isinstance(s, str)]
print L1

#生成器：
#第一种：只要把一个列表生成式的[]改成()，就创建了一个generator,取值用for循环
ww = (x*x for x in range(1,10))
print ww
for i in ww:
    print i


#第二种：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# def fib(maxn):
#     n,a,b=0,0,1
#     while n<maxn:
#         print(b)
#         a,b=b,a+b
#         # 这种赋值，先计算等值 右边 那么 b=1 a+b=1
#         # 再赋值给a和b，那么 a=1, b=1
#         n=n+1
#
# fib(6)

def fib(maxn):
    n,a,b=0,0,1
    while n<maxn:
        yield b
        a,b=b,a+b
        # 这种赋值，先计算等值 右边 那么 b=1 a+b=1
        # 再赋值给a和b，那么 a=1, b=1
        n=n+1


f = fib(6)
#生成器的执行：最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

print next(f)
print next(f)
print next(f)


