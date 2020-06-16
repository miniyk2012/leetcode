import selectors
import socket
from selectors import EVENT_WRITE, EVENT_READ

host_to_access = {'www.baidu.com', 'www.taobao.com', 'www.tencent.com', 'www.toutiao.com', 'www.meituan.com',
                  'www.tmall.com'}
selector = selectors.DefaultSelector()
stopped = False

class Fetcher:
    def __init__(self, host):
        self.response = b''  # Empty array of bytes.
        self.host = host
        self.sock = None

    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect((self.host, 80))
        except BlockingIOError:
            pass
        # Register next callback.
        selector.register(self.sock.fileno(),
                          EVENT_WRITE,
                          self.connected)

    def connected(self, key, mask):
        selector.unregister(self.sock.fileno())
        request = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(self.host)
        print('{} connected'.format(self.host))
        self.sock.send(request.encode('ascii'))
        # Register the next callback.
        selector.register(key.fd,
                          EVENT_READ,
                          self.read_response)

    def read_response(self, key, mask):
        global stopped
        chunk = self.sock.recv(64)  # 64 chunk size.
        if chunk:
            self.response += chunk
            print(self.host, chunk, 'continue')
        else:
            selector.unregister(key.fd)  # Done reading.
            host_to_access.remove(self.host)
            if not host_to_access:
                stopped = True
            print("key:{},mask:{},read response:{}".format(key, mask, self.response))


def loop():
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)

if __name__ == '__main__':
    for host in host_to_access:
        fetcher = Fetcher(host)
        fetcher.fetch()
    loop()
