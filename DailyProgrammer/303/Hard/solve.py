import heapq
import sys


class Grid:
    def __init__(self, data, elements, obstacles):
        self.data = data
        self.obstacles = obstacles
        self.elements = elements
        self.obstacles = obstacles

    def walkable(self, node):
        (x, y) = node
        return self.data[y][x] not in self.obstacles

    def cost(self, node):
        (x, y) = node
        return self.elements[self.data[y][x]]

    def neighbors(self, node):
        (x, y) = node
        return filter(self.walkable, [
            (x+xd, y+yd) for (xd, yd) in [(0, -1), (-1, 0), (0, 1), (1, 0)]])


class pQueue:
    def __init__(self):
        self.nodes = []

    def push(self, node, priority):
        heapq.heappush(self.nodes, (priority, node))

    def pop(self):
        return heapq.heappop(self.nodes)[1]

    def empty(self):
        return not len(self.nodes)


def astar(grid, start, end):
    def manhattan(a, b, d=1):
        return d * (abs(a[0] - b[0]) + abs(a[1] - b[1]))

    path = pQueue()
    path.push(start, 0)
    visited = {start: None}
    costs = {start: 0}

    while not path.empty():
        curr = path.pop()

        if curr == end:
            break

        for node in grid.neighbors(curr):
            new_cost = costs[curr] + grid.cost(node)
            if node not in costs or new_cost < costs[node]:
                path.push(node, new_cost + manhattan(end, node))
                visited[node] = (curr, new_cost)
                costs[node] = new_cost

    return visited


def get_input(fpath, start='S', end='G'):
    maze = []
    start_pos = None
    end_pos = None

    with open(fpath, 'r') as fd:
        for y, line in enumerate(fd.readlines()):
            maze.append(line.strip())
            if start_pos is None or end_pos is None:
                for x, element in enumerate(maze[y]):
                    if element == start:
                        start_pos = (x, y)
                    elif element == end:
                        end_pos = (x, y)

    return maze, start_pos, end_pos


def solve():
    maze, start, end = get_input(sys.argv[1])

    grid = Grid(
        data=maze,
        elements={' ': 1, 'S': 1, 'G': 1, 'm': 11},
        obstacles={'#'})

    path = astar(grid, start, end)

    if path.get(end):
        print('Cost: {}HP'.format(path[end][1]))
    else:
        print "No path found."

if __name__ == "__main__":
    solve()
