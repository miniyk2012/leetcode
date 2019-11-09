import itertools


def generator():
    for i in range(1010000):
        yield i


g = generator()
g_1, g_2 = itertools.tee(g, 2)

import threading


def print_sum(x, desc=''):
    if desc != '':
        import time
        time.sleep(2)
    print(desc, sum(x))


# print_sum(g_1)
# print_sum(g_2)


for x in g_1, g_2:
    t = threading.Thread(target=print_sum, args=(x, 'x'), )
    # t.setDaemon(True)
    t.start()

print('-' * 100)

g1 = generator()

g2 = generator()
for x in g1, g2:
    threading.Thread(target=print_sum, args=(x,)).start()
