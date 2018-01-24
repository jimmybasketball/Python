#!D:\Python\python27
# -*- coding:utf-8 -*-
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
@app.route('/')
def index():
    return render_template('index.html', current_time = datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello World,%s!</h1>' % name

@app.route('/user1/<name>')
def user1(name):
    # return '<h1>Hello World,%s!</h1>'%name
#使用jinja模板
    return render_template('user1.html', name=name)

@app.route('/user2/<name>')
def user2(name):
    return render_template('user2.html', name=name, current_time = datetime.utcnow())
#从base.html继承

#错误页面处理
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

class NameForm(Form):
    name = StringField('whta\'s your name', validators=[Required()])
    submit = SubmitField('submit')

if __name__=='__main__':
    app.run(debug=True)
    # manager.run()


