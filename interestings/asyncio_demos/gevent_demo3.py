import threading

import gevent
import time

from gevent import monkey

monkey.patch_all()

def eat(name):
    print(threading.current_thread().getName())
    print('%s eat 1' % name)
    time.sleep(2)
    print('%s eat 2' % name)

def play(name):
    print(threading.current_thread().getName())
    print('%s play 1' % name)
    time.sleep(1)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, name='egon')
start=time.time()
g1.join()
g2.join()
stop=time.time()
print('run time is %s' %(stop-start))
# 或者gevent.joinall([g1,g2])
print('主')