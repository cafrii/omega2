'''
5639번

이진 검색 트리 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	55482	22113	15656	38.454%

문제
이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.

노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.

전위 순회 (루트-왼쪽-오른쪽)은 루트를 방문하고, 왼쪽 서브트리, 오른쪽 서브 트리를 순서대로 방문하면서 노드의 키를 출력한다.
후위 순회 (왼쪽-오른쪽-루트)는 왼쪽 서브트리, 오른쪽 서브트리, 루트 노드 순서대로 키를 출력한다.
예를 들어, 위의 이진 검색 트리의 전위 순회 결과는 50 30 24 5 28 45 98 52 60 이고, 후위 순회 결과는 5 28 24 45 30 60 52 98 50 이다.

이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

입력
트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다.
모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

출력
입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.


--------

10:52~11:20, 1차. 하지만 timeout 으로 실패.
그 후 cpp 버전으로 pass 한 후 여러 번의 개선 작업..


'''


from dataclasses import dataclass
from typing import Optional
from collections import deque
import sys


input = sys.stdin.readline

# import itertools, sys
#
# def solve_slow(seq:list[int]):
#     '''
#     Args:
#         seq: list of numbers of pre-order tree tranversal.
#     Returns:
#         None
#         re-write postorder traversed result into seq list.
#     '''
#     @dataclass
#     class Node:
#         data: int = 0
#         left: Optional["Node"] = None
#         right: Optional["Node"] = None

#     def add_preorder(tree, data):
#         assert data != tree.data
#         # going deeper down..
#         node = tree
#         while True:
#             if data < node.data:
#                 if not node.left:
#                     node.left = Node(data)
#                     return
#                 node = node.left
#             else: # node.data < data
#                 if not node.right:
#                     node.right = Node(data)
#                     return
#                 node = node.right

#     assert len(seq) > 0 # should not empty
#     root = Node(seq[0]) # consume first element
#     for d in itertools.islice(seq, 1, None): # from second..
#         add_preorder(root, d)

#     idx_out = 0
#     def write_postorder(tree):
#         nonlocal idx_out
#         stack:list[Node|int] = [tree]
#             # list element: node or integer
#         while stack:
#             node = stack.pop()
#             if isinstance(node, int): # this is not Node, but the number to be output.
#                 seq[idx_out] = node
#                 idx_out += 1
#                 continue
#             stack.append(node.data) # append as 'integer' value

#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return
#     write_postorder(root)
#     return



def solve(arr:list[int]):
    '''
    Args:
        arr: list of numbers of pre-order tree tranversal.
    Returns:
        re-write postorder traversed result into arr list.
    '''
    @dataclass
    class Node:
        data: int = 0
        maxlimit: int = int(1e8) # subtree should not exceed this limit.
        left: Optional["Node"] = None
        right: Optional["Node"] = None

    def add_preorder(subtree:Node, que:deque)->bool:
        '''
            지정한 subtree 에 노드들을 최대한 추가한다.
            subtree 는 None 이 아님이 보장되며, subtree.maxlimit 에 의해 추가 가능한 숫자가 한정된다.
            추가할 수 없는 상황이 되면 그냥 리턴한다.
        Args:
            subtree
            que
        Returns:
            true if data is not consumed yet. ie, more data available.
        '''
        # assert data != subtree.data
        if not que:
            return False # no more data
        node = subtree
        if que[0] < node.data:
            if node.left is None:
                node.left = Node(que.popleft(), node.data) # maxlimit=node.data
                more = add_preorder(node.left, que)
                if not more:
                    return False
        # 왼쪽 subtree 에 더 이상 추가할 수 없다면, 오른쪽 subtree 에 시도.
        if node.data < que[0] < node.maxlimit:
            if node.right is None:
                node.right = Node(que.popleft(), node.maxlimit)
                more = add_preorder(node.right, que)
                if not more:
                    return False
        # subtree 에 추가하지 못한 것은 그 상태 그대로 리턴. caller 가 처리해야 함.
        return True

    # 최대 요소 개수가 10000 이고 worst-case depth 를 고려.
    sys.setrecursionlimit(11000)

    assert len(arr) > 0 # should not empty
    que = deque(arr)

    root = Node(que.popleft())
    add_preorder(root, que)

    def write_postorder(tree, arr):
        idx_out = 0
        stack:list[Node|int] = [tree] # list element: node or integer

        while stack:
            node = stack.pop()
            if isinstance(node, int): # this is not Node, but the number to be output.
                arr[idx_out] = node
                idx_out += 1
                continue
            stack.append(node.data) # append as 'integer' value

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return

    write_postorder(root, arr)
    return

#--------
arr = []
while True:
    ln = input().strip()
    if not ln: break  # EOF
    arr.append(int(ln))

solve(arr) # answer will be written back to arr.
for d in arr: print(d)



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
