#!D:\Python\python27
# -*- coding:utf-8 -*-
#根据给定的年月日打印出日期格式

months={1: 'January',2:'February',3:'March',4:'April',5:'May',6:'June',\
        7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
year=raw_input('year:')
month=raw_input('month(1-12):')
days=raw_input('day(1-31)：')
month_number=int(month)
days_number=int(days)
month_name=months[month_number]
days_name=days+endings[days_number-1]
print month_name+' '+days_name+' '+year