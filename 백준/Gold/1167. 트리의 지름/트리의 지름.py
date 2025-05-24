
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
graph = defaultdict(list)

for _ in range(N):
    arr = list(map(int, input().split()))
    n1 = arr[0]
    for k in range(1, len(arr), 2):
        if arr[k] == -1: break
        n2, w = arr[k], arr[k+1]
        graph[n1].append((n2, w))
        # graph[n2].append((n1, w))

def solve()->int:
    #
    def find_edge(root):
        far_node, max_dist = 0, 0

        stack = [(root,0)]
        visited = set([root])

        while stack:
            n1,dist = stack.pop()
            if dist > max_dist:
                far_node,max_dist = n1,dist
            for n2,w in graph[n1]:
                if n2 in visited: continue
                stack.append((n2, dist+w))
                visited.add(n2)

        return (far_node, max_dist)

    start = 1
    edge1,_ = find_edge(start)
    edge2,dist = find_edge(edge1)

    return dist

if N <= 1:
    print(0)
else:
    print(solve())
