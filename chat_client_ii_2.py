import socket

def main():
    # Créer une socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Adresse et port du serveur
    server_address = ('127.0.0.1', 8888)

    try:
        # Se connecter au serveur
        client_socket.connect(server_address)
        print(f"Connecté au serveur sur {server_address}")

        # Envoyer un message au serveur
        message = "Hello"
        client_socket.sendall(message.encode())
        print(f"Message envoyé au serveur: {message}")

        # Attendre la réponse du serveur
        data = client_socket.recv(1024)
        response = data.decode()
        print(f"Réponse du serveur: {response}")

    finally:
        # Fermer la connexion
        print("Fermeture de la connexion")
        client_socket.close()

if __name__ == "__main__":
    main()
