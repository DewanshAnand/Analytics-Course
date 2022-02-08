import pyqrcode
import png

def qr_code():
    s='This is POWER python class'
    d=pyqrcode.create(s)
    d.png('my_img.png',scale=6)
    print('Code Executed Properly')

if __name__ == '__main__':
    qr_code()