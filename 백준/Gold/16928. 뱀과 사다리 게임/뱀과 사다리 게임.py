from collections import deque
import sys
input = sys.stdin.readline

NODES = 100 # number of nodes
START,END = 1,100


def solve(path:list)->int:
    # path: quick path list, via ladder or snake
    #
    graph = [[] for i in range(NODES+1)]
    # graph[0] is not used.
    for n in range(1,NODES+1):
        graph[n] = [ k for k in range(n+1,min(n+7,NODES+1)) ]

    # use bfs
    que = deque()
    stat = [ 0 for i in range(NODES+1) ]
    #   stat[k]: 노드 k 까지 이동하는데 걸린 횟수 (주사위 굴린 횟수)
    #            <0 if not visited

    que.append(START)
    stat[START] = 0

    while que:
        node = que.popleft()
        count = stat[node]

        if node == END:
            return count

        for nxt in graph[node]:
            # nxt is next node using dice. usually node+1 ~ +6
            # assume nxt is in valid range. 1<=nxt<=NODES
            if path[nxt] > 0:
                nxt = path[nxt]
            if stat[nxt] > 0: continue

            que.append(nxt)
            stat[nxt] = count+1

    return -1



N,M = map(int, input().split())

path = [0 for i in range(NODES+1)]
# path[0] is not used.

for _ in range(N): # ladder
    s,e = map(int, input().split())
    assert s<e and 1<=s<=NODES and 1<=e<=NODES
    path[s] = e
for _ in range(M): # snake
    s,e = map(int, input().split())
    assert s>e and 1<=s<=NODES and 1<=e<=NODES
    path[s] = e

print(solve(path))
