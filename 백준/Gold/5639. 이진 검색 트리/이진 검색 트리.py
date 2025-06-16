
from dataclasses import dataclass
from typing import Optional
from collections import deque
import sys

input = sys.stdin.readline

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
