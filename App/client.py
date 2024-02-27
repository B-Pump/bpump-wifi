import socket
import tqdm
import os
from pyzbar.pyzbar import decode
from PIL import Image
import os

def read_qr_code(path):
    if os.path.exists(path):
        for obj in decode(Image.open(path)):
            print("Decoded QR Code:", obj.data.decode("utf-8"))
            return obj.data.decode("utf-8")
    else:
        print("Image not found")

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

#host = "192.168.1.25"
#port = 5001



def send_file(filename):
    filesize = os.path.getsize(filename)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    progress = tqdm.tqdm(range(filesize), f"Sending {filename}...", unit="B", unit_scale=True, unit_divisor=1024)

    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            progress.update(len(bytes_read))

# Création de la socket
with socket.socket() as s:
    host, port = read_qr_code("../data/qr_code.png").split(",", 2)
    print(host)
    print(port)

    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, int(port)))
    print("[+] Connected.")

    file = "text.txt"
    send_file(file)


print("[+] Transmission completed")
