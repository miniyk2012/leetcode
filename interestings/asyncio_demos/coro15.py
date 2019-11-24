import asyncio
from functools import partial


def mark_done(future, result):
    print(f'Set to: {result}')
    future.set_result(result)


async def b2():
    loop = asyncio.get_event_loop()
    fut = asyncio.Future()
    loop.call_later(2, mark_done, fut, 'the result')
    loop.call_later(1, partial(print, 'Hello'))
    loop.call_later(1, partial(print, 'Greeting'))
    print(f'Done: {fut.done()}')
    await asyncio.sleep(2)
    print(f'Done: {fut.done()}, Result: {fut.result()}')


if __name__ == '__main__':
    asyncio.run(b2())