import asyncio


async def handle_client(reader, writer):
    while True:
        ip, port = writer.get_extra_info('peername')
        data = await reader.read(1024)
        if not data:
            break
        print(f'Client sent: {data.decode()}')
        writer.write(f'Hello {ip}:{port}\n'.encode())
        await writer.drain()

    writer.close()


async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())