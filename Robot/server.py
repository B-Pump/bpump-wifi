import socket
import tqdm
import os

SERVER_HOST = "192.168.1.25"
SERVER_PORT = 5001

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

def receive_file(client_socket):
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}...", unit="B", unit_scale=True, unit_divisor=1024)
    
    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))

def main():
    s = socket.socket()

    try:
        s.bind((SERVER_HOST, SERVER_PORT))
        s.listen(5)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

        client_socket, address = s.accept()
        print(f"[+] {address} is connected")

        receive_file(client_socket)

    except Exception as e:
        print(f"[-] Error : {e}")

    finally:
        if 'client_socket' in locals():
            client_socket.close()
            
        s.close()
        print("[*] Server closed")