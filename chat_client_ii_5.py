import asyncio
import signal
import functools

async def send_message(writer, message):
    writer.write(message.encode())
    await writer.drain()

async def user_input_loop(writer, pseudo):
    try:
        while True:
            message = input("Entre ton message : ")
            if message.lower() == "exit":
                break

            formatted_message = f"{pseudo}|{message}"
            await send_message(writer, formatted_message)
    except asyncio.CancelledError:
        pass

async def receive_messages(reader):
    try:
        while True:
            data = await reader.read(100)
            if not data:
                break

            message = data.decode()
            print(message)
    except asyncio.CancelledError:
        pass

async def main():
    # Saisie du pseudo par l'utilisateur
    pseudo = input("Choisi ton pseudo: ")

    # Connexion au serveur
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    # Envoie du pseudo au serveur
    await send_message(writer, f"Hello|{pseudo} ")

    # Lancement des tâches asynchrones pour la saisie utilisateur et la réception de données
    user_input_task = asyncio.create_task(user_input_loop(writer, pseudo))
    receive_messages_task = asyncio.create_task(receive_messages(reader))

    # Ajout d'un gestionnaire d'événements pour le signal de fermeture du client (Ctrl+C)
    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, functools.partial(handle_client_shutdown, user_input_task, receive_messages_task))

    # Attente de la fin des deux tâches
    await asyncio.gather(user_input_task, receive_messages_task)

    # Fermeture de la connexion
    writer.close()
    await writer.wait_closed()

async def handle_client_shutdown(user_input_task, receive_messages_task, *args):
    print("Déconnexion du serveur. Programme terminé.")
    
    # Annulation des tâches asynchrones du client
    user_input_task.cancel()
    receive_messages_task.cancel()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

