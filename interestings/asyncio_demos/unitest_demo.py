"""测试异步函数的方案
来自python源码: https://github.com/python/cpython/blob/master/Lib/test/test_contextlib_async.py"""
import asyncio
import functools
import unittest
from contextlib import asynccontextmanager


def _async_test(func):
    """Decorator to turn an async function into a test case.
    这样就无须在测试用例里面手动触发事件循环了, 可以理解为自动把异步函数给触发运行"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        coro = func(*args, **kwargs)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            return loop.run_until_complete(coro)
        finally:
            loop.close()
            asyncio.set_event_loop(None)

    return wrapper


class AsyncContextManagerTestCase(unittest.TestCase):

    @_async_test
    async def test_contextmanager_plain(self):
        state = []

        @asynccontextmanager
        async def woohoo():
            state.append(1)
            yield 42
            state.append(999)

        async with woohoo() as x:
            self.assertEqual(state, [1])
            self.assertEqual(x, 42)
            state.append(x)
        self.assertEqual(state, [1, 42, 999])

    @_async_test
    async def test_xx(self):
        assert 1 == 5
