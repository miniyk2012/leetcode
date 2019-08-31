"""Five-minute Multimethods in Python
https://www.artima.com/weblogs/viewpost.jsp?thread=101605
关于重载的总结见我的笔记:
https://app.yinxiang.com/shard/s67/nl/18225537/9a0c6b27-cc0d-4712-a00a-3348528a37f7?title=python%E7%9A%84%E5%87%BD%E6%95%B0%E9%87%8D%E8%BD%BD"""


def bar(a):
    print(a)


def bar(a, b, c):
    print(a, b, c)


from mm import multimethod


@multimethod(float, float)
def foo(a, b):
    print(f'float {a}, float {b}')


@multimethod(str, str)
def foo(a, b):
    print(f'str {a}, srt {b}')


try:
    @multimethod(str, str)
    def foo(a, b):
        print('duplicated')
except TypeError:
    pass
else:
    raise RuntimeError('不应该进入这里')


@multimethod(int, int)
@multimethod(int)
def foo(a, b=10):
    print(f'int {a}, int {b}')

if __name__ == '__main__':
    try:
        bar(1)  # TypeError: foo() missing 1 required positional argument: 'b'
    except TypeError:
        pass
    bar(1, 2, 5)

    foo(3, 4)
    foo('3', '4')
    foo(4.5, 5.0)

    foo(4)

    print(foo)
