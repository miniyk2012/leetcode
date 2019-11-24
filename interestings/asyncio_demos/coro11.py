import asyncio
import time
from contextlib import asynccontextmanager


async def a():
    print('a')
    await asyncio.sleep(3)
    return 'A'


async def b():
    print('b')
    await asyncio.sleep(1)
    return 'B'


async def s1():
    return await asyncio.gather(a(), b())


"""装饰一个异步函数(协程)
"""


@asynccontextmanager
async def async_timed(func):
    start = time.perf_counter()
    yield await func()
    print(f'Cost: {time.perf_counter() - start}')


async def c():
    async with async_timed(s1) as rv:
        print(f'Result: {rv}')


async def main():
    await asyncio.gather(a(), b(), c(), a(), b())


if __name__ == '__main__':
    asyncio.run(main())
