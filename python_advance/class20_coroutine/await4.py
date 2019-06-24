import asyncio
from time import perf_counter


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')


async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task2
    print('awaited_worker_1')
    await task1
    print('awaited_worker_2')

if __name__ == '__main__':
    t1_start = perf_counter()
    asyncio.run(main())
    t1_stop = perf_counter()
    print("Elapsed time during the whole program in seconds:", t1_stop - t1_start)
