#!D:\Python\python27
# -*- coding:utf-8 -*-
import unittest

from Reload_Driver import *


class BasePage(unittest.TestCase, load):
    '''加载浏览器，初始化测试环境'''

    def setUp(self):
        self.driver = self.reloadDriver()

        self.driver.maximize_window()

        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
