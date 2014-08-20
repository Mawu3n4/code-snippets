

class Node(object):
    def __init__(self, *args, **kwargs):
        super(Node, self).__init__()
        self.label = kwargs.get('label', None)
