from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('D:/MAIN-PYTHON/Python-Projects/08-QR-Code-Encoder-Decoder/myqrcode.png')
result = decode(img)

print(result)