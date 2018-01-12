#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
import db
import models
import orm
sys.path.append('C:\Users\Administrator\PycharmProjects\blog-python-app\www')
print time.time()
db.create_engine(user='www-data', password='www-data', database='awesome')
user = db.select('select * from users')
print user

