import socket
import tqdm
import os
from pyzbar.pyzbar import decode
from PIL import Image
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

def read_qr_code(path):
    if os.path.exists(path):
        for obj in decode(Image.open(path)):
            print("Decoded QR Code:", obj.data.decode("utf-8"))
            return obj.data.decode("utf-8")
    else:
        print("Image not found")

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


with socket.socket() as s:
    host, port = read_qr_code("./data/qr_code.png").split(",", 2)
    print(host)
    print(port)

    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, int(port)))
    print("[+] Connected")

    while True:
        exoselected = str(input(f"""{"="*40}
    1. Pompe
    2. Abdo
{"="*40}
Exo: """))
        s.send(f"exo;{exoselected}".encode())
        
        while True:
            received = s.recv(BUFFER_SIZE).decode()
            title, response = received.split(";")
            if response == "finished":
                print("Exo finished!")
                break
            else:
                print("Wrong!")



    #file = "./App/text.txt"
    #send_file(file)
    #print("[+] Transmission completed")

