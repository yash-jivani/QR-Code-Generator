import qrcode 
import image 
import os.path
import time

print('\n\n\n')
print(r''' 
   ___    ____       ____               _        
  / _ \  |  _ \     / ___|   ___     __| |   ___ 
 | | | | | |_) |   | |      / _ \   / _` |  / _ \
 | |_| | |  _ <    | |___  | (_) | | (_| | |  __/
  \__\_\ |_| \_\    \____|  \___/   \__,_|  \___|
                                                 

''')

qr = qrcode.QRCode(version = 10,box_size=10,border=10)

while True:

    user = input('Enter your link : ')
    file_name = input('Enter your FileName : ')
    qr.add_data(user)
    qr.make(fit=True)
    image = qr.make_image(fill="black",back_color='white')
    image.save( file_name+'.png')
    value = os.path.isfile(file_name+'.png')
    if value==True:
        time.sleep(1)
        print('\nSet Something In Motion...')
        time.sleep(2)
        print('Your QR Code create successfully !\t')
    else:
        print('Something went wrong :( \nPlease Try agine')


    ex = input('\n1) For Create More QR-Codes press Any number: \nq) enter q for exit \n> ')
    if ex=='q':
        print('\nEscape Route\n\n(̅ ◡̅́.̅◡̅̀)̅ \n')
        break
