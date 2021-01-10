'''import urllib.request

rep = urllib.request.urlopen('http://www.fishC.com')
html = rep.read()
html.decode('utf-8')

print(html)
'''

import requests

for i in range(400,2000,100):
    for n in range(400,2000,100):

        reposes = requests.get('http://placekitten.com/g/%d/%d'%(i,n))
        print('我运行了')
        a = reposes.content
        with open('./cat%d_%d.jpg'%(i,n),'wb') as f:
            f.write(a)







# print(reposes.apparent_encoding)
# jg = reposes.text
# dy = jg.encode('utf-8')
# print(dy)