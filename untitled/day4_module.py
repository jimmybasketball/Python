#!D:\Python\python27
# -*- coding:utf-8 -*-
#三种导入模块的方法
from day4_def import sum #1
from day4_def import * #2
import day4_def      #3
day4_def.sum(1, 2)
import math
content=dir(math)
print content