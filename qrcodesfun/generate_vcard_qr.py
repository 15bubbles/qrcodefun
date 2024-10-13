import qrcode
import datetime


def generate_vcard_qr(
    first_name: str,
    last_name: str,
    email: str,
    telephone_number: str,
    output: str = "vcard_qrcode.png",
) -> None:
    data = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name};;;
FN:{first_name} {last_name}
EMAIL;type=PERSONAL,INTERNET:{email}
TEL;type=CELL:{telephone_number}
END:VCARD"""

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make()

    image = qr.make_image(
        fill_color="black",
        back_color="white",
    )

    image.save(output)
