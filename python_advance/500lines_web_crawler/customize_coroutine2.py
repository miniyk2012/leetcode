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
        yield f  # 一旦f.set_result()被执行，fetch()这个coro就会从yield f 暂停处继续往下执行, 这里就是当EVENT_WRITE可写时, 会继续往下走
        selector.unregister(sock.fileno())
        # connected后send
        request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(self.url)
        sock.send(request.encode('ascii'))

        print('connected!')

        while True:

            f = Future()

            def on_readable():
                print('read at most 4 bit once time from sock')
                f.set_result(sock.recv(4))

            selector.register(sock.fileno(),
                              EVENT_READ,
                              on_readable)
            chunk = yield f
            selector.unregister(sock.fileno())
            # 收到部分数据后保存
            if chunk:
                self.response += chunk
            else:
                # Done reading.
                break


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
            print('Task finished [or coro finished]')
            return

        next_future.add_done_callback(self.step)  # 只要coro没有运行结束，让coro从上次暂停的地方继续往下运行


fetcher = Fetcher('/353/')
Task(fetcher.fetch())


def loop():
    while True:
        events = selector.select()
        if len(events) == 0:
            break
        for event_key, event_mask in events:
            callback = event_key.data
            callback()


loop()
print(fetcher.response)
