"""`ThreadLocalSingleton` providers example."""

import threading
from queue import Queue

import dependency_injector.providers as providers


def example(example_object, queue):
    """Put provided object in the provided queue."""
    queue.put(example_object)
    queue.put(example_object)


# Create thread-local singleton provider for some object (main thread):
thread_local_object = providers.ThreadLocalSingleton(object)
# thread_local_object = providers.Singleton(object)

# Create singleton provider for thread-safe queue:
queue = providers.Singleton(Queue)

# Create callable provider for example(), inject dependencies:
# 函数的参数通过注入的方式传入, 这样就不用由客户端传参了
# thread_local_object在每个线程中都是隔离的
example = providers.DelegatedCallable(example,
                                      example_object=thread_local_object,
                                      queue=queue)

# Create factory provider for threads that are targeted to execute example():
# example只有在内部运行时才会调用, 而非注入时调用
thread_factory = providers.Factory(threading.Thread,
                                   target=example)


def multi_threads():  # Create 10 threads for concurrent execution of example():
    print('10 threads')
    threads = []
    for thread_number in range(10):
        threads.append(thread_factory(name='Thread{0}'.format(thread_number)))

    # Start execution of all created threads:
    for thread in threads:
        thread.start()

    # Wait while threads would complete their work:
    for thread in threads:
        thread.join()

    # Making some asserts (main thread):
    all_objects = list()

    while not queue().empty():
        all_objects.append(queue().get())

    print(len(all_objects), len(set(all_objects)), len(threads))
    assert len(set(all_objects)) == len(threads)
    # Queue contains same number of objects as number of threads where
    # thread-local singleton provider was used.


def single_thread():
    print('single main thread')
    for _ in range(10):
        example()
        # Making some asserts (main thread):
    all_objects = list()

    while not queue().empty():
        all_objects.append(queue().get())
    print(len(all_objects), len(set(all_objects)))


if __name__ == '__main__':
    multi_threads()
    single_thread()
