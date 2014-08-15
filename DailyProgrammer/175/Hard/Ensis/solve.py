import math
from PIL import Image, ImageDraw

def getMirrors():
    mirrors = []
    for i in range(int(raw_input())):
        x1, y1, x2, y2 = [float(i) for i in raw_input().split(" ")]
        mirrors.append([(x1, y1), (x2, y2)])
    return mirrors

def getRay():
    x, y, dx, dy, sz = [float(i) for i in raw_input().split(" ")]
    return [(x, y), normalize(dx, dy), sz]

def dist((x1, y1), (x2, y2)):
    dx, dy = x2 - x1, y2 - y1
    return math.sqrt(dx * dx + dy * dy)

def normalize(x, y):
    sz = dist((0, 0), (x, y))
    return (x / sz, y / sz)

def getCos((x1, y1), (x2, y2)):
    return (x1 * x2 + y1 * y2) / (dist((0, 0), (x1, y1)) * dist((0, 0), (x2, y2)))

def intersect(ray, mirrors):
    (x1, y1), (x2, y2), sz = ray
    x2 += x1
    y2 += y1
    while sz > 0:
        mind = sz
        minm = 0
        minc = (0, 0)
        for m in mirrors:
            (x3, y3), (x4, y4) = m
            denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if not denom:
                continue
            a, b = x1 * y2 - y1 * x2, x3 * y4 - y3 * x4
            x = (a * (x3 - x4) - (x1 - x2) * b) / denom
            y = (a * (y3 - y4) - (y1 - y2) * b) / denom
            d = dist(ray[0], (x, y))
            if (x < min(x3, x4) or x > max(x3, x4) or
                y < min(y3, y4) or y > max(y3, y4) or d > mind):
                continue
            mind = d
            minm = m
            minc = (x, y)
        if minm == 0:
            continue
        print 2 * mind * getCos(ray[1], (x4 - x3, y4 - y3))
        sz -= mind
        sz = 0


sz = 300
im = Image.new("RGB", (sz, sz))
mirrors = getMirrors()
ray = getRay()

intersect(ray, mirrors)

im.save("out.png")
