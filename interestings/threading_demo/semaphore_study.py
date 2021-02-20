import random
import threading
import time

# 创建信号量，初始个数为0
semaphore = threading.Semaphore(0)

# 消费者
def consumer():
    # 信号量计数器减1
    semaphore.acquire()
    print(f'conumser:number is {number}')

def producer():
    global number
    time.sleep(1)
    number = random.randint(0, 100)
    print(f'producer:number is {number}')
    # 信号量计数器加1
    semaphore.release()

if __name__ == '__main__':
    c = threading.Thread(target=consumer)
    p = threading.Thread(target=producer)
    c.start()
    p.start()
    print('Done')
