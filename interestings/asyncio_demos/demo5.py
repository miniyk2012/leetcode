import asyncio
import time


def myfun(i):
    print('start {}th'.format(i))
    time.sleep(1)
    print('finish {}th'.format(i))
    return i


async def main():
    loop = asyncio.get_event_loop()
    futures = (
        loop.run_in_executor(
            None,
            myfun,
            i)
        for i in range(10)
    )
    a = await asyncio.gather(*futures)
    print(a)


if __name__ == '__main__':
    asyncio.run(main())
