import socket
from selectors import DefaultSelector, EVENT_WRITE

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
        yield f
        selector.unregister(sock.fileno())
        print('connected!')


class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
            print(next_future)
        except StopIteration:
            print('stop')
            return

        next_future.add_done_callback(self.step)  # 假如coro没有运行结束，让coro从上次暂停的地方继续往下运行


fetcher = Fetcher('/353/')
Task(fetcher.fetch())


def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()

loop()