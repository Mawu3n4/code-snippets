import heapq


def check_bounds(size):
    def _check_bounds(node):
        (x, y) = node
        return 0 <= x < size and 0 <= y < size
    return _check_bounds


def get_knight_moves(node, size, end=None):
    (x, y) = node
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]
    return filter(check_bounds(size), map(lambda mv: (x+mv[0], y+mv[1]), moves))


def get_bishop_moves(node, size, end):
    (x, y) = node
    (end_x, end_y) = end
    x_step = 1 if x < end_x else -1
    y_step = 1 if y < end_y else -1
    while 0 <= x + x_step < size and 0 <= y + y_step < size:
        x += x_step
        y += y_step
        yield (x, y)


MOVES = {
    'bishop': get_bishop_moves,
    'knight': get_knight_moves
}


class HeapQueue:
    def __init__(self):
        self.nodes = []

    def push(self, node, priority):
        heapq.heappush(self.nodes, (priority, node))

    def pop(self):
        return heapq.heappop(self.nodes)[1]

    def empty(self):
        return not len(self.nodes)


def astar(start, end, size, piece_name):
    path = HeapQueue()
    path.push(start, 0)
    visited = {start: None}
    costs = {start: 0}

    while not path.empty():
        curr = path.pop()

        if curr == end:
            break

        for node in MOVES[piece_name](curr, size, end):
            new_cost = costs[curr] + 1
            if node not in costs or new_cost < costs[node]:
                path.push(node, new_cost)
                visited[node] = curr
                costs[node] = new_cost

    return visited


def reconstructPath(visited, start, end):
    curr = end
    path = [curr]

    while start not in path:
        if curr not in visited:
            print('{} is unaccessible by a {} from {}'.format(
                curr, piece, start
            ))
            return [start]
        curr = visited[curr]
        path.append(curr)

    return path

size = int(raw_input('Size? (int): '))
start = tuple(map(int, raw_input('Start? (int int): ').split(' ')))
end = tuple(map(int, raw_input('End?(int int): ').split(' ')))
piece = raw_input('Piece? {}: '.format(MOVES.keys()))

grid = []
for i in range(size):
    grid.append(['_']*size)
path = reconstructPath(astar(start, end, size, piece), start, end)
for i, node in enumerate(path):
    grid[node[0]][node[1]] = str(len(path) - i)
print('')
print('\n'.join('|'.join(row) for row in grid))
