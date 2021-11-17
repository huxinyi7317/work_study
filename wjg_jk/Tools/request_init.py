import requests


def request_init(url,type,header,data=[],json={}):
    # 请求公共
    if type == "get":
        rep = requests.get(url=url,headers=header,data=data)
    else:
        rep = requests.post(url=url,headers=header,json=json)
    return rep.content.decode("utf-8")

