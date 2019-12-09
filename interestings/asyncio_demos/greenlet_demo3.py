# 切换
from greenlet import greenlet
import time
def f1():
    res=1
    for i in range(10000000):
        res+=i
        g2.switch()

def f2():
    res=1
    for i in range(10000000):
        res*=i
        g1.switch()

start=time.time()
g1=greenlet(f1)
g2=greenlet(f2)
g1.switch()
stop=time.time()
print('run time is %s' %(stop-start)) # 52.763017892837524