import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()


class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

    # Method on Future class.
    def __iter__(self):
        # Tell Task to resume me here. 这样的好处是, 代码中都写成yield from即可, 而不用区分何时用yield, 何时用yield from
        yield self
        return self.result


def read(sock):
    f = Future()

    def on_readable():
        f.set_result(sock.recv(4096))

    selector.register(sock.fileno(), EVENT_READ, on_readable)
    chunk = yield from f  # Read one chunk.
    selector.unregister(sock.fileno())
    return chunk


def read_all(sock):
    response = []
    # Read whole response.
    chunk = yield from read(sock)
    while chunk:
        response.append(chunk)
        chunk = yield from read(sock)

    return b''.join(response)


class Fetcher:
    def __init__(self, url):
        self.response = b''  # Empty array of bytes.
        self.url = url

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect(('xkcd.com', 80))
        except BlockingIOError:
            pass

        f = Future()

        def on_connected():
            f.set_result(None)

        selector.register(sock.fileno(),
                          EVENT_WRITE,
                          on_connected)
        yield from f  # 一旦f.set_result()被执行，fetch()这个coro就会从yield f 暂停处继续往下执行, 这里就是当EVENT_WRITE可写时, 会继续往下走
        selector.unregister(sock.fileno())
        # connected后send
        request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(self.url)
        sock.send(request.encode('ascii'))

        print('connected!')

        self.response = yield from read_all(sock)
        print(self.response)


class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
        except StopIteration:
            print('stop')
            return

        next_future.add_done_callback(self.step)  # 只要coro没有运行结束，让coro从上次暂停的地方继续往下运行


def fetch_urls():
    # 异步爬取数百个网站
    fetchers = [Fetcher(f'/{num}/') for num in range(10, 500)]
    for fetcher in fetchers:
        Task(fetcher.fetch())  # 每个Task负责爬一个网址


def loop():
    while True:
        events = selector.select()
        if len(events) == 0:
            break
        for event_key, event_mask in events:
            callback = event_key.data
            callback()


fetch_urls()
loop()
