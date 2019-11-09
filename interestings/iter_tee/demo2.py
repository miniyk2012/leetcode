def generator():
    for i in range(101000):
        yield i


def split(g):
    value_list_1 = []
    value_list_2 = []

    def wrap(queue):
        while True:
            if not queue:
                try:
                    value = next(g)
                except StopIteration:
                    return
                value_list_1.append(value)
                value_list_2.append(value)
            # print('len(value_list_1)={}'.format(len(value_list_1)))
            # print('len(value_list_2)={}'.format(len(value_list_2)))
            yield queue.pop(0)

    g_1 = wrap(value_list_1)
    g_2 = wrap(value_list_2)
    return g_1, g_2


g = generator()
g_1, g_2 = split(g)

import threading


def print_sum(x):
    print(sum(x))

# print_sum(g_1)
# print_sum(g_2)

for x in g_1, g_2:
    threading.Thread(target=print_sum, args=(x,)).start()
