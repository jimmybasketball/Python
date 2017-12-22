#!D:\Python27
# encoding=utf-8
from Common import *


class sysnc_Img(Comon):
    def __init__(self):
        self.base_path = self.filePath('Files\\SaveImg\\')
        self.patthon = u'(.*)_(.*)_(.*)_(.*)_(.*).jpg'

    def sync_file(self):
        '''同步目录下的文件'''
        try:
            for dirpath, dirnames, filenames in os.walk(self.base_path):
                for name in filenames:
                    params = {}
                    filename = name.decode('gbk').encode('UTF-8')
                    allGroup = re.search(self.patthon, filename)
                    if allGroup:
                        ##真实姓名
                        realName = allGroup.group(1)
                        params["realname"] = realName
                        ##身份证号码
                        idCard = allGroup.group(2)
                        params["id_card"] = idCard
                        ##订单号
                        order = allGroup.group(3)
                        params["tid"] = order
                        ##订单号
                        fromto = allGroup.group(4)
                        params["from"] = fromto
                        ###订单的正面或者反面
                        side = allGroup.group(5)
                        params["side"] = side
                        ##图片地址
                        params["path"] = dirpath + name
                        ##开始请求接口
                        if fromto == 'hk':
                            params["url"] = 'http://api.petmall.hk/tmallIntl/Idcard.html?do=imgUpload'
                        else:
                            params["url"] = 'http://api.epet.com/tmallIntl/Idcard.html?do=imgUpload'
                        response = load_http(**params).getMsg()
                        if response:
                            rep_msg = response["msg"].encode('utf-8')
                            mian_msg = '来自 ' + fromto + ' 的订单' + order + ">>> " + realName + "身份证"
                            if side == 'back':
                                side_msg = '反面'
                            else:
                                side_msg = "正面"
                            self.fillLog().debug(mian_msg + side_msg + rep_msg)
                            if response["error_code"] == '100':
                                os.remove(params["path"])
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
        except:
            pass






