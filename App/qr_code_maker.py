import qrcode

def generate_qr_code(data):        
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=15, border=2)

    qr.add_data(data)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save("data/qr_code.png")

    print("QR Code generated successfully")

generate_qr_code("example data")