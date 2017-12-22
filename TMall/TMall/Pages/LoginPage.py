#!D:\Python\python27
# -*- coding:utf-8 -*-
import time

from selenium.webdriver.common.by import By

from TMall.Common.PageElemnt import *
from TMall.Common.Common import Comon


class LoginPage(PageObject, Comon):
    '''
    登录界面
    '''

    def __init__(self, driver, shopname):
        '''
        登录初始化
        :param driver  驱动
        :param shopName 店铺名称
        '''
        PageObject.__init__(self, driver=driver)
        self.username = shopname
        self.problem = self.get_shop_cfg(shopname)["valid"]

    def findQR(self):
        '''获取二维码'''
        while True:
            METHOD = By.XPATH, ".//*[@id='J_QRCodeImg']/img"
            mark = self.findElemenAcctLocated(*METHOD)
            if mark:
                try:
                    mark_url = mark.get_attribute('src').encode('utf-8')
                    if mark_url:
                        now_time = time.strftime('%Y年%m月%d日%H点%M分%S秒 ', time.localtime(time.time()))
                        params = now_time, self.username, mark_url, self.username
                        send_ok = self.send_ding(self.username, *params)
                        if send_ok:
                            self.wait(30)
                            login_user = self.find_login_user()
                            if login_user:
                                if login_user != self.username:
                                    self.find_logout()
                                else:
                                    return True
                            else:
                                self.driver.refresh()
                                self.wait()
                        else:
                            return False
                    else:
                        return False
                except:
                    return False
            else:
                return False

    def find_login_user(self):
        '''查找登录用户名'''
        self.find_secrity()
        METHOD = By.XPATH, ".//*[@id='login-info']/a[1]"
        login_user = self.findElemenAcctLocated(*METHOD)
        if login_user and login_user.is_displayed():
            login_user_text = login_user.text.encode('utf-8')
            return login_user_text
        else:
            return None


    def find_secrity(self):
        '''获取安全验证'''
        METHOD = By.XPATH, ".//div[2]/div[2]/iframe"
        secrity_ifram = self.findElement(*METHOD)
        if secrity_ifram and secrity_ifram.is_displayed():
            self.driver.switch_to_frame(secrity_ifram)
            METHOD2 = By.XPATH, ".//form[@id='J_Question']/ul/li[2]/span/input"
            input_valid = self.findElement(*METHOD2)
            if input_valid and input_valid.is_displayed():
                input_valid.clear()
                input_valid.send_keys(unicode(self.problem, 'utf-8'))
                self.wait()
                METHOD3 = By.ID, "J_FooterSubmitBtn"
                submit_btn = self.findElement(*METHOD3)
                submit_btn.click()
            else:
                pass
        else:
            pass

    def find_logout(self):
        '''退出'''
        METHOD = By.ID, "J_Logout"
        logout = self.findElemenAcctLocated(*METHOD)
        if logout:
            logout.click()
            self.wait(5)
        else:
            pass

