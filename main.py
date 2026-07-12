import qrcode

def generate_qr():
    data = input("Enter URL or Text: ")

    img = qrcode.make(data)
    img.save("qrcode.png")

    print("QR Code Created Successfully!")
    print("Saved as: qrcode.png")


if __name__ == "__main__":
    generate_qr()
