import socket

IP = "192.168.227.135"
PORT = 5002

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(1)

print(f"Le serveur écoute sur {IP}:{PORT}")

client_socket, client_address = server_socket.accept()

print("Connexion établie avec", client_address)

data = client_socket.recv(1024)

print("Données reçues:", data.decode())

client_socket.close()
server_socket.close()