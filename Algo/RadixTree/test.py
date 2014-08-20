
import utils.branch
import utils.leaf

import rtree


### TODO: Insert
rootLeaf = utils.leaf.Leaf()
tLeaf = utils.leaf.Leaf()
slowLeaf = utils.leaf.Leaf()
lyLeaf = utils.leaf.Leaf()
estLeaf = utils.leaf.Leaf()
oastLeaf = utils.leaf.Leaf()
ingLeaf = utils.leaf.Leaf()
erLeaf = utils.leaf.Leaf()

tBranch = utils.branch.Branch(label='t', leaf=tLeaf)
slowBranch = utils.branch.Branch(label='slow', leaf=slowLeaf)
lyBranch = utils.branch.Branch(label='ly', leaf=lyLeaf)
estBranch = utils.branch.Branch(label='est', leaf=estLeaf)
oastBranch = utils.branch.Branch(label='oast', leaf=oastLeaf)
ingBranch = utils.branch.Branch(label='ing', leaf=ingLeaf)
erBranch = utils.branch.Branch(label='er', leaf=erLeaf)

rootLeaf.branches = [tBranch, slowBranch]
tLeaf.branches = [oastBranch, estBranch]
slowLeaf.branches = [lyBranch]
oastLeaf.branches = [ingBranch, erBranch]
### TODO

tree = rtree.RadixTree(root=rootLeaf)
print "Enter strings to lookup: "
while (1):
    print tree.lookup(raw_input())
