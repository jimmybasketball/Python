#coding=utf-8
#!D:\Python\python27
import requests
import json

url = 'https://api.douban.com/v2/movie/search'
params=dict(q=u'刘德华')
r = requests.get(url, params=params)
print 'Search Params:\n', json.dumps(params, ensure_ascii=False)#将 Python 对象编码成 JSON 字符串。
print 'Search Response:\n', json.dumps(r.json(), ensure_ascii=False, indent=4)