import time

from gevent import spawn, joinall, monkey

monkey.patch_all()


def task(pid):
    """
    Some non-deterministic task
    """
    time.sleep(0.5)
    print('Task %s done' % pid)

def synchronous():
    for i in range(10):
        task(i)

def asynchronous():
    g_l = [spawn(task, i) for i in range(10)]
    joinall(g_l)

if __name__ == '__main__':
    print('Synchronous:')
    synchronous()

    print('Asynchronous:')
    asynchronous()