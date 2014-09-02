import sys
import math

def convert(nb):
    return float(nb) if '.' in nb else int(nb)

x, y = raw_input('Starting point (X, Y) ?: ').split(' ')
x = convert(x)
y = convert(y)

def translate(*args, **kwargs):
    a, b, = args[0]
    return (x+convert(a), y+convert(b))

def reflect(*args, **kwargs):
    axis, = args[0]
    return (x * -1 if axis.lower() == 'x' else x,
            y * -1 if axis.lower() == 'y' else y)

def rotate(*args, **kwargs):
    a, b, c, = args[0]
    cos = math.cos(convert(c))
    sin = math.sin(convert(c))
    a = convert(a)
    b = convert(b)
    return (cos * (x - a) - sin * (y - b) + a,
            sin * (x - a) + cos * (y - b) + b)

def scale(*args, **kwargs):
    a, b, c, = args[0]
    a = convert(a)
    b = convert(b)
    c = convert(c)
    return (abs((x - a) * c) + a, abs((y - b) * c) + b)

def finish(*args, **kwargs):
    sys.exit(0)

def show(*args, **kwargs):
    print (x, y)
    return x ,y

commands = {'translate': 'A B',
            'rotate': 'X|Y',
            'reflect': 'A B C',
            'scale': 'A B C',
            'show': '',
            'finish': ''}

while True:
    command = raw_input('$ ').split(' ')
    if len(command) and command[0] in commands:
        x, y = globals()[command[0]](command[1:])
    else:
        print 'Unknown command:'
        print '\n'.join(['    {0} {1}'.format(key, commands[key])
                         for key in commands])
