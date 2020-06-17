import selectors
import socket

host_to_access = {'www.baidu.com'
    # , 'www.taobao.com', 'www.tencent.com', 'www.toutiao.com', 'www.meituan.com',
    #               'www.tmall.com'
                  }
selector = selectors.DefaultSelector()
stopped = False


def connect(sock, address):
    f = Future()
    sock.setblocking(False)
    try:
        sock.connect(address)
    except BlockingIOError:
        pass

    def on_connected():
        f.set_result(None)
        print('{} connected'.format(address))

    selector.register(sock.fileno(), selectors.EVENT_WRITE, on_connected)
    yield from f
    selector.unregister(sock.fileno())


def read(sock):
    f = Future()

    def on_readable():
        f.set_result(sock.recv(40))

    selector.register(sock.fileno(), selectors.EVENT_READ, on_readable)
    chunk = yield from f
    selector.unregister(sock.fileno())
    return chunk


def read_all(sock):
    response = []
    chunk = yield from read(sock)
    while chunk:
        response.append(chunk)
        chunk = yield from read(sock)
    return b''.join(response)


class Fetcher:
    def __init__(self, host):
        self.response = b''  # Empty array of bytes.
        self.host = host

    def fetch(self):
        global stopped
        sock = socket.socket()
        yield from connect(sock, (self.host, 80))

        request = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(self.host)
        sock.send(request.encode('ascii'))
        self.response = yield from read_all(sock)
        print("{} response:{}".format(self.host, self.response))
        host_to_access.remove(self.host)
        if not host_to_access:
            stopped = True


class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            # send会进入到coro执行, 即fetch, 直到下次yield
            # next_future 为yield返回的对象
            print('future result:', future.result)
            next_future = self.coro.send(future.result)
            print('next_future result:', next_future.result)
        except StopIteration:
            return
        next_future.add_done_callback(self.step)


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

    def __iter__(self):
        yield self
        return self.result


def loop():
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()


if __name__ == '__main__':
    import time

    start = time.time()
    for host in host_to_access:
        fetcher = Fetcher(host)
        Task(fetcher.fetch())
    loop()
