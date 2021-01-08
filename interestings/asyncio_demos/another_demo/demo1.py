"""这只是一个对yield, send的实验, 不用太关注"""

import types


def func1():
    ret = yield request("http://test.com/foo")
    ret = 'func1:' + ret
    ret = yield func2(ret)
    ret = 'func1:' + ret
    return ret


def func2(data):
    result = yield request("http://test.com/" + data)
    result = 'func2:' + result
    return result


def request(url):
    # 这里模拟返回一个io操作，包含io操作的所有信息，这里用字符串简化代替
    result = yield "iojob of %s" % url
    return result


def isgenerator(gen):
    return isinstance(gen, types.GeneratorType)


class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def wrapper(gen):
    # 第一层调用 入栈
    stack = Stack()
    stack.push(gen)
    result = None

    # 开始逐层调用
    while True:
        # 获取栈顶元素
        item = stack.peek()
        # 生成器
        if isgenerator(item):
            try:
                # 尝试获取下层调用并入栈
                child = item.send(result)  # child是'yield='右边的东西
                stack.push(child)
                # result 使用过后就还原为None
                result = None
                # 如果是generator, 由wrapper驱动, 入栈后直接进入下次循环，继续向下探索
                continue
            except StopIteration as e:
                # 如果自己运行结束了，就暂存result，下一步让自己出栈
                result = e.value
                # print('e.value=', result)
        else:  # IO 操作
            # 遇到了 IO 操作，yield 出去，由外层框架读取IO, IO 完成后会被用 IO 结果唤醒并暂存到 result
            # print('io=', item)
            result = yield item  # result接收外部的send输入

        # 走到这里则本层已经执行完毕，出栈，下次迭代将是调用链上一层
        stack.pop()
        # 没有上一层的话，那整个调用链都执行完成了，return
        if stack.empty():
            print("finished")
            return result


def main1():
    w = wrapper(func1())
    url1 = w.send(None)
    print(url1)  # iojob of http://test.com/foo
    # 做url1 IO, 得到response, 结果"bar"传入，继续运行
    url2 = w.send("bar")
    print(url2)  # iojob of http://test.com/bar
    # 做url2 IO, 得到response, 结果"barz"传入，继续运行, 遇到StopIteration结束
    try:
        w.send("barz")
    except StopIteration as e:
        r = e.value
        print(r)


# 维护一个就绪列表，存放所有完成的IO事件，格式为（wrapper，result）
ready = []


def on_request():
    # 使用 wrapper 包装后，可以只通过send处理IO了
    g = wrapper(func1())
    # 把开始状态直接视为结果为None的就绪状态
    ready.append((g, None))


class Observable:
    def __init__(self):
        self.func = []

    def addListener(self, io_job, func):
        self.func.append((io_job, func))

    def change(self):
        for io_job, func in self.func:
            func(io_job)
        self.func = []


observable = Observable()


# 让ioloop每轮循环都执行此函数，用来处理的就绪的IO
def process_ready():
    # 遍历所有已经就绪生成器，将其向下推进
    for g, result in ready:
        # 用result唤醒生成器，并得到下一个io操作
        try:
            io_job = g.send(result)
            # print('io_job=', io_job)
        except StopIteration as e:
            print(e.value)
            break
        # 注册io操作, 完成后把生成器加入就绪列表，等待下一轮处理
        observable.addListener(
            io_job, lambda io_job: ready.append((g, io_job)))
    ready.clear()


def main2():
    on_request()
    on_request()
    on_request()
    while True:
        if not ready:
            break
        print(ready)
        print()
        process_ready()
        observable.change()


if __name__ == '__main__':
    # main1()
    main2()
