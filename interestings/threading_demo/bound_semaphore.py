import threading
import time

# 创建有界信号量，最大值为5，最小值为0
#bounded_sem = threading.BoundedSemaphore(value=5)
bounded_sem = threading.Semaphore(value=5) # 这里没有区别


def run(n):
   bounded_sem.acquire()  #信号量获取一把锁, 最多5个线程同时运行
   time.sleep(1)
   print("run the thread: %s\n" % n)
   bounded_sem.release()
   


if __name__ == '__main__':
    num = 0
    for i in range(20):
      t = threading.Thread(target=run, args=(i,))
      t.start()
    while threading.active_count() != 1:
       pass  # print threading.active_count()
    else:
       print('----all threads done---')
       print(num)
