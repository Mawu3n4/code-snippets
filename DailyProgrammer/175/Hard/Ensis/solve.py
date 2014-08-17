import math
from PIL import Image, ImageDraw

def getMirrors():
    mirrors = []
    for i in range(int(raw_input())):
        x1, y1, x2, y2 = [float(i) for i in raw_input().split(" ")]
        mirrors.append([(x1, y1), (x2, y2)])
    mirrors.append([(0, 0), (30, 0)])
    mirrors.append([(30, 0), (30, 30)])
    mirrors.append([(30, 30), (0, 30)])
    mirrors.append([(0, 30), (0, 0)])
    return mirrors

def getRay():
    x, y, dx, dy, sz = [float(i) for i in raw_input().split(" ")]
    return [(x, y), normalize(dx, dy), sz]

def dist((x1, y1), (x2, y2)):
    dx, dy = x2 - x1, y2 - y1
    return math.sqrt(dx * dx + dy * dy)

def normalize(x, y):
    sz = dist((0, 0), (x, y))
    if not sz:
        return (x, y)
    return (x / sz, y / sz)

def getCos((x1, y1), (x2, y2)):
    return (x1 * x2 + y1 * y2) / (dist((0, 0), (x1, y1)) * dist((0, 0), (x2, y2)))

def drawLine(draw, p1, p2, col):
    draw.line([(p1[0] * 10, p1[1] * 10), (p2[0] * 10, p2[1] * 10)], fill=col)

def intersect(draw, ray, mirrors):
    (x1, y1), (x2, y2), sz = ray
    x2 += x1
    y2 += y1
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
        if (x < min(x3, x4) - 0.0001 or x > max(x3, x4) + 0.0001 or
            y < min(y3, y4) - 0.0001 or y > max(y3, y4) + 0.0001 or
            d > mind or (x - x1) / (x2 - x1) < 0 or d < 0.0001):
            continue
        mind = d
        minm = m
        minc = (x, y)
    if minm == 0:
        drawLine(draw, ray[0], (x1 + ray[1][0] * ray[2], y1 + ray[1][1] * ray[2]), (255, 0, 0))
        ray[2] = 0
        return
    (x3, y3), (x4, y4) = minm
    coef = 2 * mind * getCos(ray[1], (x4 - x3, y4 - y3))
    vx, vy = normalize(x4 - x3, y4 - y3)
    drawLine(draw, minc, ray[0], (255, 0, 0))
    ray[0] = minc
    ray[1] = normalize((x1 + vx * coef) - minc[0], (y1 + vy * coef) - minc[1])
    ray[2] = sz - mind

sz = 300
im = Image.new("RGB", (sz, sz), (255, 255, 255))
draw = ImageDraw.Draw(im)
mirrors = getMirrors()
ray = getRay()
stx, sty = [i * 10 for i in ray[0]]

for m in mirrors:
    drawLine(draw, m[0], m[1], (0, 0, 0))
draw.ellipse((stx - 3, sty - 3, stx + 3, sty + 3), fill=(0, 0, 255))
while ray[2]:
    intersect(draw, ray, mirrors)

im.save("out.png")
