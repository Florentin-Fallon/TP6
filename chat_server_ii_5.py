import asyncio

CLIENTS = {}

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')  # Récupère l'adresse du client (IP, port)
    
    # Vérifie si le client est déjà dans CLIENTS
    if addr not in CLIENTS:
        data = await reader.read(100)
        message = data.decode()
        
        # Vérifie que le message commence par "Hello|"
        if message.startswith("Hello|"):
            pseudo = message.split("|")[1]
            
            # Ajoute le client à la liste CLIENTS avec son pseudo
            CLIENTS[addr] = {"r": reader, "w": writer, "pseudo": pseudo}
            
            # Annonce à tous les clients que le nouveau client a rejoint la chatroom
            announcement = f"Annonce: {pseudo} a rejoint la chatroom"
            for client_addr, client_data in CLIENTS.items():
                if client_addr != addr:
                    client_writer = client_data["w"]
                    client_writer.write(announcement.encode())
                    await client_writer.drain()

    try:
        while True:
            data = await reader.read(100)
            message = data.decode()
            
            # Si le client a fermé la connexion, le retirer de CLIENTS
            if not data:
                break
            
            # Récupère le pseudo du client
            pseudo = CLIENTS[addr]["pseudo"]

            print(f"{pseudo}a dit : {message}")
            
            # Envoie le message à tous les autres clients avec le pseudo du client émetteur
            for client_addr, client_data in CLIENTS.items():
                if client_addr != addr:
                    client_writer = client_data["w"]
                    client_writer.write(f"{pseudo}a dit : {message}".encode())
                    await client_writer.drain()
            
    except asyncio.CancelledError:
        pass
    finally:
        # Ferme la connexion et retire le client de CLIENTS
        print(f"ANNONCE :{pseudo} a quitté la chatroom")
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
