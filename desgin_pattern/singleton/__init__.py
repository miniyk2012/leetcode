from __future__ import annotations
from typing import Optional


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, level):
        # 会被调用多次
        self.level = level


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instance: Optional[Singleton] = None

    def __call__(cls, *args, **kwargs) -> Singleton:
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):

    def __init__(self, value: str) -> None:
        print('*' * 10)  # 只会被调用1次
        self.value = value

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == '__main__':
    logger1 = Logger('info')
    logger2 = Logger('debug')
    assert logger1 is logger2
    assert logger1.level == 'debug'
    assert logger2.level == 'debug'

    s1 = Singleton(10)
    s2 = Singleton(20)
    if id(s1) == id(s2):
        print(s1.value)
        print(s2.value)
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
