import qrcode

from typing import Literal

import qrcode.constants


def generate_wifi_qr(
    ssid: str,
    password: str,
    security_type: Literal["WEP", "WPA", "nopass"],
    output="wifi_qrcode.png",
) -> None:
    data = f"WIFI:S:{ssid};T:{security_type};P:{password};;"
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
