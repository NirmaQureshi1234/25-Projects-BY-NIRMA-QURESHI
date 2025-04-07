import qrcode 

data = 'Don\'t forget to subscribe!'

img = qrcode.make(data)


qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('D:/MAIN-PYTHON/Python-Projects/08-QR-Code-Encoder-Decoder/myqrcode.png')