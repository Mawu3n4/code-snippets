from operator import __add__, __sub__, __mul__, __div__, __pow__
import re

def __builtin_sum(cells, select):
    s = 0.0
    for c in select:
        s += parseExp(cells, getCell(cells, c))
    return s

def __builtin_product(cells, select):
    s = 1.0
    for c in select:
        s *= parseExp(cells, getCell(cells, c))
    return s

def __builtin_average(cells, select):
    return __builtin_sum(cells, select) / len(select)

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

def selectCells(formula):
    cells = formula.split("~")
    if len(cells) > 2:
        print "You can only have maximum one '~' per formula"
        exit()
    select = extractCells(cells[0])
    if len(cells) > 1:
        rm = extractCells(cells[1])
        for i in rm:
            if i in select:
                select.remove(i)
    return select

def getCell(cells, xy):
    if xy not in cells:
        cells[xy] = "0"
    return cells[xy]

def testRegex(rx, f, ops, funcs):
    m = re.match(rx, f)
    if not m:
        return False
    gr = m.groups()
    return funcs[ops.index(gr[1])](parseExp(cells, gr[0]), parseExp(cells, gr[2]))

def parseExp(cells, f):
    if re.match("[0-9]+(\.[0-9]+)?$", f):
        return float(f)
    elif re.match("[A-Z]+[0-9]+$", f):
        return parseExp(cells, getCell(cells, colRowToXY(f)))
    m = re.match("([a-z]+)\(([^\)]+)\)$", f)
    if m:
        if "__builtin_" + m.group(1) in globals():
            return globals()["__builtin_" + m.group(1)](cells, selectCells(m.group(2)))
        else:
            print "Unknown builtin: " + m.group(1)
            return 0
    m = testRegex("(.+)([+-])(.+)$", f, "+-", [__add__, __sub__])
    if m is False:
        m = testRegex("(.+)([*/])(.+)$", f, "*/", [__mul__, __div__])
    if m is False:
        m = testRegex("(.+)([\^])(.+)$", f, "^", [__pow__])
    return (m)

def applyCommand(cells):
    f = raw_input()
    eq = f.split("=")
    if len(eq) == 1:
        print parseExp(cells, getCell(cells, colRowToXY(eq[0])))
    else:
        select = selectCells(eq[0])
        for c in select:
            cells[c] = eq[1]

cells = {}
while True:
    applyCommand(cells)
