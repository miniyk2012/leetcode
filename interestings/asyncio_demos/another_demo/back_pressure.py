from asyncio import start_server, run


async def on_client_connected(reader, writer):
    while True:
        data = await reader.readline()
        if not data:
            break
        writer.write(data)  # 过多的connect会走到这里, 而这个函数如果想不阻塞, 就得写入缓冲区, 可能造成缓冲溢出, 也就是背压过大


async def server():
    srv = await start_server(on_client_connected, '127.0.0.1', 8888)
    async with srv:
        await srv.serve_forever()


if __name__ == '__main__':
    run(server())
