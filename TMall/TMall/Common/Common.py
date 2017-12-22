#!D:\Python\python27
# -*- coding:utf-8 -*-
import ConfigParser
import logging
import logging.config
import os
import re
from   time import sleep
import time
from ReqHttp import *


class Comon(object):
    def read_cfg(self, module):
        '''
        读取配置文件
        :param cfg_path 配置文件地址
        :param module  读取的文件节点
        '''
        cfg_path = self.filePath('Config\\shop_cfg.ini')
        config = ConfigParser.ConfigParser()
        config.read(cfg_path)
        return dict(config.items(module))

    def fillLog(self):
        '''记录日志信息'''
        LOGPATH = self.filePath('Config\\logger.ini')
        logging.config.fileConfig(LOGPATH)
        logger = logging.getLogger("epet")
        return logger


    def filePath(self, direct):
        '''
        获取文件的位置
        :param direct 文件相对路径
        '''
        BASE_DIR = "D:\\PyCharm404\\__py\\TMall\\"
        FILE_PATH = \
            (
                os.path.join(BASE_DIR, direct),
            )
        path = '/'.join(FILE_PATH)
        return path


    def get_shop_cfg(self, shopname):
        '''
        获取登录账户的配置信息
        :param shop 店铺名称
        '''
        shopupper = re.findall("[a-zA-Z]+", shopname)[0]
        return self.read_cfg(shopupper.upper())

    @property
    def get_url_cfg(self):
        '''获取链接地址的'''
        return self.read_cfg('URLPATH')

    def send_ding(self, shopname, *params):
        '''
        发送叮叮消息
        :param params 发送的叮叮信息
        '''
        ding_params = {}
        ##叮叮地址
        URL = self.get_url_cfg['ding_url']
        ding_params["url"] = URL
        ##提醒信息
        shop_info = self.get_shop_cfg(shopname)
        msg = shop_info['remind'] % params
        ding_params["msg"] = msg
        ##发送人群
        user = shop_info['touser']
        ding_params["user"] = user
        ##当前店铺是否有活动
        active = int(shop_info["active"])
        ###当前时间
        crt_time = int(time.strftime('%H', time.localtime(time.time())))
        ##开始发送叮叮信息
        if active == 1:
            msg2=load_http(**ding_params).getMsg()
            self.fillLog().debug(msg2["msg"].encode('utf-8'))
            return True
        elif crt_time >= 6 and crt_time <= 23:
            load_http(**ding_params).getMsg()
            return True
        else:
            return False

    def save_idcard(self, **params):
        '''
        保存身份证图片
        :param params 个人身份信息
        '''
        ##身份证保存目录
        img_path = self.filePath('Files\\SaveImg\\')
        ##订单来源
        fromto = params["from"]
        ##订单号
        order = params["tid"]
        ##真实姓名
        real_name = params["realname"]
        ##身份证号码
        id_card = params["id_card"]
        ##身份证正反两面
        names = ['face.jpg', 'back.jpg']
        for name in names:
            if os.path.exists(img_path + name):
                face_name = img_path + real_name + "_" + id_card + "_" + order + "_" + fromto + "_" + name
                if os.path.exists(face_name):
                    os.remove(face_name)
                else:
                    pass
                os.rename(img_path + name, face_name)
            else:
                pass

    def get_epetunsync_interface(self, shopname):
        '''
        获取易宠ERP后台未同步的订单
        :param shopname 店铺名称
        '''
        shop_info = self.get_shop_cfg(shopname)
        shop_info.pop('username')
        shop_info.pop('remind')
        shop_info.pop('touser')
        shop_info.pop('valid')
        url_list = ['petmall.hk', 'epet.com']
        params = {}
        for server in url_list:
            url = 'http://api.' + server + '/zhe800/oauth.html'
            shop_info["url"] = url
            req_order = self.__request(**shop_info)
            if req_order:
                if server == 'petmall.hk':
                    params["hk"] = req_order
                else:
                    params["epet"] = req_order
            else:
                pass
            sleep(2)
        else:
            return params


    def __request(self, **params):
        '''请求订单地址'''
        response = load_http(**params).getMsg()
        if response:
            if response["code"] == 'succeed' and response["orders"]:
                return response["orders"]
            else:
                return None
        else:
            return None


    def jpg_save_as(self, index):
        '''
        身份证正反两面另存为
        :param index 图片当前位置
        '''
        base_path = self.filePath("Config\\")
        os.chdir(base_path)
        if index == 1:
            os.system("face.au3")
        elif index == 2:
            os.system("back.au3")
        else:
            pass


