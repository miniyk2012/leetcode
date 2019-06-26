import asyncio

future = asyncio.Future()

async def coro1():
    await asyncio.sleep(1)
    print('core1 before', future.done())
    future.set_result('data')
    print('core1 after', future.done())


async def coro2():
    print(await future)
    print('core2', future.done())

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([
    coro1(),
    coro2()
]))
loop.close()