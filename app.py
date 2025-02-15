
import qrcode
from PIL import Image

def generate_qr(url, file_name):
    if not url:
        print("Error: Please provide a valid URL")
        return
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(file_name)
    print(f"QR code generated successfully and saved as {file_name}")

if __name__ == "__main__":
    url = input("Enter the URL/link: ")
    file_name = input("Enter the file name with extension : ")
    generate_qr(url, file_name)



