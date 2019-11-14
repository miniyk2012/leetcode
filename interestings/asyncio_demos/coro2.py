import asyncio


def c():
    print('Enter c')
    return 12


loop = asyncio.get_event_loop()
future = loop.run_in_executor(None, c)


async def get_result():
    print(future)
    await future
    print(future)
    return future.result()


def spam():
    future = loop.run_in_executor(None, c)
    yield from future


if __name__ == '__main__':
    ret = loop.run_until_complete(get_result())
    print('ret:', ret)
    print('*' * 20)
    print(next(spam()))

    loop.close()

