def consumer():
    status = True
    while True:
        n = yield status
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
    c.send(None)
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