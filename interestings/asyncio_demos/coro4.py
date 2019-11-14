import asyncio
import time


async def a():
    print('Suspending a')
    await asyncio.sleep(3)
    print('Resuming a')


async def b():
    print('Suspending b')
    await asyncio.sleep(1)
    print('Resuming b')


async def c():
    await a()
    await b()


async def c2():
    await asyncio.gather(a(), b())


async def c3():
    await asyncio.wait([a(), b()])


async def c4():
    task1 = asyncio.create_task(a())
    task2 = asyncio.create_task(b())
    print('before task1')
    await task1
    print('between tasks')
    await task2
    print('after task2')


async def c5():
    task = asyncio.create_task(b())
    await a()
    await task


async def c6():
    task = asyncio.create_task(b())
    await task
    await a()


async def c7():
    task1 = asyncio.create_task(b())
    task2 = asyncio.create_task(b())
    task3 = asyncio.create_task(b())
    await a()


async def c8():
    task = asyncio.ensure_future(b())
    await a()
    await task


async def c9():
    loop = asyncio.get_event_loop()
    task = loop.create_task(b())
    await a()
    await task


def show_performance(func):
    print('*' * 20)
    start = time.perf_counter()
    asyncio.run(func())
    print(f'{func.__name__} Cost: {time.perf_counter() - start}')


if __name__ == '__main__':
    # show_performance(c)
    # show_performance(c2)
    # show_performance(c3)
    # show_performance(c4)
    # show_performance(c5)
    # show_performance(c6)
    # show_performance(c7)
    show_performance(c8)
    show_performance(c9)
