#!D:\Python\python27
# -*- coding:utf-8 -*-
'''然后写一个app.py，处理3个URL，分别是：

    GET /：首页，返回Home；

    GET /signin：登录页，显示登录表单；

    POST /signin：处理登录表单，显示登录结果。

注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。'''
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin'  and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='bad username or password', username=username)

if __name__=='__main__':
    app.run()

