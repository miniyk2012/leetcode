import asyncio


async def a():
    print('enter a')
    await asyncio.sleep(0)
    print('left a')
    return 12


async def main(task):
    print(task)
    await task
    print(task.result())


def c1():
    loop = asyncio.get_event_loop()
    task = loop.create_task(a())
    loop.run_until_complete(main(task))
    loop.close()


async def c2():
    task = asyncio.create_task(a())
    print(task)
    await task
    print(task.result())


def c3():
    asyncio.run(c2())


if __name__ == '__main__':
    c1()
    print('*' * 100)
    c3()
