import asyncio
from functools import partial


def mark_done(future, result):
    print(f'Set to: {result}')
    future.set_result(result)


async def b1():
    loop = asyncio.get_event_loop()
    fut = asyncio.Future()
    loop.call_soon(mark_done, fut, 'the result')
    loop.call_soon(partial(print, 'Hello', flush=True))
    loop.call_soon(print, 'Greeting')
    print(f'Done: {fut.done()}')
    await asyncio.sleep(0)
    print(f'Done: {fut.done()}, Result: {fut.result()}')

if __name__ == '__main__':
    asyncio.run(b1())