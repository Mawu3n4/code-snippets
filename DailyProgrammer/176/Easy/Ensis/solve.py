import sys
import re

if len(sys.argv) < 2:
    print "Usage: python solve.py <selector>"
    exit()

def colRowToXY(s):
    gr = re.match("([A-Z]+)([0-9]+)", s)
    if not gr:
        print "Error: wrong column-row syntax: " + s
        exit()
    gr = gr.groups()
    x = 0
    for i in range(0, len(gr[0])):
        x = x * 26 + ord(gr[0][i]) - 64
    return (x - 1, int(gr[1]) - 1)

def extractCells(formula):
    cells = []
    for s in formula.split("&"):
        rect = s.split(":")
        p1 = colRowToXY(rect[0])
        if len(rect) == 1:
            if p1 not in cells:
                cells.append(p1)
        elif len(rect) == 2:
            p2 = colRowToXY(rect[1])
            for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                for j in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                    if (i, j) not in cells:
                        cells.append((i, j))
        else:
            print "There should only be 1 or 0 ':' in a subexpression: " + s
    return cells

cells = sys.argv[1].split("~")
if len(cells) > 2:
    print "You can only have maximum one '~' per formula"
    exit()

select = extractCells(cells[0])
if len(cells) > 1:
    rm = extractCells(cells[1])
    for i in rm:
        if i in select:
            select.remove(i)

print len(select)
for i in select:
    print "%d, %d" % i
