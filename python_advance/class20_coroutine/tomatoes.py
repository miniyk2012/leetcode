import asyncio
import random


class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos


all_potatos = Potato.make(5)


async def ask_for_potato():
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 10)))


async def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        else:
            potato = all_potatos.pop()
            yield potato
            count += 1
            if count == num:
                break


async def buy_potatos():
    bucket = []
    async for p in take_potatos(50):  # 后面迭代的是一个异步生成器。
        print(f'Got potato {id(p)}...')
        bucket.append(p)


async def buy_tomatos():
    bucket = []
    async for p in take_potatos(50):  # 后面迭代的是一个异步生成器。
        print(f'Got tomato {id(p)}...')
        bucket.append(p)


async def main():
    task1 = asyncio.create_task(buy_potatos())
    task2 = asyncio.create_task(buy_tomatos())
    await task1
    await task2


if __name__ == '__main__':
    asyncio.run(main())
