import asyncio
from functools import partial


async def a():
    print('in a')
    await asyncio.sleep(1)
    return 'A'


def callback(future):
    print(f'in call back, future.result()={future.result()}')


def callback2(future, n):
    print(f'Result: {future.result()}, N: {n}')


def callback_factory(n):
    def callback(future):
        print(f'Result: {future.result()}, N: {n}')

    return callback


async def main():
    task1 = asyncio.create_task(a())
    task1.add_done_callback(callback)
    task1.add_done_callback(callback_factory(n=4))  # 可以添加多个callback

    task2 = asyncio.create_task(a())
    task2.add_done_callback(partial(callback2, n=2))
    task2.add_done_callback(callback_factory(n=3))  # 可以添加多个callback
    return await task1


if __name__ == '__main__':
    ret = asyncio.run(main())
    print(ret)
