依赖注入是个非常大的话题.
https://medium.com/@shivama205/dependency-injection-python-cb2b5f336dce

https://qihqi.github.io/python/dependency-injection-python/给了我一个灵感, 我做了一个小小尝试,
https://github.com/miniyk2012/my_hello_flask/blob/master/demos/form/views.py:

```python
def use_services(*services):
    """用于依赖注入"""
    def outer(func):
        def wrapper(s=services):
            return func(*s)

        return wrapper

    return outer


class Service1:
    @classmethod
    def work(cls):
        return "work1"


class Service2:
    @classmethod
    def work(cls):
        return "work2"



def do_work(s1, s2):
    return s1.work() + s2.work()

...

app.add_url_rule(**{'rule': '/do-work', 'view_func': use_services(Service1, Service2)(do_work), 'methods': ['GET', 'POST'],
     "endpoint": "do_work"})

```