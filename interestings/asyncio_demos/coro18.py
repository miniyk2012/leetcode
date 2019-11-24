import asyncio
from functools import partial
from threading import Thread


async def a():
    print('before a')
    await asyncio.sleep(1)
    print('after a')
    return 'A'


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def shutdown(loop):
    loop.stop()


def shutdown_callback(future, loop):
    print('callback')
    loop.stop()
    print('new loop done')


async def b1():
    new_loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(new_loop,))  # 在另一个线程中开启一个event loop
    t.start()

    future = asyncio.run_coroutine_threadsafe(a(), new_loop)  # loop在另一个线程中跑, 且是线程安全的(与主线程不会因为cpu分配的问题导致逻辑出现问题)
    # print('add callback')
    # future.add_done_callback(partial(shutdown_callback, loop=new_loop))
    print(future)
    print(f'Result: {future.result(timeout=2)}')
    new_loop.call_soon_threadsafe(partial(shutdown, new_loop))




if __name__ == '__main__':
    asyncio.run(b1())
