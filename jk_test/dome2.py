import requests
import re

url = 'http://dev.echronos.com:10460'

url = url
url = f'{url}/accounts/login?next=/&query='
# hd = 'Accept: application/json,Cookie: csrftoken=BItL6qDc4ryTUKxlDznyMO0gmn7SxUdiOSovyVytGGbg6LdjbXNQcrFb7lHxsH5H; sessionid=5mtywgkpcut4mfqn97ct7pxtx5sjirbl'
jg = requests.get(url=url)
# print(jg.text)
head = jg.headers
print(head)

csrfroken=re.search(r"'Set-Cookie': 'csrftoken=(.*); expires",str(head)).group(1)
print(csrfroken)
s = jg.text
token = re.search(r"var token = '(.*)';",s).group(1)

# print(token)

user = ['15179745797']
body={'username': user, 'password': '111111', 'is_auto': 'false',
        'csrfmiddlewaretoken': token}
header = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':'csrftoken={}'.format(csrfroken)}

url = f'{url}/accounts/login'
dr = requests.post(url=url,data=body,headers=header)

# login = dr.status_code
login = dr.text
print(login)