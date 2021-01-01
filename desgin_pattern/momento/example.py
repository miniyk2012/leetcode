'''https://mp.weixin.qq.com/s/5swuBXkm2kv_kvfZOXNhwg'''

from copy import copy, deepcopy
from functools import wraps


def memento(obj, deep=True):
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Transaction:

    # deep = False
    # states = []

    def __init__(self, deep, *targets):
        self.deep = deep
        self.targets = targets
        self.commit()

    def commit(self):
        # 重新为states赋值, 这样states就保存了target的新状态
        self.states = [memento(target, self.deep) for target in self.targets]

    def rollback(self):
        for a_state in self.states:
            a_state()


def transactional(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # args[0] is obj
        state = memento(args[0])
        try:
            func(*args, **kwargs)
        except Exception as e:
            state()
            raise e

    return wrapper


class Transactional:

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, cls):
        def transaction(*args, **kwargs):
            state = memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e

        return transaction


class NumObj:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s, %r>' % (self.__class__.__name__, self.value)

    def increment(self, num=1):
        self.value += num

    @Transactional
    def do_stuff(self):
        self.increment()
        print(self)
        self.value += '111'

    @transactional
    def do_stuff2(self):
        self.increment(2)
        print(self)
        self.value += '222'

    z = lambda x: x


if __name__ == '__main__':
    num_obj = NumObj(-1)
    print(num_obj)
    # 使用Transactional
    print('-- now doing stuff')

    try:
        num_obj.do_stuff()
    except Exception:
        print('-> doing stuff failed')
        import sys
        import traceback

        traceback.print_exc(file=sys.stdout)

    print(num_obj)

    # 使用transactional
    print('-- now doing stuff2')
    try:
        num_obj.do_stuff2()
    except Exception:
        print('-> doing stuff2 failed')
        import sys
        import traceback

        traceback.print_exc(file=sys.stdout)
    print(num_obj)

    print(num_obj.do_stuff)
    print(num_obj.do_stuff2)
    print(num_obj.z)

    # 使用Transaction
    print('\n使用Transaction')
    a_transaction = Transaction(True, num_obj)
    try:
        for i in range(3):
            num_obj.increment()
            print(num_obj)

        a_transaction.commit()
        print('----committed')
        for i in range(3):
            num_obj.increment()
            print(num_obj)
        num_obj.value += 'x'
        print(num_obj)
    except Exception:
        a_transaction.rollback()
        print('----rollback')
    print(num_obj)
