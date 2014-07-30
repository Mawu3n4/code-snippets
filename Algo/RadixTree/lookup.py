
import RadixTree as rTree

def lookup(root, search):

    Node curr_node = root
    len_found = 0
    len_search = len(search)

    while (curr_node and not curr_node.isLeaf() and len_found < len_search):
        Child next_node = rTree.getChilds(curr_node, search[len_found:])

        if next_node:
            curr_node = next_node
            len_found += len(curr_node.label)

        else:
            curr_node = null

    return (curr_node and curr_node.isLeaf() and len_found == len_search);
}
