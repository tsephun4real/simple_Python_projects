import qrcode

name = input("Enter your name: ")
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
address = input("Enter your address: ")

personal_details = {
    "name": name,
    "date_of_birth": date_of_birth,
    "address": address
}

datails_to_encode = str(personal_details)

qr = qrcode.make(datails_to_encode)

qr.save("personal_details_qr.png")

print("QR code generated and saved as personal_details_qr.png")
