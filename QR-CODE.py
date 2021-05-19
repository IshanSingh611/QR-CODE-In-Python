#pip install pyqrcode
#QR CODE GENERATOR IN PYTHON
import pyqrcode

string = input("Enter string:  ")
text = pyqrcode.create(string)
text.svg("myQR.svg",scale=8)
print("file saved")