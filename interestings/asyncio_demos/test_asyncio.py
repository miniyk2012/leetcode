import asyncio
import functools
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


@_async_test
async def test_contextmanager_plain():
    state = []

    @asynccontextmanager
    async def woohoo():
        state.append(1)
        yield 42
        state.append(999)

    async with woohoo() as x:
        assert state == [1]
        assert x == 42
        state.append(x)
    assert state == [1, 42, 999]


@_async_test
async def test_xx():
    assert 1 == 5
