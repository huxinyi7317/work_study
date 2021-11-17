import requests


# class WeiShop:
#     def __init__(self):
#         self.header={"Authorization":f"Bearer {token}",
#                         "shopid":shopid}
def request_init(url,type,header,data=[],json={}):
    # 请求公共
    if type == "get":
        rep = requests.get(url=url,headers=header,data=data)
    else:
        rep = requests.post(url=url,headers=header,json=json)
    return rep.content.decode("utf-8")

def add_shop_good(url,header,json,type="post"):
    #添加商品
    jg = request_init(url=url,header=header,type=type,json=json)
    print('返回结果：\n'+f'{jg}')
token = r"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.\
    eyJ1c2VyIjoxLCJleHRyYSI6W10sImFwcCI6Im1hbmFnZXIiLCJhdWQiOiIiLCJleHAiOjE2MTg5OTMyODAsImlhdCI6MTYxODkwNjg4MCwiaXNzIjoiIiwianRpIjoiYTFmMzg5NGFkM2I3OGIwYzVjMDUzZmQ0OGMxM2NiMTYiLCJuYmYiOjE2MTg5MDY4ODAsInN1YiI6IiJ9.9C2nzFSLFCamyarxovP6x9Rx_TIuwXWnOIX0fNZ7r5k"
shopid = "1"
header = {
    "Authorization":"Bearer {}".format(token),
    "shopid":shopid,
    "from":"shop-h5",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoxLCJleHRyYSI6W10sImFwcCI6Im1hbmFnZXIiLCJhdWQiOiIiLCJleHAiOjE2MTg5OTMyODAsImlhdCI6MTYxODkwNjg4MCwiaXNzIjoiIiwianRpIjoiYTFmMzg5NGFkM2I3OGIwYzVjMDUzZmQ0OGMxM2NiMTYiLCJuYmYiOjE2MTg5MDY4ODAsInN1YiI6IiJ9.9C2nzFSLFCamyarxovP6x9Rx_TIuwXWnOIX0fNZ7r5k",
    "Host": "api.weitshop.cn"
}
id = 1
json = {
    "goods_type":1,
    "title":"测试商品{}".format(id),
    "vice_title":"脚本添加测试商品",
    "main_picture":"https://test-1254212114.cos.ap-nanjing.myqcloud.com/uploads/shop/id_1/group_1/202104/7214_wallhaven-4856m1.jpg","video":"","video_cover":"","slideshow":["https://test-1254212114.cos.ap-nanjing.myqcloud.com/uploads/shop/id_1/group_11/202104/6626_wallhaven-4856m1.jpg"],
    "classId":[],
    "marketing_tab":[],
    "serviceId":[],
    "cart_type":1,
    "groupId":[],
    "tabId":[],
    "norms_type":0,
    "price":"1.00",#价格
    "original_price":"100",#划线价格
    "cost_price":"",
    "stock":"100",
    "stock_warning":"",
    "stock_set":1,
    "stock_show":1,
    "sales_show":1,
    "virtual_sales":"",
    "postage":2,
    "express_fee":1,
    "express_site":10,
    "freight":"",
    "expressage":1,
    "weight":"",
    "volume":"",
    "goods_code":"",
    "bar_code":"",
    "timing_sold_out":1,
    "timing_sold_out_time":"",
    "goods_state":2,
    "goods_state_time":"",
    "type":[],
    "start_purchase_limit":1,
    "browseauthId":"",
    "buyauthId":"",
    "member_equities":[],
    "relevance_goods_id":"",
    "goods_detail":"",
    "goods_param_type":"5",
    "goods_param":"","spec":[],"options":[]}
url = r"http://test001.weitshop.cn/shop/Goods/addEdit"
i = 0
while i < 100:
    add_shop_good(url=url,header=header,json=json)
    i +=1
    id +=1
print("已添加商品数量{}".format(i))