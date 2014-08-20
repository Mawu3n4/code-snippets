

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
