import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())

tree = defaultdict(list)
# tree[node1]: [ (node2, weight), ... ]

for _ in range(N-1):
    p,c,w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))


def solve() -> int:

    def find_edge(root:int):
        stack = [(root, 0)] # (node, dist_from_root)
        visited = set([root])
        edge,max_dist = -1,0
        while stack:
            n,dist = stack.pop()
            if dist > max_dist:
                edge,max_dist = n,dist
            if n not in tree:
                continue
            for c,w in tree[n]:
                if c in visited: continue
                stack.append((c, dist+w))
                visited.add(c)
        return (edge,max_dist)

    # 어떤 노드부터 시작하더라도 상관 없음.
    start = next(iter(tree.keys()))
    edge1,_ = find_edge(start)
    edge2,dist = find_edge(edge1)

    return dist

if N <= 1:
    print(0)
else:
    print(solve())

