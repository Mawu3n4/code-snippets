

class Node(object):
    def __init__(self, *args, **kwargs):
        super(Node, self).__init__()
        self.label = kwargs.get('label', None)

class Branch(Node):

    def __init__(self, *args, **kwargs):
        super(Branch, self).__init__(*args, **kwargs)
        self.leaf = kwargs.get('leaf', None)


class Leaf(Node):

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


#TODO: print tree
class RadixTree(object):

    def __init__(self, *args, **kwargs):
        super(RadixTree, self).__init__()
        self.root = kwargs.get('root', None)

    # TODO: lookup(slow) == True, fix insert ?
    def lookup(self, search):

        curr_node = self.root
        len_found = 0
        len_search = len(search)

        while (curr_node and not curr_node.isEnd() and len_found < len_search):
            next_branch = curr_node.getNextBranch(search[len_found:])

            if next_branch:
                curr_node = next_branch.leaf
                len_found += len(next_branch.label)

            else:
                curr_node = None

        return (curr_node and curr_node.isEnd() and len_found == len_search)


### TODO: Insert
rootLeaf = Leaf()
tLeaf = Leaf()
slowLeaf = Leaf()
lyLeaf = Leaf()
estLeaf = Leaf()
oastLeaf = Leaf()
ingLeaf = Leaf()
erLeaf = Leaf()

tBranch = Branch(label='t', leaf=tLeaf)
slowBranch = Branch(label='slow', leaf=slowLeaf)
lyBranch = Branch(label='ly', leaf=lyLeaf)
estBranch = Branch(label='est', leaf=estLeaf)
oastBranch = Branch(label='oast', leaf=oastLeaf)
ingBranch = Branch(label='ing', leaf=ingLeaf)
erBranch = Branch(label='er', leaf=erLeaf)

rootLeaf.branches = [tBranch, slowBranch]
tLeaf.branches = [oastBranch, estBranch]
slowLeaf.branches = [lyBranch]
oastLeaf.branches = [ingBranch, erBranch]
### TODO

tree = RadixTree(root=rootLeaf)
print "Enter strings to lookup: "
while (1):
    print tree.lookup(raw_input())
