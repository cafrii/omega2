'''


10:52~11:20 그러나 timeout 실패.

'''


from dataclasses import dataclass
from typing import List, Optional, Generator
import itertools
import sys
import weakref


def solve_timeout(seq:list[int])->Generator[int]:
    '''
    return generator
    '''
    @dataclass
    class Node:
        data: int = 0
        left: Optional["Node"] = None
        right: Optional["Node"] = None

    def add_preorder(tree, data):
        assert data != tree.data
        if data < tree.data:
            if tree.left:
                add_preorder(tree.left, data)
            else:
                tree.left = Node(data)
        else: # tree.data < data
            if tree.right:
                add_preorder(tree.right, data)
            else:
                tree.right = Node(data)

    def gen_postorder(tree):
        if tree.left:
            yield from gen_postorder(tree.left)
        if tree.right:
            yield from gen_postorder(tree.right)
        yield tree.data
        return

    assert len(seq) > 0 # should not empty
    root = Node(seq[0]) # consume first element
    for d in itertools.islice(seq, 1, None): # from second
        add_preorder(root, d)

    yield from gen_postorder(root)
    return


def solve_2(seq:list[int]):
    '''
    it is still slow!
    '''
    @dataclass
    class Node:
        data: int = 0
        left: Optional["Node"] = None
        right: Optional["Node"] = None

    def add_preorder(tree, data):
        assert data != tree.data
        if data < tree.data:
            if tree.left:
                add_preorder(tree.left, data)
            else:
                tree.left = Node(data)
        else: # tree.data < data
            if tree.right:
                add_preorder(tree.right, data)
            else:
                tree.right = Node(data)

    def gen_postorder(tree):
        if tree.left:
            gen_postorder(tree.left)
        if tree.right:
            gen_postorder(tree.right)
        print(tree.data)
        return

    assert len(seq) > 0 # should not empty
    root = Node(seq[0]) # consume first element
    for d in itertools.islice(seq, 1, None): # from second
        add_preorder(root, d)

    gen_postorder(root)
    return



def solve_nonrecursive(seq:list[int]):
    '''
    '''
    @dataclass
    class Node:
        data: int = 0
        left: Optional["Node"] = None
        right: Optional["Node"] = None

    def add_preorder(tree, data):
        assert data != tree.data
        # going down..
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
    for d in itertools.islice(seq, 1, None): # from second
        add_preorder(root, d)

    def print_postorder(tree):
        stack:list[tuple[Node,int]] = [(tree,0)]
            # list element: (node, is_final)
        while stack:
            node,final = stack.pop()
            if final:
                print(node.data)
                continue
            stack.append((node, 1))
            if node.right:
                stack.append((node.right, 0))
            if node.left:
                stack.append((node.left, 0))
        return
    print_postorder(root)
    return


def solve_outputlist(seq:list[int]):
    '''
    '''
    @dataclass
    class Node:
        data: int = 0
        left: Optional["Node"] = None
        right: Optional["Node"] = None

    def add_preorder(tree, data):
        assert data != tree.data
        # going down..
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
    for d in itertools.islice(seq, 1, None): # from second
        add_preorder(root, d)

    idx_out = 0
    def print_postorder(tree):
        nonlocal idx_out
        stack:list[tuple[Node,int]] = [(tree,0)]
            # list element: (node, is_final)
        while stack:
            node,final = stack.pop()
            if final:
                # print(node.data)
                seq[idx_out] = node.data
                idx_out += 1
                continue
            stack.append((node, 1))
            if node.right:
                stack.append((node.right, 0))
            if node.left:
                stack.append((node.left, 0))
        return
    print_postorder(root)
    return


#--------
input = sys.stdin.readline

# max node is 10,000 according to question.
# worst case, tree depth can be 10000.
# sys.setrecursionlimit(11000)

seq = []
while True:
    ln = input().strip()
    if not ln: break  # EOF
    seq.append(int(ln))

solve_outputlist(seq)

# solve_nonrecursive(seq)

# if seq:
#     for d in solve_nonrecursive(seq):
#         print(d)



'''

예제 입력 1
50
30
24
5
28
45
98
52
60
예제 출력 1
5
28
24
45
30
60
52
98
50

run=(python3 5639.py)

echo '50\n30\n24\n5\n28\n45\n98\n52\n60' | $run


export _N=100

(python3 <<EOF
import os
N = int(os.getenv('_N','100'))
for n in range(N,0,-1):
    print(n)
EOF
) | time $run

N=10000 일 때..
$run > /dev/null  5.42s user 0.75s system 99% cpu 6.175 total
5.4 초나 소요되어 실패.

이걸, generator 대신 직접 출력하게 하면..
$run > /dev/null  4.94s user 0.76s system 99% cpu 5.742 total
약간 줄어들긴 하는데..

seq array 에 다시 기록하게 하면?
$run > /dev/null  4.97s user 0.78s system 99% cpu 5.792 total

add 할 때, recursive 대신 loop 로 구현하면?
$run > /dev/null  3.32s user 0.02s system 99% cpu 3.356 total
-> 개선은 되긴 하는데, pass 조건에는 아직 부족.

print 까지 loop 로 구현
->
$run > /dev/null  2.82s user 0.02s system 97% cpu 2.902 total


'''
