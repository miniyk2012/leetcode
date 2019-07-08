import requests

import locale
locale.setlocale(locale.LC_ALL, 'C')
import tesserocr

from PIL import Image
session = requests.session()

headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
            }
url = 'http://my.cnki.net/Register/CheckCode.aspx'
	# 登录的网址。

	# 登录的参数。
login = session.get(url, headers=headers)
code = login.status_code
print(login)

x=login.content
file = open('cap.jpg', "wb")
file.write(x)
file.close()
im = Image.open('cap.jpg')

im=im.convert('L')
threshold=140
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
im=im.point(table,'1')
im.show()


result=tesserocr.image_to_text(im)
print(result)
input()
