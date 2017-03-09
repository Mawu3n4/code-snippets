#!/usr/bin/env python3
from PIL import Image


def function(z):
    return pow(z, 2) - 0.221 - 0.713j


def make_set(width, height):
    h_step = 2.0/(height-1)
    w_step = 2.0/(width-1)
    return [[(i*w_step-1 + 1j*j*h_step-1j)
            for i in range(width)]
            for j in range(height)]


def iterations(z, threshlod):
    i = 0
    while abs(z)<threshold:
        z = function(z)
        i += 1
    return i

if __name__ == '__main__':
    threshold = 2
    width, height = 500, 400
    pixels = make_set(width, height)

    pixels = [list(x) for x in zip(*pixels)]
    pixels = ([list(map(lambda x: iterations(x, threshold), row))
               for row in pixels])
    max_value = max([max(row) for row in pixels])
    print(max_value)
    norm = 255/max_value
    pixels_RGB = [[int(v*norm) for v in row] for row in pixels]
    image = Image.new('L', (width, height))
    px = [item for sublist in pixels for item in sublist]
    print(px[:50])
    image.putdata(px)
    image.show()
