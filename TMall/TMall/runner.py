#!D:\Python\python27
# -*- coding:utf-8 -*-
import multiprocessing

from TMall.Main.Main import *
from TMall.Common.ScanThread import *


def start_case():
    while True:
        Test().run()


def start_img():
    while True:
        sysnc_Img().sync_file()


if __name__ == '__main__':
    monitor_case = multiprocessing.Process(target=start_case)
    monitor_case.daemon = True
    monitor_case2 = multiprocessing.Process(target=start_img)
    monitor_case2.daemon = True
    monitor_case.start()
    monitor_case2.start()
    monitor_case.join()
    monitor_case2.join()
