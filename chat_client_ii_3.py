import asyncio
from aioconsole import ainput

async def user_input(writer):
    while True:
        user_message = await ainput("Votre message: ")
        writer.write(user_message.encode())
        await writer.drain()

async def receive_messages(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        print(f"Message reçu du serveur: {data.decode()}")

async def main():
    reader, writer = await asyncio.open_connection(host="127.0.0.1", port=8888)

    try:
        await asyncio.gather(
            user_input(writer),
            receive_messages(reader)
        )
    except asyncio.CancelledError:
        pass
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
