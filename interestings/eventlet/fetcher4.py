"""
定义协程函数 ->（封装成 task->）获取事件循环 -> 将 task 放到事件循环中执行
在封装 task 这一个步骤上加上括号，是因为我们也可以选择直接将协程放到事件循环中，事件循环会自动帮我们完成这一操作。
"""

import asyncio
import functools

import requests


async def scan(url):
    await asyncio.sleep(0.1)
    r = requests.get(url).status_code
    print("{}:{}".format(url, r))
    return r


async def scan2(urls):
    if len(urls) > 0:
        url = urls.pop()
        r = requests.get(url).status_code
        return ("{} :{}".format(url, r))


urls = ['http://www.baidu.com',
        'http://www.taobao.com',
        'https://www.bilibili.com',
        'http://www.google.com']
total = len(urls)
done = 0


def call_back(loop, future):
    global done
    done = done + 1
    print('回调函数，协程返回值为：{},Done:{}'.format(future.result(), done))
    if done < total:
        task = asyncio.ensure_future(scan2(urls))
        task.add_done_callback(functools.partial(call_back, loop))
    else:
        loop.stop()


async def main(loop):
    task = asyncio.ensure_future(scan2(urls))
    task.add_done_callback(functools.partial(call_back, loop))


def demo1():
    task = asyncio.ensure_future(scan('http://www.baidu.com'))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
    print(task.result())


def demo2():
    loop = asyncio.get_event_loop()
    task = loop.create_task(scan('http://www.baidu.com'))  # 封装为task
    loop.run_until_complete(task)
    print(task.result())


def demo3():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scan('http://www.baidu.com'))


def demo4():
    tasks = [asyncio.ensure_future(scan(urls[i])) for i in range(len(urls))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        try:
            print('Task Result:', task.result())
        except Exception as e:
            print(e)


def demo5():
    tasks = [asyncio.ensure_future(scan(urls[i])) for i in range(len(urls))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    for task in tasks:
        print('Task Result:', task.result())


def demo6():
    loop = asyncio.get_event_loop()
    task = loop.create_task(main(loop))
    loop.run_forever()

if __name__ == '__main__':
    demo1()
    demo2()
    demo3()
    print()
    demo4()
    print()
    demo5()
    print('-------------')
    demo6()
