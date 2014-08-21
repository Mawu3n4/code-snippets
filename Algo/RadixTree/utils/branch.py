
from utils import node

class Branch(node.Node):

    def __init__(self, *args, **kwargs):
        super(Branch, self).__init__(*args, **kwargs)
        self.leaf = kwargs.get('leaf', None)
