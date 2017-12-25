#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

from models import User, Blog, Comment

from transwarp import db

db.create_engine(user='www-data', password='www-data', database='awesome')

u = User(name='Test', email='tes1t@example.com', password='12345678901', image='about:blank')
print u

u.insert()

print 'new user id:', u.id

u1 = User.find_first('where email=?', 'test@example.com')
print 'find user\'s name:', u1.name

u1.delete()

u2 = User.find_first('where email=?', 'test@example.com')
print 'find user:', u2
