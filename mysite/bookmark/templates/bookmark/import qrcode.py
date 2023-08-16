import qrcode

def create_qr_code(data, file_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

if __name__ == "__main__":
    # QR 코드로 만들 데이터
    data_to_encode = "www.skbroadband.com"

    # 저장할 파일 경로와 파일 이름
    file_path = "skbroadband_qr_code.png"

    create_qr_code(data_to_encode, file_path)