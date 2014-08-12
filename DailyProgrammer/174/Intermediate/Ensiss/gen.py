import hashlib
import sys
import math
from PIL import Image, ImageDraw, ImageColor

def interpolate(a, b, x):
    f = (1 - math.cos(x * 3.1415927)) * .5
    return  a * (1 - f) + b * f

def noise(x, y, seed):
    n = x + y * 57 + seed * 1337
    n = (n << 13) ^ n
    n = (n * (n * n * 15731 + 789221) + 1376312589)
    return (1.0 - (n & 0x7fffffff) / 1073741824.0)

def smoothNoise(x, y, seed):
    corners = (noise(x - 1, y - 1, seed) + noise(x + 1, y - 1, seed) + noise(x - 1, y + 1, seed) + noise(x + 1, y + 1, seed)) / 16
    sides = (noise(x - 1, y, seed) + noise(x + 1, y, seed) + noise(x, y - 1, seed) + noise(x, y + 1, seed)) / 8
    center = noise(x, y, seed) / 4
    return (corners + sides + center)

def interpolatedNoise(x, y, seed):
    ix = int(x)
    iy = int(y)
    fx = x - ix
    fy = y - iy

    v1 = smoothNoise(ix, iy, seed)
    v2 = smoothNoise(ix + 1, iy, seed)
    v3 = smoothNoise(ix, iy + 1, seed)
    v4 = smoothNoise(ix + 1, iy + 1, seed)

    i1 = interpolate(v1 , v2 , fx)
    i2 = interpolate(v3 , v4 , fx)
    return interpolate(i1 , i2 , fy)

def perlinNoise(x, y, persistence, frequency, octaves, seed):
    total = 0
    freq = frequency
    amplitude = 1
    for i in range(octaves):
        total += (interpolatedNoise(x * frequency, y * frequency, seed + i) + 1) * amplitude * .5
        frequency *= 2
        amplitude *= persistence
    return (total)

if len(sys.argv) < 2:
    print "Usage: python gen.py <username>"
    sys.exit()

h = hashlib.md5(sys.argv[1]).digest()
img = Image.new("RGB", (128, 128))
draw = ImageDraw.Draw(img)

for j in range(img.size[1]):
    for i in range(img.size[0] / 2):
        n = int((perlinNoise(i, j, 1, 0.1, 2, ord(h[0])) - .6) * 255)
        if n > 100:
            col = ImageColor.getrgb("hsl(%d, 100%%, 50%%)" % ord(h[1]))
        else:
            col = (0, 0, 0)
        img.putpixel((i, j), col)
        img.putpixel((img.size[0] - i - 1, j), col)

img.save(sys.argv[1] + ".png")
