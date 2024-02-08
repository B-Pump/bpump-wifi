import socket

# Définir l'adresse IP et le port sur lesquels le serveur écoute
IP = '0.0.0.0'  # Vous pouvez remplacer '0.0.0.0' par l'adresse IP de votre appareil
PORT = 12345

# Créer un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à l'adresse et au port spécifiés
server_socket.bind((IP, PORT))

# Ecouter les connexions entrantes
server_socket.listen(1)

print("Le serveur écoute sur {}:{}".format(IP, PORT))

# Accepter la connexion entrante
client_socket, client_address = server_socket.accept()

print("Connexion établie avec", client_address)

# Recevoir des données du client
data = client_socket.recv(1024)

print("Données reçues:", data.decode())

# Fermer la connexion avec le client
client_socket.close()

# Fermer le socket du serveur
server_socket.close()
