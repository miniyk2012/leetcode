"""第三方库，不是线程安全的哟"""

from __future__ import annotations

from rbnics_utils_decorators_dispatch import dispatch  # 使用补丁来支持lambda功能 https://github.com/mrocklin/multipledispatch/issues/78


class A:
    def __init__(self, name='a'):
        self.name = name

    def __str__(self):
        return super(A, self).__str__() + self.name

    @dispatch(int)
    def foo(self, a):
        print(f'int a')

    @dispatch(str)
    def foo(self, a):
        print(f'str a')

    @dispatch(str, int)
    def foo(self, a, b):
        print(f'str {a} int {b}')

    # # Python interpreter fails on @dispatch(F) because F is not fully defined yet, 因此使用lambda来解决该问题
    @dispatch(lambda cls: cls)
    def foo(self, other):
        print(f'other {other}')


if __name__ == '__main__':
    a = A()
    b = A('b')
    a.foo(1)
    a.foo("x")
    a.foo('a', 3)
    a.foo(b)

    print(a)
    print(b)
