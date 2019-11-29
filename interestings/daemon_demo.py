import os
import random
import threading
import time
from _signal import SIGKILL
from multiprocessing import Process

thread_or_process = Process


def is_process_alive(pid):
    try:
        os.kill(pid, 0)
    except OSError as e:
        if e.errno == 3:  # process is dead
            return False
        elif e.errno == 1:  # no permission
            return True
        else:
            raise
    else:
        return True

def child():
    print('child')
    time.sleep(5)
    with open('current_file.txt', 'w') as f:
        f.write(str(random.randint(0, 100)))


def parent():
    print('parent')
    b = thread_or_process(target=child)
    b.daemon = True
    b.start()
    time.sleep(2)
    print('end')


a = thread_or_process(target=parent)
a.start()
time.sleep(1)
print(is_process_alive(a.pid))
os.kill(a.pid, SIGKILL)
a.join()
print(is_process_alive(a.pid))


print('terminate parent')
