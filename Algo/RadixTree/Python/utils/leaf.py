
from utils import node

class Leaf(node.Node):

    def __init__(self, *args, **kwargs):
        super(Leaf, self).__init__(*args, **kwargs)
        self.branches = kwargs.get('branches', [])

    def isEnd(self):
        return False if len(self.branches) else True

    def getNextBranch(self, prefix):
        for branch in self.branches:
            if prefix.startswith(branch.label):
                return branch

        return None
