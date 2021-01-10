import requests
import re

url = 'http://192.168.188.14:10157/accounts/login'
hd = 'Accept: application/json,Cookie: csrftoken=BItL6qDc4ryTUKxlDznyMO0gmn7SxUdiOSovyVytGGbg6LdjbXNQcrFb7lHxsH5H; sessionid=5mtywgkpcut4mfqn97ct7pxtx5sjirbl'
jg = requests.get(url=url)
t = jg.text
# print(t)
# print(jg.text)
# s = jg.json()
# print(t)
# print(type(t))
str1 = "小明 18 男性"
# 18 -> 22
# + *
shaixuan = re.sub(r'(\d+)','22',str1)
print(shaixuan)