from barcode import EAN13
from barcode.writer import ImageWriter


number = '5901432115697'

barcodeGen = EAN13(number, writer=ImageWriter())
barcodeGen.save("bar-code")
