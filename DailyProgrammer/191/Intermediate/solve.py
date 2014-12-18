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

def pathfinding(grid, start):
    path = pQueue()
    path.push(start, 0)
    print grid.neighbors(start)
    return path

grid = Grid(10, 10)
grid.walls = [(5, 5)]

pathfinding(grid, (3, 1))
