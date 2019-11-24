import asyncio
from contextlib import asynccontextmanager


class Conn:
    async def query(self, statement):
        print(statement)


conn = Conn()


async def acquire_db_connection():
    print('acquire')
    return conn


async def release_db_connection(conn):
    print('release')
    return conn


@asynccontextmanager
async def get_connection():
    conn = await acquire_db_connection()
    try:
        yield conn
    finally:
        await release_db_connection(conn)


async def get_all_users():
    async with get_connection() as conn:
        return await conn.query('SELECT ...')


if __name__ == '__main__':
    asyncio.run(get_all_users())