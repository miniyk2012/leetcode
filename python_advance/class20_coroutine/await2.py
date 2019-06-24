import asyncio
from time import perf_counter


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task


if __name__ == '__main__':
    t1_start = perf_counter()
    asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
    t1_stop = perf_counter()
    print("Elapsed time during the whole program in seconds:", t1_stop - t1_start)
