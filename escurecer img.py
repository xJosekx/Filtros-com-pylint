from PIL import Image
from random import randint

img = Image.open("sorvete.jpeg")
img = img.convert("L")
pix = img.load()
width, height = img.size
for x in range(width):
    for y in range(height):
        pix[x,y] = int(pix[x,y] ** 0.76)

img.show()




