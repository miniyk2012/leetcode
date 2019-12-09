import time
def f1():
    res=1
    for i in range(10000000):
        res+=i

def f2():
    res=1
    for i in range(10000000):
        res*=i

start=time.time()
f1()
f2()
stop=time.time()
print('run time is %s' %(stop-start)) #10.985628366470337