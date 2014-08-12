from PIL import Image, ImageDraw
import math

def ccw((x1, y1), (x2, y2), (x3, y3)):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def angle((x1, y1), (x2, y2)):
    return (math.atan2(y2 - y1, x2 - x1))

def readPts():
    pts = []
    for i in range(int(raw_input())):
        line = raw_input().split(",")
        pts.append((int(line[0].strip()), int(line[1].strip())))
    return (pts)

pts = sorted(readPts(), key=lambda x:x[0])

ratio = 50
sz = 0.4
img = Image.new("RGB", ((pts[-1][0] + 1) * ratio, (pts[-1][0] + 1) * ratio))
draw = ImageDraw.Draw(img)
for x,y in pts:
    draw.ellipse(((x) * ratio, (y) * ratio, (x + sz) * ratio, (y + sz) * ratio), fill=(255, 255, 255))

hull = [pts[0]]
pts = sorted(pts[1:], key=lambda x:angle(hull[0], x))
hull.append(pts[0])
for pt in pts[1:]:
    while ccw(hull[-2], hull[-1], pt) <= 0:
        hull.pop()
    hull.append(pt)
while ccw(hull[-2], hull[-1], hull[0]) <= 0:
    hull.pop()

for x, y in hull:
    draw.ellipse(((x) * ratio, (y) * ratio, (x + sz) * ratio, (y + sz) * ratio), fill=(255, 0, 0))
img.save("hull.png")
