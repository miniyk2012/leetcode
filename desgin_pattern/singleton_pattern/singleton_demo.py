# What the Gang of Four’s original Singleton Pattern
# might look like in Python.


class Logger(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print("create a Logger instance")
            cls._instance = cls.__new__(cls)
        return cls._instance


class Singleton:
    _instance = None

    def __init__(self, v):
        print('singleton init')
        self.v = v

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating the Singleton')
            cls._instance = super(Singleton, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance


if __name__ == "__main__":
    logger1 = Logger.instance()
    logger2 = Logger.instance()
    print('Are they the same object?', logger1 is logger2)
    print()
    s1 = Singleton('s1')
    print(s1)
    print(s1.v)
    s2 = Singleton('s2')
    print(s2)
    print(s2.v)
    print('Are they the same object?', s1 is s2)
    
