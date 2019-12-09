# 协程在爬虫上的应用
from gevent import monkey

monkey.patch_all()

import gevent
import requests
import time


def get_page(url):
    print('GET: %s' % url)
    response = requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' % (len(response.text), url))


start_time = time.time()
gevent.joinall([
    gevent.spawn(get_page, 'https://www.python.org/'),
    gevent.spawn(get_page, 'https://www.yahoo.com/'),
    gevent.spawn(get_page, 'https://github.com/'),
])
stop_time = time.time()
print('协程并行时间 %s' % (stop_time - start_time))

print('--------------------------------')
s = time.time()
get_page('https://www.python.org/')
get_page('https://www.yahoo.com/')
get_page('https://github.com/')
t = time.time()
print('串行时间>>', t - s)  # run time is 2.5960400104522705
