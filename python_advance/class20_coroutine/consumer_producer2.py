def consumer():
    status = True
    while True:
        n = yield status  #  先yield把status返回给producer后会卡住，直到接收到send的值赋给n再往下跑
        print("我拿到了{}!".format(n))
        if n == 3:
            status = False
        if n == 5:
            status = 'status'


def producer(consumer):
    n = 5
    while n > 0:
        # yield给主程序返回消费者的状态
        yield consumer.send(n)
        n -= 1

async def async_function():
    return 1

if __name__ == '__main__':
    c = consumer()
    print(c.send(None))
    p = producer(c)
    for status in p:
        print(status)
        if status == False:
            print("我只要3,4,5就行啦")
            break
    print("程序结束")

    try:
        async_function().send(None)
    except StopIteration as e:
        print(e.value)


def gen_fn():
    result = yield 1
    print('result of yield: {}'.format(result))
    result2 = yield 2
    print('result of 2nd yield: {}'.format(result2))
    return 'done'