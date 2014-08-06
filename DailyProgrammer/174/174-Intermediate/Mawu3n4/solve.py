import hashlib
from PIL import Image, ImageDraw

print "Username: ",
username = raw_input()
# Easy seed
seed = hashlib.sha256(username).hexdigest()
seed += seed

img = Image.new('RGB', (320, 320), "white")

pen = ImageDraw.Draw(img)
pixels = img.load()

def genSquare(color, seed, size):
    x = 0
    y = 0
    for c in seed:
        if 52 < ord(c) < 100: pen.rectangle(((x, y), (x+size, y+size)), fill=color)
        x = 0 if x >= img.size[0]/2 - size else x + size
        y = y + size if x == 0 else y

genSquare((150, 75, 0), seed, 40)
genSquare((250, 250, 0), seed[::-1], 40)

# Vertical Symmetry
for i in range(img.size[0]/2):
    for j in range(img.size[1]):
        pixels[img.size[0]/2+i, j] = pixels[img.size[0]/2-i, j]

img.save(username + "-out.png", "PNG")

