#!D:\Python\python27
# -*- coding:utf-8 -*-
import unittest
import time as t
import sys

from HTMLTestRunner import HTMLTestRunner

from TMall.Common.Common import *

reload(sys)
sys.setdefaultencoding('utf-8')


class Test(Comon):
    '''执行测试并生成测试报告'''

    @property
    def __getReportPath(self):
        '''获取测试报告的生成路径'''
        now = t.strftime("%Y%m%d%H%M%S", t.localtime(t.time()))
        return unicode(self.filePath("Report\\") + now + "Report.html", 'utf-8')

    def run(self):
        '''运行测试用例'''
        with open(self.__getReportPath, 'wb') as fp:
            discover = unittest.defaultTestLoader.discover \
                (
                    self.filePath('Cases'),
                    pattern='test_*.py'
                )
            runner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"测试报告")

            runner.run(discover)






