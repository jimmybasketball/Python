#!D:\Python\python27
# -*- coding:utf-8 -*-
import urllib2
import json

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers


class load_http(object):
    '''http请求'''

    def __init__(self, **param):
        self.url = param.pop('url')  ###请求地址
        self.imgParams = self.__joinData(**param)  ##请求参数


    def __joinData(self, **param):
        '''
        处理已有数据,有图片时组装图片
        :param param 已有数据
        '''
        if param.has_key('path'):
            param["picture"] = open(param["path"], 'rb')  ###图片上传
        else:
            pass

        return param

    def getMsg(self):
        '''请求数据'''
        register_openers()

        datagen, headers = multipart_encode \
            (
                self.imgParams
            )

        self.request = urllib2.Request(self.url, datagen, headers)

        return self.__sendMsg(self.request)


    def __sendMsg(self, request):
        '''
        开始请求
        :param request 请求连接至
        '''
        try:
            response = urllib2.urlopen(request)
            response = response.read().decode('utf-8')
            msg = json.loads(response, encoding='utf-8')
            return msg
        except:
            return None
















