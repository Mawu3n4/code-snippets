NODES = {}


def isodd(n):
    return n % 2


def iseven(n):
    return not isodd(n)


class Algae(object):
    def __init__(self, size):
        self.limit = size
        self.nodes = {}

    def build(self):
        for n in range(2, self.limit):
            self.add_branch(n)

    def empty_node(self):
        return {'child': None, 'parents': set(), 'neighbor': None}

    def add_branch(self, n):
        if n not in self.nodes:
            self.nodes[n] = self.empty_node()

        previous = n
        while n != 1:
            if iseven(n):
                n = n / 2
            else:
                n = 3 * n + 1

            if n not in self.nodes:
                self.nodes[n] = self.empty_node()

            if iseven(previous):
                self.nodes[previous]['child'] = n
                self.nodes[n]['parents'].add(previous)
            else:
                self.nodes[previous]['neighbor'] = n
                self.nodes[n]['neighbor'] = previous

            if (
                    self.nodes[previous]['neighbor'] is not None and
                    self.nodes[previous]['neighbor'] != n
            ):
                self.nodes[self.nodes[previous]['neighbor']]['child'] = n
                self.nodes[n]['parents'].add(self.nodes[previous]['neighbor'])

            previous = n


def conjecture(n):
    while n != 1:
        yield n

        if iseven(n):
            n = n / 2
        else:
            n = 3 * n + 1
