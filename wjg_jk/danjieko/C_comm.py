import requests
from requests.api import request
import json
import re

class WeiShop:
    def __init__(self,token):
        self.header = {
            "Authorization": "Bearer {}".format(token),
            "shopid": "7",
            "from": "shop-h5",
        }


    def request_init(self, url, type, header, data=[], json={}):
        # 请求公共
        if type == "get":
            rep = requests.get(url=url, headers=header, data=data)
        else:
            rep = requests.post(url=url, headers=header, json=json)
        return rep

class Weitshop(WeiShop):
    def __init__(self):
        self.ip = 'http://dlshop.weitshop.cn/index.php'
    def user_login(self, json,header, type='post',url="/shop/Auth/login"):
        # C端账号密码登录接口
        url = self.ip+url
        session = requests.session()
        jg = session.post(url=url, headers=header, json=json).text
        return jg
    def add_shop_good(self, header, json, type="post", url="/shop/Goods/addEdit"):
        # 添加商品
        url = self.ip+url
        jg = self.request_init(url=url, header=header,
                               type=type, json=json).json()
        # print('返回结果：\n'+f'{jg}')
        return jg

    def goods_list(self,header,json,type='post',url='/shop/appGoods/list'):
        # 获取商品列表
        url=self.ip+url
        jg = self.request_init(url=url, header=header,
                               type=type, json=json).json()
        print('返回结果：\n'+f'{jg}')
        return jg
    def addre_add(self,header,json,type='post',url='/shop/AppUser/AddressAddEdit'):
        # 添加收货地址
        url=self.ip+url
        jg = self.request_init(url=url, header=header,
                               type=type, json=json).json()
        # print('返回结果：\n'+f'{jg}')
        return jg
    def get_shop_particular(self,header,json,type='post',url='/shop/appGoods/list'):
        # 获取商品详细
        url=self.ip+url
        jg = self.request_init(url=url, header=header,
                               type=type, json=json).json()
        # print('返回结果：\n'+f'{jg}')
        return jg


if __name__ == "__main__":
    a = Weitshop()
    b = WeiShop(token=None)
    json = {"mobile": "test123", "password": "test123"}
    jg = a.user_login(json=json,header=b.header)
    # print(jg)
    itme = re.search(r'"token":"(.*?)"',jg).group(1)
    # print(itme)
    token = itme
    itme = WeiShop(token=token)
    heades = itme.header
    a.goods_list(header=heades,json=None)
