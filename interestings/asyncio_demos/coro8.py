import asyncio
import random


async def a():
    print('Suspending a')
    await asyncio.sleep(3)
    print('Resuming a')
    return 'A'


async def cancel_after(task, when):
    await asyncio.sleep(when)
    task.cancel()


async def d(n):
    print(f'Suspending a with {n}')
    await asyncio.sleep(2)
    print(f'Resuming a with {n}')
    return 'A'


async def c5():
    loop = asyncio.get_event_loop()
    print(id(loop))
    n = random.randint(1, 100)
    outer = asyncio.shield(d(n))
    # outer = asyncio.create_task(d(n))
    loop.create_task(cancel_after(outer, 1))
    try:
        await outer
    except asyncio.CancelledError:
        print('Cancelled!')


def main():
    loop = asyncio.get_event_loop()
    print(id(loop))
    loop.run_until_complete(c5())

main()