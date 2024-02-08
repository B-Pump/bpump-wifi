import socket

# Définir l'adresse IP et le port du serveur auquel se connecter
SERVER_IP = '192.168.1.100'  # Remplacez ceci par l'adresse IP du serveur
SERVER_PORT = 12345

# Créer un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Établir une connexion avec le serveur
client_socket.connect((SERVER_IP, SERVER_PORT))

# Envoyer des données au serveur
data = "Hello, server!"
client_socket.sendall(data.encode())

# Fermer la connexion avec le serveur
client_socket.close()
