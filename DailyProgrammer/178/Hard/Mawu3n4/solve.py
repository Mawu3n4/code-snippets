
# [13][24][^1][^2][^3][^4]
# (.)\1..\1
# .*1.*
# .*(12|23|34).*
# .*(?:13|31)(.*)

from PIL import Image
import time
import re

size = int(raw_input('Image size ?: '))
pattern = raw_input('Regexp ?: ').strip()

def fill(data, x, y, end_x, end_y, value):
    if (x+1) == end_x:
        if re.compile(pattern).search(value):
            data[x, y] = (0, 0, 0)
    else:
        fill(data, (x + end_x)>>1, y, end_x, (y + end_y)>>1, value + "1")
        fill(data, x, y, (x + end_x)>>1, (y + end_y)>>1, value + "2")
        fill(data, x, (y + end_y)>>1, (x + end_x)>>1, end_y, value + "3")
        fill(data, (x + end_x)>>1, (y + end_y)>>1, end_x, end_y, value + "4")

img = Image.new("RGB", (size, size), "white")
fill(img.load(), 0, 0, size, size, "")
img.save("out.png")

