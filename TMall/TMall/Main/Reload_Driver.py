#!D:\Python\python27
# -*- coding:utf-8 -*-
from selenium import webdriver

from TMall.Common.Common import *


class load(Comon):
    '''加载配置'''

    @property
    def getDriver(self):
        '''获取浏览器驱动地址'''
        return self.read_cfg("URLPATH")["driver"]

    @property
    def getPrefs(self):
        '''构建浏览器的配置'''
        return \
            {
                'profile.default_content_settings.popups': 0,
                'download.default_directory': self.filePath('Files\\DownLoad')
            }

    @property
    def getOptions(self):
        '''构建浏览器的Option配置'''
        options = webdriver.ChromeOptions()

        options.add_experimental_option('prefs', self.getPrefs)

        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

        return options


    def reloadDriver(self):
        '''加载浏览器配置'''
        chrome_drover = self.getDriver

        os.environ["webdriver.chrome.driver"] = chrome_drover

        return webdriver.Chrome(chrome_drover, chrome_options=self.getOptions)






