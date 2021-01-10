import requests
import re
import unittest



class Test_01:
    '''
        测试数据
    '''
    def __init__(self,url='http://dev.echronos.com:10460',user='15179745784'):
        self.url =url
        self.user = user
    def logintoken(self,users=False):#获取登入验证码
        url = self.url
        url = f'{url}/accounts/login?next=/&query='
        # hd = 'Accept: application/json,Cookie: csrftoken=BItL6qDc4ryTUKxlDznyMO0gmn7SxUdiOSovyVytGGbg6LdjbXNQcrFb7lHxsH5H; sessionid=5mtywgkpcut4mfqn97ct7pxtx5sjirbl'
        jg = requests.get(url=url)
        # print(jg.text)
        head = jg.headers
        self.csrfroken=re.search(r"'Set-Cookie': 'csrftoken=(.*); expires",str(head)).group(1)
        # print(self.csrfroken)
        s = jg.text
        self.token = re.search(r"var token = '(.*)';",s).group(1)
    def test_zhuce(self):#注册页面码
        url = self.url
        user = self.user
        self.logintoken()                
        body=f'phone={user}&code=111111'
        header = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':'csrftoken={}'.format(self.csrfroken)}

        url = f'{url}/channel/im/check/code/'
        dr = requests.post(url=url,data=body,headers=header)

        # login = dr.status_code
        json_text = dr.json()   #返回响应内容
        return json_text
 
    def test_zhucesetmm(self):#注册设置密码
        url = self.url
        user = self.user
        self.logintoken()
        body=f'phone={user}&code=111111&password=111111&confirmPassword=111111&agreeToDeal=true&password1=111111'
        header = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':'csrftoken={}'.format(self.csrfroken)}

        url = f'{url}/channel/im/app_user_register/'
        dr = requests.post(url=url,data=body,headers=header)

        # login = dr.status_code
        json_text = dr.json()#注册响应体
        # print(json_text)

        assert json_text['msg'] == 'ok'
        return json_text
    def test_login(self):#登入
        url = self.url
        self.logintoken()
        user = self.user
        body={'username': user, 'password': '111111', 'is_auto': 'false',
                'csrfmiddlewaretoken': self.token}
        header = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':'csrftoken={}'.format(self.csrfroken)}

        url = f'{url}/accounts/login'
        dr = requests.post(url=url,data=body,headers=header)

        # login = dr.status_code
        json_text = dr.json()
        # print(json_text)
        assert json_text['msg'] == 'ok'
        # print(dr.headers)
        # drherder = dr.headers
        return json_text

if __name__ == "__main__":
    f = open('账号文件.txt','r',encoding='utf-8')
    user = f.readline()
    while True:
        if not user:
            break
        case = Test_01(user=user)
        case.test_zhucesetmm()
        case.test_login()
    f.close()
    # t = Test_01()
    # t.test_zhucesetmm()
    # t.test_login()