def my_coroutine():
    while True:
        received = yield 3
        print('Received', received)


# it = my_coroutine()
# val = it.send(None)
# print('Send return', val)
#
# val = it.send(5)
# print('Send return', val)
#
# print()

def delegated():
    a = yield 1
    print(a)
    b = yield 2
    print(b)
    return 'c'


def composed():
    yield 'A'
    it = delegated()
    x = yield next(it)
    while True:
        try:
            yield it.send(x)
        except StopIteration as e:
            print(e.value)
            break
    yield 'B'


it = composed()
print(next(it))
while True:
    try:
        b = it.send('x')
        print(b)
    except StopIteration:
        break
print()


def new_composed():
    yield 'A'
    c = yield from delegated()
    print(c)
    yield 'B'


it = new_composed()
print(next(it))
while True:
    try:
        b = it.send('x')
        print(b)
    except StopIteration:
        break
