import threading


class SingletonType(type):
    """线程安全的单例: https://www.cnblogs.com/huchong/p/8244279.html
    基于参数的单例: https://code.activestate.com/recipes/578103-singleton-parameter-based/"""
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        key = (cls, args, str(kwargs))
        if not hasattr(cls, "_instances") or key not in cls._instances:
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instances"):
                    cls._instances = {}
                if key not in cls._instances:
                    cls._instances[key] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[key]


class Foo(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    foo1 = Foo('name1')
    foo2 = Foo('name2')
    foo3 = Foo('name2')
    print(foo1, foo2, foo3)
    print(foo1 is foo2)
    print(foo2 is foo3)
    print(foo1.name)
    print(foo2.name)
    print(foo3.name)
