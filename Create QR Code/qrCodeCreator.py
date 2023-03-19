# import qrcode
# img = qrcode.make('https://www.instagram.com/dev.abdallah.it/?r=nametag')
# img.save("test.png")


# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('https://www.instagram.com/dev.abdallah.it')
# img = qr.make_image(fill_color="black", back_color="white")
# img.save('instaProfile.png')


# import io
# import qrcode
# qr = qrcode.QRCode()
# qr.add_data("https://www.instagram.com/dev.abdallah.it/?r=nametag")
# qr.make_image(fill_color="green", back_color="black")
# f = io.StringIO()
# qr.print_ascii(out=f)
# f.seek(0)
# print(f.read())
