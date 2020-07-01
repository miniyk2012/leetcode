"""
https://kenreitz.org/essays/the-future-of-python-http
"""
import requests
import json

# 这些包都过时了, 因此没法用
# from webscale import DevNullAdpater
# from wsgicore.adapters import WsgiAdapter
# from haystackapp.core import app as haystack

from requests.adapters import BaseAdapter


class A:
    def __init__(self):
        self.elapsed = None
        self.history = None
        self.raw = None
        self.is_redirect = None
        self.content = json.dumps([1, 2, 3])


class DevNullAdapter(BaseAdapter):
    def send(self, request, stream=False, timeout=None, verify=True,
             cert=None, proxies=None):
        return A()


if __name__ == '__main__':
    s = requests.session()
    s.mount('null:', DevNullAdapter())
    # s.mount('http://haystack', WsgiAdapter(app=haystack))

    # Make a request via DevNullAdapter
    r = s.get('null://someurl')
    print(r.content)
    print(type(r.content))

    # Make a request via Haystack WSGI App
    # r = s.get('http://haystack/index')

    # Make a request via standard HTTPS
    r = s.get('https://github.com/')
    print(r.content)
