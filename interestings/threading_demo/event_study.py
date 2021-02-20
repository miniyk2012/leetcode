import threading
import random
import time

class Producer(threading.Thread):
    def __init__(self, numbers, event):
        super(Producer, self).__init__()
        self.numbers = numbers
        self.event = event

    def run(self):
        while True:
            number = random.randint(0, 100)
            self.numbers.append(number)
            print(f'Producer add {number} in numbers')
            self.event.set() # 设置事件标志为true，激活其他线程
            time.sleep(1) # 模拟耗时操作


class Consumer(threading.Thread):
    def __init__(self, numbers, event):
        super(Consumer, self).__init__()
        self.numbers = numbers
        self.event = event

    def run(self):
        while True:
            self.event.wait() # 阻塞线程
            while self.numbers: 
                number = self.numbers.pop() # 获取数字
                print(f'Consumer pop {number} in numbers')
            self.event.clear() # 设置事件标志为false

def main():
    numbers = []
    event = threading.Event() # 实例化事件对象
    producer = Producer(numbers, event)
    consumer = Consumer(numbers, event)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('Done')

if __name__ == '__main__':
    main()
