import asyncio
import time
from contextlib import contextmanager


async def a():
    await asyncio.sleep(3)
    return 'A'


async def b():
    await asyncio.sleep(1)
    return 'B'


async def s1():
    return await asyncio.gather(a(), b())


@contextmanager
def timed(func):
    start = time.perf_counter()
    yield asyncio.run(func())
    print(f'Cost: {time.perf_counter() - start}')


if __name__ == '__main__':

    with timed(s1) as rv:
        print(f'Result: {rv}')