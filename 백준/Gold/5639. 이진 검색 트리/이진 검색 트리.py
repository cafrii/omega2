
from dataclasses import dataclass
from typing import Optional
import itertools, sys

input = sys.stdin.readline


def solve(seq:list[int]):
    '''
    Args:
        seq: list of numbers of pre-order tree tranversal.
    Returns:
        re-write postorder traversed result into seq list.
    '''
    @dataclass
    class Node:
        data: int = 0
        left: Optional["Node"] = None
        right: Optional["Node"] = None

    def add_preorder(tree, data):
        assert data != tree.data
        # going deeper down..
        node = tree
        while True:
            if data < node.data:
                if not node.left:
                    node.left = Node(data)
                    return
                node = node.left
            else: # node.data < data
                if not node.right:
                    node.right = Node(data)
                    return
                node = node.right

    assert len(seq) > 0 # should not empty
    root = Node(seq[0]) # consume first element
    for d in itertools.islice(seq, 1, None): # from second..
        add_preorder(root, d)

    idx_out = 0
    def write_postorder(tree):
        nonlocal idx_out
        stack:list[Node|int] = [tree]
            # list element: node or integer
        while stack:
            node = stack.pop()
            if isinstance(node, int): # this is not Node, but the number to be output.
                seq[idx_out] = node
                idx_out += 1
                continue
            stack.append(node.data) # append as 'integer' value

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return
    write_postorder(root)
    return

#--------
seq = []
while True:
    ln = input().strip()
    if not ln: break  # EOF
    seq.append(int(ln))

solve(seq)
for d in seq:
    print(d)
