
from utils.branch import Branch
from utils.leaf import Leaf
from rtree.rtree import RadixTree


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
