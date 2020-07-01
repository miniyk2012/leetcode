import asyncio

import aiohttp

host_to_access = {'www.baidu.com', 'www.taobao.com', 'www.tencent.com', 'www.toutiao.com', 'www.meituan.com',
                  'www.tmall.com'}

loop = asyncio.get_event_loop()


async def fetch(url):
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.get(url) as response:
            response = await response.read()
            print('{} response:{}'.format(url, response))
            return response


if __name__ == '__main__':
    tasks = [fetch('http://' + host + '/') for host in host_to_access]
    loop.run_until_complete(asyncio.gather(*tasks))
