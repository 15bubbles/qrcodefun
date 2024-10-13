import qrcode

qr = qrcode.QRCode()
qr.add_data("Some text")
qr.print_ascii()
