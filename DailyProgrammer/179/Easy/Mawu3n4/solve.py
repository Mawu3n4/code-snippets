from PIL import Image

im = Image.open(raw_input('Path to the image to convert?: '))
data = im.load()

def RGBtoGrayScale(r, g, b):
    g = (max(r, g, b) + min(r, g, b)) >> 1
    return (g, g, g)

for x in range(im.size[0]):
    for y in range(im.size[1]):
        data[x,y] = RGBtoGrayScale(*data[x, y])

im.show()
