"""非线程安全哟"""
registry = {}


class MultiMethod(object):
    def __init__(self, name):
        self.name = name
        self.typemap = {}

    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args)  # a generator expression!
        function = self.typemap.get(types)
        if function is None:
            raise TypeError("no match")
        return function(*args)

    def register(self, types, function):
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = function
        # print(self.typemap)


def multimethod(*types):
    def register(function):
        print(function)  # 只有在2次装饰的时候, fuction才是mm.MultiMethod, 才拥有__lastreg__
        function = getattr(function, "__lastreg__", function)
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(types, function)
        mm.__lastreg__ = function  # 保存本次注册的函数
        return mm
    return register