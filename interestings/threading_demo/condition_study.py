import threading
from threading import Condition
import time
import random

class Producer(threading.Thread):
    
    def __init__(self, condition, numbers):
        self.condition = condition
        self.numbers = numbers
        super(Producer, self).__init__()

    def run(self):
        while True:
            with self.condition:
                i = random.randint(0, 100)
                self.numbers.append(i)
                print(f'produce {i}')
                i += 1
                self.condition.notify_all()
            time.sleep(1)        

class Consumer(threading.Thread):

    def __init__(self, indent, condition, numbers):
        self.indent = indent
        self.condition = condition
        self.numbers = numbers
        super(Consumer, self).__init__() 

    def run(self):
        while True:
            with self.condition:
                if not self.numbers:
                    self.condition.wait()
                else:
                    num = self.numbers.pop(0)
                    print(f'threading {self.indent} consume {num}')


def main():
    condition = Condition()
    numbers = []
    producer = Producer(condition, numbers)
    consumer1 = Consumer(1, condition, numbers)
    consumer2 = Consumer(2, condition, numbers)
    producer.start()
    consumer1.start()
    consumer2.start()


if __name__ == '__main__':
    main()





