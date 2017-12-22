#!D:\Python\python27
# -*- coding:utf-8 -*-
def application(environ, start_reponse):
    start_reponse('200 ok', [('Content-Type', 'text/html')])
    return '<h1>Hello, web</h1>'