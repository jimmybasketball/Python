#!D:\Python\python27
# -*- coding:utf-8 -*-
__author__ = 'jimmy'

import requests
import re
import urllib

mp3data=[]
for ii in range(0,2):
    #寻找歌曲的列表页，点击下一页，找到musiclist
    url='http://www.htqyy.com/genre/musicList/11?pageIndex='+ str(ii) +'&pageSize=20&order=hot'
    html=requests.request('POST', url)
    #分析返回值，找到关键字段value
    mp3data.extend(re.findall(r'value="(.*?)"><span', html.text))
    # print html.text
    #选择歌曲追踪数据，找到value的对应歌曲的原始数据
all_song_url=list(map(lambda ii:'http://f1.htqyy.com/play6/' +ii+ '/mp3/1',mp3data))
print all_song_url
kk=0
for jj in all_song_url:
    try:
        urllib.urlretrieve(jj, 'F:\\downloads\\song\\'+mp3data[kk]+ '.mp3')
    except Exception as err:
        print '这个歌曲不能下载',mp3data[kk]
        print err
    kk+=1