from django.utils.functional import SimpleLazyObject, lazy, LazyObject


# 有延迟实例化需求的类DemoObject
class DemoObject(object):
    def __init__(self):
        print('init')
        self.title = 'just a demo'


# 因为继承了LazyObject，所以DemoLazyObject有延迟实例化的功能
class DemoLazyObject(LazyObject):
    # 子类需要重新实现_setup方法，该方法实例化类DemoObject，并把生成的对象赋给_wrapped。
    def _setup(self):
        self._wrapped = DemoObject()


# 定义一个需要惰性计算的函数，该函数只是简单返回字符串的title
def lazy_func(text):
    print('lazy func')
    return text.title()


# 获得一个惰性代理对象lazy_wraper
lazy_wraper = lazy(lazy_func, str)

if __name__ == '__main__':
    a_demo = SimpleLazyObject(lambda: DemoObject())
    print('call a_demo')
    print(a_demo.title)
    print(a_demo.title)

    print()
    # 初始化的时候把_wrapped设置为empty，未对实际的类进行实例化操作，达到延迟类实例化的效果。
    b_demo = DemoLazyObject()
    print('call b_demo')
    # 只有对结果需要进行某些操作的时候，比如获取属性，才会去调用_setup进行实例化。
    print(b_demo.title)
    print(b_demo.title)

    print()
    c_demo = DemoObject()
    print('call c_demo')
    print(c_demo.title)
    print(c_demo.title)

    print()
    # 注意，此时虽然调用了惰性函数，但并不会直接去调用lazy_func函数
    # res只是一个代理对象, 而不是直接返回调用的结果。当实际使用结果的时候，该代理对象才会触发去调用相关的函数，返回计算结果。
    res = lazy_wraper('hello world')
    print('call lazy func')
    # 在对结果进行打印的时候，才会去实际调用lazy_func。
    print(res)

    print()
    res = lazy_func('hello world')
    print('call lazy func')
    print(res)
