import random
import asyncio


async def d(n):
    print(f'Suspending a with {n}')
    await asyncio.sleep(2)
    print(f'Resuming a with {n}')
    return 'A'

async def b():
    print('Suspending b')
    await asyncio.sleep(1)
    print('Resuming b')
    return 'B'


async def c6():
    n = random.randint(1, 100)
    task1 = asyncio.shield(d(n))
    task2 = asyncio.create_task(b())
    task1.cancel()
    await asyncio.gather(task1, task2, return_exceptions=True)

