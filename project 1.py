import image
import qrcode
qr=qrcode.QRCode(
   version=10,
   box_size=5,
   border=3
)

data=input("Enter Designation of QR code: ")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save(input("Name of QR code: ")+".png")