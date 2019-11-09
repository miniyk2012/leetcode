def generator():
    for i in range(10):
        yield f'我是你第{i}个爷爷'


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
            print('len(value_list_1)={}'.format(len(value_list_1)))
            print('len(value_list_2)={}'.format(len(value_list_2)))
            yield queue.pop(0)

    g_1 = wrap(value_list_1)
    g_2 = wrap(value_list_2)
    return g_1, g_2


g = generator()
g_1, g_2 = split(g)

# for v in g_1:
#     print(v)
#
# for v in g_2:
#     print(v)

print('-' * 100)

while True:
    try:
        value1 = next(g_1)
        print(value1)
        value2 = next(g_2)
        print(value2)
    except StopIteration:
        break

