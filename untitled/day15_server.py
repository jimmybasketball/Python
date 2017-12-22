#!D:\Python\python27
# -*- coding:utf-8 -*-
import socket
#服务端
s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)
while True:
    c,addr = s.accept()
    print 'Got connection from ',addr
    c.send('thank U for connecting')
    c.close()



