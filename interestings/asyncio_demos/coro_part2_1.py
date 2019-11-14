import asyncio


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

