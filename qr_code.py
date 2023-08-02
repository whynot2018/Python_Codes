#
#   PyThon Learning  @Faymaz
#       @programirez
#
# ----   qrcode.py   -----------
# pip install qrcode
import qrcode
from PIL import Image

# The data you want to encode in the QR code
data = "https://faymaz.coox"

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
image = qr.make_image(fill="black", back_color="white")

# Save the  Image
image.save("qr_code.png")
image.open("qr_code.png")
