from PIL import Image, ImageShow, ImageFilter

def soma(L):
    return (L + f) % 255

def brilho(L):
    return int(((L / 255) ** f)*255)
    
img = Image.open("sorvete.jpeg")
img = img.convert("YCbCr")
a, b, c = img.split()


a = a.filter(ImageFilter.GaussianBlur(5))

b = b.filter(ImageFilter.GaussianBlur(25))

c = c.filter(ImageFilter.GaussianBlur(50))

img = Image.merge("YCbCr", (a,b,c))
img = img.convert("RGB")
img.save("out.png")
img.show()

