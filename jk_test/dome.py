import requests
import re

class test_case():

        def logintoken(self,url):#获取登入验证码
                url = url
                url = f'{url}/accounts/login?next=/&query='
                # hd = 'Accept: application/json,Cookie: csrftoken=BItL6qDc4ryTUKxlDznyMO0gmn7SxUdiOSovyVytGGbg6LdjbXNQcrFb7lHxsH5H; sessionid=5mtywgkpcut4mfqn97ct7pxtx5sjirbl'
                jg = requests.get(url=url)
                # print(jg.text)
                head = jg.headers
                self.csrfroken=re.search(r"'Set-Cookie': 'csrftoken=(.*); expires",str(head)).group(1)
                # print(self.csrfroken)
                s = jg.text
                self.token = re.search(r"var token = '(.*)';",s).group(1)

                # print(token)
        def zhuce(self,url,user):#注册
                self.logintoken(url=url)
                
                body=f'phone={user}&code=111111'
                header = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':'csrftoken={}'.format(self.csrfroken)}

                url = f'{url}/channel/im/check/code/'
                dr = requests.post(url=url,data=body,headers=header)

                # login = dr.status_code
                login = dr.json()
                assert login['msg'] == 'ok'
                print('验证通过')
 
        def zhucesetmm(self,url,user):#注册设置密码
                self.logintoken(url=url)
                
                body=f'phone={user}&code=111111&password=111111&confirmPassword=111111&agreeToDeal=true&password1=111111'
                header = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':'csrftoken={}'.format(self.csrfroken)}

                url = f'{url}/channel/im/app_user_register/'
                dr = requests.post(url=url,data=body,headers=header)

                # login = dr.status_code
                login = dr.json()
                assert login['msg'] == 'ok'
                print('注册成功')
 
        def login(self,url，user):#登入
                self.logintoken(url=url)
                user = ['15179745797']
                body={'username': user, 'password': '111111', 'is_auto': 'false',
                        'csrfmiddlewaretoken': self.token}
                header = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':'csrftoken={}'.format(self.csrfroken)}

                url = f'{url}/accounts/login'
                dr = requests.post(url=url,data=body,headers=header)

                # login = dr.status_code
                login = dr.json()
                assert login['msg'] == 'ok'
                print('登入成功')
                print(dr.headers)
                # drherder = dr.headers
                
                


url = 'http://dev.echronos.com:10460'

url1 = 'http://dev.echronos.com:10504'#注册码
url2 = 'http://dev.echronos.com:10504'#注册
if __name__ == "__main__":
        pass
#     test_case().login(url=url)#登入
#       test_case().zhuce(url=url)
#       test_case().zhucesetmm(url=url)

