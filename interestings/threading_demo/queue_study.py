from queue import Queue
from threading import Thread
import time
import random


# 生产者
class producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(10):
            number = random.randint(0, 100)
            self.queue.put(number) # 将数据存入队列
            print(f'producer add {number} to queue')

# 消费者
class consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            number = self.queue.get() # 获取队列中的数据
            print(f'consumer get {number} from queue')
            self.queue.task_done() # 发送任务完成信息
            time.sleep(1) # 耗时操作

