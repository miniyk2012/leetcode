import asyncio
import threading
import time

from concurrent.futures.thread import ThreadPoolExecutor

e = ThreadPoolExecutor()


def worker(index):
    print(index, 'before:', time.time())
    time.sleep(1)
    print(index, 'after:', time.time())
    return index


def main(index):
    loop = asyncio.new_event_loop()
    rv = loop.run_until_complete(loop.run_in_executor(e, worker, index))
    print('Thread', index, 'got result', rv)


if __name__ == '__main__':


    threads = []
    for i in range(5):
        t = threading.Thread(target=main, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
