#!D:\Python\python27
# -*- coding:utf-8 -*-
import time as t

from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Common import *


class PageObject(Comon):
    def __init__(self, driver):
        '''
        页面需要的参数
        :param driver 驱动地址
        :param username 登录的账户名
        '''
        self.driver = driver


    def wait(self, time=2):
        t.sleep(time)

    @property
    def getUrl(self):
        '''获取当前页面的服务地址'''

        return self.driver.current_url

    def getCurrentWindow(self):
        '''获取当前窗口句柄'''
        self.wait()

        return self.driver.current_window_handle

    def getWindows(self):
        '''获取所有窗口的句柄'''

        self.wait()

        return self.driver.window_handles

    def screen_page(self, img_path):
        '''
        获取当前截图
        :param img_path 图片地址
        '''
        base_path = os.path.dirname(unicode(img_path))  ##图片目录地址
        base_name = os.path.basename(unicode(img_path, 'utf-8'))  ##图片名称
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        else:
            pass
        os.chdir(base_path)
        self.driver.get_screenshot_as_file(base_name)

    def findElement(self, *loc):
        '''
        查找单个元素
        @loc  tuple参数
        '''
        try:
            self.wait()

            return self.driver.find_element(*loc)

        except NoSuchElementException:
            return None

    def findsElement(self, *loc):
        '''
        查找多个元素
        @loc  tuple参数
        '''
        try:
            self.wait()

            return self.driver.find_elements(*loc)

        except:
            return None

    def findByElement(self, elment, *loc):
        '''
        通过元素去定位元素
        @elment    父级元素
        @loc   子级定位地址
        '''
        try:
            self.wait()

            return elment.find_element(*loc)

        except:
            return None

    def findsByElement(self, elment, *loc):
        '''
        通过元素去定位元素
        @loc    父级元素
        @loc1   子级定位地址
        '''
        try:
            self.wait()

            return elment.find_elements(*loc)

        except:
            return None

    def findElemenAcctClick(self, *loc):
        '''
        查找元素是否可以点击
        :param  *loc:  tuple type
        '''
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))

        except:
            return None

    def findElemenAcctDisplay(self, *loc):
        '''
        查找元素是否显示
         :param  *loc:  tuple type
        '''
        try:
            return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loc))
        except:
            return None

    def findElemenAcctLocated(self, *loc):
        '''
        查找元素是否存在
         :param  *loc:  tuple type
        '''
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))
        except:
            return None

