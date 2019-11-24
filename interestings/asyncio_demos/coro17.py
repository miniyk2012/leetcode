"""同步代码实现异步
用run_into_executor可以把同步函数逻辑转化成一个协程，且实现了并发"""
import asyncio
import concurrent
import time


def a():
    time.sleep(1)
    return 'A'


async def b():
    await asyncio.sleep(2)
    return 'B'


def show_perf(func):
    print('*' * 20)
    start = time.perf_counter()
    ret = asyncio.run(func())
    print('result:', ret)
    print(f'{func.__name__} Cost: {time.perf_counter() - start}')


async def c1():
    loop = asyncio.get_running_loop()
    print('id(loop)', id(loop))
    print('before', loop._default_executor)
    ret = await asyncio.gather(
        loop.run_in_executor(None, a),
        b()
    )
    print('after', loop._default_executor)
    return ret


async def c2():
    loop = asyncio.get_running_loop()
    print('id(loop)', id(loop))
    print('before', loop._default_executor)
    ret = await loop.run_in_executor(None, a)
    print('after', loop._default_executor)
    return ret


async def c3():
    loop = asyncio.get_running_loop()
    print('id(loop)', id(loop))
    print('before', loop._default_executor)
    with concurrent.futures.ProcessPoolExecutor() as e:
        ret = (await asyncio.gather(
            loop.run_in_executor(e, a),
            b()
        ))
        print('after', loop._default_executor)
        return ret


async def perf_time():
    start = time.perf_counter()
    ret = await asyncio.gather(c1(), c2(), c3())
    print(f'Cost: {time.perf_counter() - start}')
    return ret


if __name__ == '__main__':
    print(asyncio.run(perf_time()))

    show_perf(c1)
    show_perf(c2)
    show_perf(c3)
