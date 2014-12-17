import heapq

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

class pQueue:
    def __init__(self):
        self.nodes = []

    def push(self, node, wheight):
        heapq.heappush(self.nodes, (wheight, node))

    def pop(self):
        return heapq.heappop(self.nodes)[1]

    def empty(self):
        return not len(self.nodes)

def pathfinding(grid, start, end):
    path = pQueue()
    path.push(start, 0)

    return path

# inputs = raw_input("Size of the grid, starting position and destination ?:\n").split(' ')
inputs = "10 (0,0) (9,9)".split(' ')
grid = Grid(inputs[0], inputs[0])

grid.walls = [(5, 5)]

def strtotuple(s):
    return tuple([int(x) for x in s.strip('()').split(',')])

pathfinding(grid, strtotuple(inputs[1]), strtotuple(inputs[2]))

print Grid.neighbors(grid, (3, 1))
