def my_coroutine():
    while True:
        received = yield 3
        print('Received', received)

it = my_coroutine()
val = it.send(None)
print('Send return', val)

val = it.send(5)
print('Send return', val)

print()

def delegated():
    a = yield 1
    print(a)
    b = yield 2
    print(b)

def composed():
    yield 'A'
    it = delegated()
    next(it)
    while True:
        r = it.send('x')
    yield 'B'

it = composed()
