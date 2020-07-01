"""
https://kenreitz.org/essays/the-future-of-python-http
"""
import requests

# 这些包都过时了, 因此没法用
from webscale import DevNullAdpater
from wsgicore.adapters import WsgiAdapter
from haystackapp.core import app as haystack

s = requests.session()
s.mount('null:', DevNullAdapter())
s.mount('http://haystack', WsgiAdapter(app=haystack))

# Make a request via DevNullAdapter
r = s.get('null://someurl')

# Make a request via Haystack WSGI App
r = s.get('http://haystack/index')

# Make a request via standard HTTPS
r = s.get('https://github.com/')