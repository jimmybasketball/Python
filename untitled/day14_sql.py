#!D:\Python\python27
# -*- coding:utf-8 -*-
import  sqlite3
#数据库建立链接
# conn = sqlite3.connect('somedatabase.db')
# curs = conn.cursor()
# conn.commit()
# conn.close()

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return  float(value)

conn = sqlite3.connect('foot.db')
curs = conn.cursor()
# curs.execute('''
# CREATE TABLE food2(
#   id text PRIMARY KEY ,
#   DESC text,
#   water float,
#   kcal float,
#   protein float,
#   fat float,
#   ash float,
#   carbs float,
#   fiber float,
#   sugar float
# )
#
# ''')

# query = 'insert into food VALUES (?,?,?,?,?,?,?,?,?,?)'
#
# for line in open(r'f:\ABBREV.txt'):
#     fields = line.split('^')
#     vals = [convert(f) for f in fields[:10]]
#     print vals
#     #执行sql
#     curs.execute(query, vals)
# conn.commit()
# conn.close()

#查询数据库
conn = sqlite3.connect('foot.db')
c = conn.cursor()
query = 'select * from food WHERE  kcal<=100 AND  fiber>=10 ORDER  BY sugar'
c.execute(query)
print c.fetchone()
print c.fetchall()
c.close()
conn.close()

#异常处理rollback
conn = sqlite3.connect('foot.db')
c = conn.cursor()
query = 'insert into food VALUES (?,?)'
try:
    c.execute(query, ('1', 'test'))

    conn.commit()
except Exception as e:
    print e
    conn.rollback()

c.close()
conn.close()
