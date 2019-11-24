import asyncio


async def myfun(i):
    print('start {}th'.format(i))
    await asyncio.sleep(1)
    print('finish {}th'.format(i))


async def main():
    myfun_list = [myfun(i) for i in range(10)]
    await asyncio.gather(*myfun_list)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    myfun_list = [myfun(i) for i in range(10)]
    loop.run_until_complete(asyncio.gather(*myfun_list))
    print()
    loop.run_until_complete(main())
