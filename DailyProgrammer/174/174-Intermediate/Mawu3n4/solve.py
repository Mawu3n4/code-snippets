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

def genSquare(color, seed):
    x = 0
    y = 0
    for c in seed:
        if 52 < ord(c) < 100: pen.rectangle(((x, y), (x+20, y+20)), fill=color)
        x = 0 if x >= 320/2 - 20 else x + 20
        y = y + 20 if x == 0 else y

genSquare((150, 75, 0), seed)
genSquare((250, 250, 0), seed[::-1])

# Vertical Symmetry
for i in range(160):
    for j in range(320):
        pixels[160+i, j] = pixels[160-i, j]

img.save(username + "-out.png", "PNG")

