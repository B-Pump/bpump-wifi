import socket

SERVER_IP = "192.168.227.135"
SERVER_PORT = 5002

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, SERVER_PORT))

data = "Coucou !!!"
client_socket.sendall(data.encode())

client_socket.close()