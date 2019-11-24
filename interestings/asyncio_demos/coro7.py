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


async def stop_after(loop, when):
    await asyncio.sleep(when)
    loop.stop()


def c4():
    loop = asyncio.get_event_loop()
    outer = asyncio.shield(a())
    outer.cancel()
    loop.create_task(stop_after(loop, 2))

    loop.run_forever()
    print(outer.cancelled())