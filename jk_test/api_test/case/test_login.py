import requests
import re
import unittest
import time
from jk_test.api_test.po.login_sj import Test_01


class Testjk(unittest.TestCase):
        def test_01_zhuce(self):#注册
                
                case_login = Test_01(url='http://xcxlm.huacaigou.com',user='15179745785')                
                case_login.test_zhucesetmm()
                
        def test_02_login(self):#登入
                case_login = Test_01()                
                case_login.test_login()

             
if __name__ == "__main__":
        unittest.main()
