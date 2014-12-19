from random import randrange

import collections
import math
import sys

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []

    def walkable(self, node):
        (x, y) = node
        return (0 <= x < self.width
                and 0 <= y < self.height
                and not node in self.obstacles)

    def neighbors(self, node):
        (x, y) = node
        return filter(self.walkable, [(x+xd, y+yd)
                                      for xd in range(-1,2)
                                      for yd in range(-1,2)
                                      if xd or yd])

    def show(self, path=[], space='.', pathc='O', wall='X'):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in path:
                    sys.stdout.write(pathc)
                else:
                    sys.stdout.write(space if self.walkable((x, y)) else wall)
            print ''


class Queue:
    def __init__(self):
        self.nodes = collections.deque()

    def push(self, node):
        self.nodes.append(node)

    def pop(self):
        return self.nodes.popleft()

    def empty(self):
        return not len(self.nodes)

def pathfinding(grid, start, end):
    path = Queue()
    path.push(start)
    visited = {}
    visited[start] = None

    while not path.empty():
        curr = path.pop()

        if curr == end:
            break

        for node in grid.neighbors(curr):
            if not node in visited:
                path.push(node)
                visited[node] = curr

    return visited

def strtotuple(s):
    return tuple([int(x) for x in s.strip('()').split(',')])

def sample(size, percent):
    return int(math.floor(size*percent/100.))

def addObstacles(grid, start, end, well_pop=3, asteroid_pop=6):
    size = grid.width * grid.height

    for n_wells in range(sample(size, 3)):
        x, y = randrange(size), randrange(size)
        neighbors = grid.neighbors((x, y))
        while not grid.walkable((x, y)) or (x, y) in [start, end] or {start, end} & set(neighbors):
            x, y = randrange(size), randrange(size)
            neighbors = grid.neighbors((x, y))
        grid.obstacles.append((x, y))
        grid.obstacles.extend(neighbors)

    for n_asteroids in range(sample(size, 6)):
        x, y = randrange(size), randrange(size)
        while not grid.walkable((x, y)) or (x, y) in [start, end]:
            x, y = randrange(size), randrange(size)
        grid.obstacles.append((x, y))

    grid.obstacles = list(set(grid.obstacles))

def getInput():
    size, start, end = raw_input("Size of the grid, starting position and destination ?:\n").split(' ')
    return int(size), strtotuple(start), strtotuple(end)

def solve():
    size, start, end = getInput()
    grid = Grid(size, size)
    addObstacles(grid, start, end)
    path=pathfinding(grid, start, end)
    reconstructed_path = []
    if end in path:
        curr = path[end]
        while not start in reconstructed_path:
            reconstructed_path.append(curr)
            curr = path[curr]
    else:
        print "No path found."

    grid.show(path=reconstructed_path)


if __name__ == "__main__":
    solve()
