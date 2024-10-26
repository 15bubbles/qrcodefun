import qrcode
import qrcode.constants


def generate_mecard_qr(
    first_name: str,
    last_name:str,
    email: str,
    telephone_number: str,
    output: str = "mecard_qrcode.png",
) -> None:
    data = (
        f"MECARD:"
        f"N:{last_name},{first_name};"
        f"EMAIL:{email};"
        f"TEL:{telephone_number};;"
    )

    qr = qrcode.QRCode(
        version=1,
        error_code=qrcode.constants.ERROR_CORRECT_L,
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
