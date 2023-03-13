from PIL import Image, ImageOps, ImageFilter

with Image.open("sorvete.jpeg") as img:
    img = img.convert("L")
img = ImageOps.equalize(img)
img = ImageOps.colorize(img, black ="blue", white ="black")

img.save("out.png")
img.show()