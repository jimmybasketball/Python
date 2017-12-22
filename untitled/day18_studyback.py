#!D:\Python\python27
# -*- coding:utf-8 -*-
from multiprocessing import process
from multiprocessing import pool
import os

def run_proc(name):
    print'run child process %s(%s'%(name,os.getpgid())

