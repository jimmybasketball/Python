#!D:\Python\python27
# -*- coding:utf-8 -*-
import win32api

import win32con
from selenium.webdriver.common.action_chains import ActionChains

from LoginPage import *


class GoodList(LoginPage):
    '''商品列表页'''

    def __init__(self, driver, shopname):
        LoginPage.__init__(self, driver, shopname)


    def input_order(self, order):
        '''
        订单号输入框
        :param order 订单号
        '''
        METHOD = By.ID, "bizOrderId"
        orderInput = self.findElemenAcctLocated(*METHOD)
        if orderInput:
            self.driver.execute_script("arguments[0].scrollIntoView();", orderInput)
            orderInput.clear()
            orderInput.send_keys(order)
        else:
            pass

    def searchButton(self):
        '''查询订单按钮'''
        try:
            METHOD = By.XPATH, ".//*[@id='sold_container']/div/div[1]/div[1]/form/div[7]/div/div/button[1]"
            search = self.findElemenAcctLocated(*METHOD)
            ActionChains(self.driver).move_to_element(search).perform()
            search.click()
            self.wait()
            return True
        except:
            return False


    def qingguan_mess(self, flag):
        '''清关材料链接'''
        params = {}
        current_window = self.getCurrentWindow()
        METHOD = By.LINK_TEXT, "查看清关材料"
        try:
            qingguan = self.findElemenAcctClick(*METHOD)
            if qingguan and qingguan.is_displayed():
                qingguan.click()
                self.wait(3)
                all_windows = self.getWindows()
                for window in all_windows:
                    if window != current_window:
                        self.driver.switch_to_window(window)
                        self.driver.refresh()
                        self.wait()
                        order = self.__getOrder()
                        if order:
                            params["tid"] = order
                            username = self.getUserName()
                            if username:
                                params["realname"] = unicode(username)
                                cardId = self.getCardId()
                                if cardId:
                                    params["id_card"] = cardId
                                    self.__getImag()
                                    params["from"] = flag
                                    self.save_idcard(**params)
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                        self.driver.close()
                        self.driver.switch_to_window(current_window)
                        self.wait()
            else:
                pass
        except:
            self.driver.refresh()

    def __getOrder(self):
        '''
        获取订单号
        :param div:父级元素
        '''
        patthon = u'&id=(.*)'
        current_url = self.driver.current_url
        search_url = re.search(patthon, current_url)
        if search_url:
            return search_url.group(1)
        else:
            return None


    def getUserName(self):
        '''获取用户名'''
        user_path = By.XPATH, ".//div[@id='id-card']/div[2]/table/tbody/tr[2]/td[2]"

        user_name = self.findElemenAcctLocated(*user_path)
        if user_name:
            return user_name.text.encode('UTF-8')
        else:
            return None


    def getCardId(self):
        '''获取身份证号码'''
        METHOD = By.XPATH, ".//*[@id='id-card']/div[2]/table/tbody/tr[3]/td[2]"

        userid = self.findElemenAcctLocated(*METHOD)
        if userid:
            return userid.text.encode('UTF-8')
        else:
            return None


    def __getImag(self):
        '''获取身份证图片'''
        for index in xrange(1, 3):
            METHOD = By.XPATH, ".//*[@id='id-card']/div[2]/table/tbody/tr[1]/td[2]/img[" + str(index) + "]"
            img = self.findElemenAcctLocated(*METHOD)
            if img:
                ActionChains(self.driver).move_to_element(img).context_click(img).perform()
                self.wait()
                win32api.keybd_event(86, 0, 0, 0)
                win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
                self.jpg_save_as(index)
            else:
                pass
            self.wait()

    def find_2secrity(self):
        '''二次验证'''
        METHOD = By.XPATH, ".//*[@id='list-sold-items']/div[@class='aq_def_overlay']/div[2]/iframe"
        valid2 = self.findElement(*METHOD)
        if valid2 and valid2.is_displayed():
            self.driver.switch_to_frame(valid2)
            METHOD2 = By.XPATH, ".//form[@id='J_Question']/ul/li[2]/span/input"
            input_info = self.findElement(*METHOD2)
            if input_info and input_info.is_displayed():
                input_info.clear()
                input_info.send_keys(unicode(self.problem, 'utf-8'))
                METHOD3 = By.ID, "J_FooterSubmitBtn"
                submit = self.findElement(*METHOD3)
                if submit and submit.is_displayed():
                    submit.click()
                    self.driver.switch_to.default_content()
                else:
                    pass
            else:
                pass
        else:
            pass


