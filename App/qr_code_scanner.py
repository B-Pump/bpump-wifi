from pyzbar.pyzbar import decode
from PIL import Image
import os

image_path = "data/qr_code.png"

if os.path.exists(image_path):
    for obj in decode(Image.open(image_path)):
        print("Decoded QR Code:", obj.data.decode("utf-8"))
else:
    print("Image not found")