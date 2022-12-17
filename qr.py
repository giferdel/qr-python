import qrcode

link = 'https://linktr.ee/giferdel'
qr = qrcode.QRCode(version=2,box_size=20,border=5)
qr.add_data(link)
qr.make(fit=True)

img=qr.make_image(fill='black',back_color='red')
img.save('qr.png')

