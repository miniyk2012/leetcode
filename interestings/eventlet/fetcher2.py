import selectors
import socket

host_to_access = {'www.baidu.com'
    # , 'www.taobao.com', 'www.tencent.com', 'www.toutiao.com', 'www.meituan.com',
    #               'www.tmall.com'
                  }
selector = selectors.DefaultSelector()
stopped = False


class Fetcher:
    def __init__(self, host):
        self.response = b''  # Empty array of bytes.
        self.host = host

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect((self.host, 80))
        except BlockingIOError:
            pass
        f = Future()

        def on_connected():
            f.set_result(None)
            print('{} connected'.format(self.host))

        selector.register(sock.fileno(), selectors.EVENT_WRITE, on_connected)

        yield f
        selector.unregister(sock.fileno())

        request = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(self.host)
        sock.send(request.encode('ascii'))

        global stopped
        while True:
            f = Future()

            def on_readable():
                try:
                    data = sock.recv(40)
                    f.set_result(data)
                except socket.error as e:
                    print(e)

            selector.register(sock.fileno(), selectors.EVENT_READ, on_readable)
            chunk = yield f
            selector.unregister(sock.fileno())
            # print("host:{},read response:{}".format(self.host, chunk))
            if chunk:
                self.response += chunk
            else:
                print(self.host + " removed, whole response: ", self.response)
                host_to_access.remove(self.host)
                if not host_to_access:
                    stopped = True
                return


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
