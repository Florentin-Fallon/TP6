import asyncio

async def handle(reader, writer):
    # Récupérer les informations sur le client
    client_addr = writer.get_extra_info('peername')
    print(f"Client connected from {client_addr}")

    while True:
        # Lire le message du client
        data = await reader.read(1024)
        if not data:
            break

        message_from_client = data.decode()
        print(f"Message received from {client_addr[0]}:{client_addr[1]}: {message_from_client}")

    # Fermer la connexion lorsque le client se déconnecte
    print(f"Client {client_addr[0]}:{client_addr[1]} disconnected.")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle, '127.0.0.1', 8888
    )

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    try:
        while True:
            await asyncio.sleep(1)  # Keep the event loop running
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        await server.wait_closed()

# Lancer le serveur
asyncio.run(main())
