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

image_path = "../data/qr_code.png"
read_qr_code(image_path)