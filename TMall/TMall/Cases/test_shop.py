#!D:\Python\python27
# -*- coding:utf-8 -*-
import sys

from TMall.Main.Setup_TearDown import BasePage
from TMall.Pages.GoodListPages import *

reload(sys)
sys.setdefaultencoding('utf-8')


class testShop(BasePage):
    '''爬去天猫后台信息'''

    @property
    def get_shop(self):
        return 'naturalbalance海外旗舰店'

    def testShop(self):
        self.driver.get("https://trade.taobao.com/trade/itemlist/list_sold_items.htm")
        current_shop = GoodList(driver=self.driver, shopname=self.get_shop)
        success = current_shop.findQR()
        if success:
            flag = False
            while True:
                orders = current_shop.get_epetunsync_interface(shopname=self.get_shop)
                if orders:
                    current = int(time.time())
                    new_orders = []
                    if orders.has_key("hk"):
                        new_orders.extend(orders["hk"])
                    else:
                        pass
                    if orders.has_key("epet"):
                        new_orders.extend(orders["epet"])
                    else:
                        pass
                    for order in new_orders:
                        current_shop.input_order(order)
                        search = current_shop.searchButton()
                        if search:
                            if order in orders["hk"]:
                                current_shop.qingguan_mess('hk')
                            else:
                                current_shop.qingguan_mess('epet')
                            end = int(time.time()) - current
                            if end >= 180:
                                current = int(time.time())
                                self.driver.refresh()
                            else:
                                pass
                        else:
                            flag = True
                            break
                    if flag == True:
                        self.tearDown()
                        break
                    else:
                        pass
                else:
                    sleep(5)
        else:
            self.tearDown()








