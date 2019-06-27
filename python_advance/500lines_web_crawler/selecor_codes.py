import socket
from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()

sock = socket.socket()
sock.setblocking(False)
sock2 = socket.socket()
sock2.setblocking(False)

try:
    sock.connect(('xkcd.com', 80))
except BlockingIOError:
    pass

try:
    sock2.connect(('xkcd.com', 80))
except BlockingIOError:
    pass


def connected(key, mask):
    selector.unregister(key.fd)
    print('connected!')


selector.register(sock.fileno(), EVENT_WRITE, connected)
selector.register(sock2.fileno(), EVENT_WRITE, connected)


def loop():
    while True:
        events = selector.select()
        print(len(events))
        if len(events) == 0:
            break
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)


import time

time.sleep(1)
loop()
