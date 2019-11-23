import asyncio
import time


async def a():
    print('Suspending a')
    await asyncio.sleep(3)
    print('Resuming a')
    return 'A'


async def b():
    print('Suspending b')
    await asyncio.sleep(1)
    print('Resuming b')
    return 'B'


async def main():
    start = time.perf_counter()
    done, pending = await asyncio.wait([a(), b()], return_when=asyncio.tasks.FIRST_COMPLETED)
    print(f'first Cost: {time.perf_counter() - start}')  # 1s

    start = time.perf_counter()
    task = await pending.pop()
    print(f'pending Cost: {time.perf_counter() - start}')  # 2s



asyncio.run(main())