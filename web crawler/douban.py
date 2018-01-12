#!D:\Python\python27
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium.webdriver.common.action_chains import ActionChains
browser= webdriver.Firefox()

browser.get('https://www.douban.com/')
# time.sleep(6)
#
# browser.find_element_by_id('form_email').send_keys('867745834@qq.com')
# browser.find_element_by_id('form_password').send_keys('qazwsx@12345')
# browser.find_element_by_class_name('bn-submit').click()
# #获得元素属性值
# attribute = browser.find_element_by_class_name('bn-submit').get_attribute('type')
# print attribute
# browser.quit()
# browser.refresh()
# browser.quit()

# browser.get('https://www.baidu.com')
#
# print browser.title
# print browser.current_url
#这里,10是要等待的秒数.如果没有满足until()方法中的条件,就会始终在这里wait 15秒,依然找不到,就抛出异常
# element = WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_id('kw'))
# element.send_keys('selenium')
#
# browser.implicitly_wait(30)

#find_elements找出一组元素
# driver = webdriver.Firefox()
# file_path = 'file:///' + os.path.abspath('checkbox.html')
# driver.get(file_path)
# # 选择页面上所有的 tag name 为 input 的元素
# inputs = driver.find_elements_by_tag_name('input')
# #然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()
# # driver.quit()

#层级定位
# driver = webdriver.Firefox()
# file_path = 'file:///' + os.path.abspath('level_locate.html')
# driver.get(file_path)
# #点击 Link1 链接（弹出下拉列表）
# driver.find_element_by_link_text('Link1').click()
# #在父亲元件下找到 link 为 Action 的子元素
# menu =driver.find_element_by_id('dropdown1').find_element_by_link_text('Anotheraction')
# #鼠标移动到子元素上
# ActionChains(driver).move_to_element(menu).perform()
# time.sleep(5)
# driver.quit()

#frame 定位
# driver = webdriver.Firefox()
# file_path = 'file:///' + os.path.abspath('frame.html')
# driver.get(file_path)
# driver.implicitly_wait(30)
# #先找到到 ifrome1（id = f1）
# driver.switch_to_frame("f1")
# #再找到其下面的 ifrome2(id =f2)
# driver.switch_to_frame("f2")
# #下面就可以正常的操作元素了
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()

#多窗口处理
# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com/")
# #获得当前窗口
# nowhandle=driver.current_window_handle
# #打开注册新窗口
# driver.find_element_by_id('kw').send_keys('22')
# driver.find_element_by_link_text('登录').click()

# driver.find_element_by_partial_link_text('立即注册').click()
# driver.find_element_by_link_text('立即注册').click()
# #获得所有窗口
# allhandles=driver.window_handles
# #循环判断窗口是否为当前窗口
# for handle in allhandles:
#     if handle != nowhandle:
#         driver.switch_to_window(handle)
#         print 'now register window!'
# #切换到邮箱注册标签
#         driver.find_element_by_tag_name("-blank").click()
#         time.sleep(5)
#         driver.close()
# #回到原先的窗口
# driver.switch_to_window(nowhandle)
# driver.find_element_by_id("kw").send_keys(u"搜索成功！")
# time.sleep(3)
# driver.quit()

#cookie
cookie= browser.get_cookies()
print cookie
# time_local= time.localtime(1547274463)
# dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
# print dt
# browser.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})
# for cookie in browser.get_cookies():
#     print "%s -> %s" % (cookie['name'], cookie['value'])
# # 删除一个特定的 cookie
# browser.delete_cookie("key-aaaaaaa")

#验证码问题
# browser.add_cookie({
# 'name':'bid','value': 't1uu_td7Wpk',
# 'name':'ll','value': '"108309"',
# 'name':'ps','value': 'y',
# 'name':'__yadk_uid','value': 'Sscr1VI75dnCbnymiRBm37tkx72MZO6D',
# 'name':'ap','value': '1',
# 'name':'_pk_ref.100001.8cb4','value': '%5B%22%22%2C%22%22%2C1515739540%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DG8n_3COq00JOUaxo8F32PbVJeI88TOdtssrDDqex3tzPNYpa7oI9MfcG8yzLm_x0%26wd%3D%26eqid%3Dd6e8368600013440000000055a585995%22%5D',
# 'name':'__utmb','value': '30149280.5.10.1515739546',
# 'name':'__utmc','value': '30149280',
# 'name':'__utmt','value': '1',
# 'name':'ck','value': 'KiMY',
# 'name':'_pk_id.100001.8cb4','value': 'ce0484b0ce2cd826.1512633890.4.1515739574.1515656628.',
# 'name':'_pk_ses.100001.8cb4','value': '*',
# 'name':'push_noty_num','value': '0',
# 'name':'push_doumail_num','value': '0',
# 'name':'__utma','value': '30149280.1417552922.1512633895.1515654908.1515739546.4',
# 'name':'__utmz','value': '30149280.1515739546.4.4.utmcsr','value': 'baidu|utmccn','value': '(organic)|utmcmd','value': 'organic',
# 'name':'__utmv','value': '30149280.17242',
#
# })
#
# browser.get('https://www.douban.com/')
# time.sleep(3)
# browser.quit()