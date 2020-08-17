import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


# Example
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name


# Example
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance is not None:
            return self._instance
        obj = super(Singleton, self).__call__(*args, **kwargs)
        self._instance = obj
        return obj


class Foo(metaclass=Singleton):
    def __init__(self, value):
        self.value = value
        print('Creating Foo')


if __name__ == '__main__':
    a = Spam('Guido')
    b = Spam('Guido')
    print(a is b)

    c = Foo("a")
    d = Foo("b")
    print(c is d)
    print(c.value)
