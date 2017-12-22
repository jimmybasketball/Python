#!D:\Python\python27
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
from hello import application
httpd = make_server('', 8866, application)
print 'Serving http on port 8000...'
httpd.serve_forever()