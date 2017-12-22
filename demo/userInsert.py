#!D:\Python\python27
# -*- coding:utf-8 -*-
import sqlite3
import xlrd
conn = sqlite3.connect('demo.db')
curs = conn.cursor()
#建表
# curs.execute('''
# CREATE TABLE user(
# name text,
# password text
# )
# ''')
sql = 'insert into user VALUES (?,?)'

# 打开文件
workbook = xlrd.open_workbook(r'F:\user.xlsx')
sheet1 = workbook.sheet_by_name(sheet_name='Sheet1')

for i in range(1, sheet1.nrows):
    vals = [sheet1.cell(i, 0).value, sheet1.cell(i, 1).value]

    curs.execute(sql, vals)

curs.execute('SELECT *FROM user')
print curs.fetchall()
conn.close()

