import sys
from numpy.random import choice
import numpy
from PIL import Image


def parse_file(filename):
    """ Format of ITF equations files
    size
    iterations
    A0 B0 C0 D0 E0 F0 p0
    A1 B1 C1 D1 E1 F1 p1
    ...
    An Bn Cn Dn En Fn pn
    """
    with open(sys.argv[1], 'r') as fd:
        itf_set = [map(float, line.split(' ')) for line in fd.readlines()]
        size = int(itf_set.pop(0)[0])
        iterations = int(itf_set.pop(0)[0])
        probabilities = [eq.pop(-1) for eq in itf_set]
        itf_set = numpy.array(itf_set)

    return itf_set, probabilities, iterations, size


def generate(itf_set, probabilities=None, iterations=5000, size=1):
    x, y = (1, 1)
    box = [0, 0, 0, 0]
    points = [(x, y)]
    for i in range(iterations):
        a, b, c, d, e, f = itf_set[
            choice(
                range(itf_set.shape[0]),
                p=probabilities)]
        x, y = a*x + b*y + e, c*x + d*y + f
        box = [
            x*size if x*size < box[0] else box[0],
            x*size if x*size > box[1] else box[1],
            y*size if y*size < box[2] else box[2],
            y*size if y*size > box[3] else box[3],
        ]
        points.append((x*size, y*size))

    return points, box


def main():
    filename = sys.argv[1]
    itf_set, probabilities, iterations, size = parse_file(filename)

    points, box = generate(
        itf_set,
        probabilities=probabilities,
        iterations=iterations,
        size=size)

    width = int(abs(box[0]) + abs(box[1]))
    height = int(abs(box[2]) + abs(box[3]))

    origin = (width - box[1], height-box[3])

    img = Image.new(
        'RGB', (width+2, height+2), "black")
    print(img.size)
    pixels = img.load()
    for x, y in points:
        px = origin[0] + x
        py = origin[1] + y
        pixels[px, py] = (int(px), int(py), 100)

    img.show()


if __name__ == '__main__':
    main()


