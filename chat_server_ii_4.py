import asyncio

CLIENTS = {}

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')  # Récupère l'adresse du client (IP, port)
    
    # Vérifie si le client est déjà dans CLIENTS
    if addr in CLIENTS:
        print(f"Client {addr} is already connected. Ignoring.")
        return
    
    print(f"Nouvelle connection via {addr}")
    
    # Ajoute le client à la liste CLIENTS
    CLIENTS[addr] = {}
    CLIENTS[addr]["r"] = reader
    CLIENTS[addr]["w"] = writer
    
    try:
        while True:
            data = await reader.read(100)
            message = data.decode()
            
            # Si le client a fermé la connexion, le retirer de CLIENTS
            if not data:
                break
            
            print(f"{addr} a dit : {message}")
            
            # Envoie le message à tous les autres clients
            for client_addr, client_data in CLIENTS.items():
                if client_addr != addr:
                    client_writer = client_data["w"]
                    client_writer.write(f"{addr[0]}:{addr[1]} said: {message}".encode())
                    await client_writer.drain()
            
    except asyncio.CancelledError:
        pass
    finally:
        # Ferme la connexion et retire le client de CLIENTS
        print(f"{addr} a quitter le chat.")
        del CLIENTS[addr]
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)
    
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
