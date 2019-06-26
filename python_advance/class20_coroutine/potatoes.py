import random
from asyncio import sleep
import asyncio


class Fruite:
    cls_id = 0

    def __init__(self):
        self.potato_id = self.cls_id

    @classmethod
    def make_fruite(cls, n):
        potatoes = []
        for _ in range(n):
            cls.cls_id += 1
            potatoes.append(cls())
        return potatoes

class Tomato(Fruite):
    pass

class Potato(Fruite):
    pass


async def produce_random(fruite):
    await sleep(2 * random.random())
    num = random.randint(1, 10)
    return fruite.make_fruite(num)


async def take_fruite(fruite):
    potatoes = []
    while True:
        if not potatoes:
            new_potatoes = await produce_random(fruite)
            potatoes.extend(new_potatoes)
        po = potatoes.pop(0)
        print(f'{po.__class__.__name__} {po.potato_id}')




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([take_fruite(Potato), take_fruite(Tomato())]))
