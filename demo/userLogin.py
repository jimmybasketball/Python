#!D:\Python\python27
# -*- coding:utf-8 -*-
import sqlite3
conn = sqlite3.connect('demo.db')
curs = conn.cursor()
sql = 'select name from USER WHERE NAME = INPUT '