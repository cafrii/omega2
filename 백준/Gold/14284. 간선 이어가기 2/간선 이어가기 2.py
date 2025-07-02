
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

INF = 500001  # 5000 * 100 + 1

def solve(graph:list[list[tuple[int,int]]], s:int, t:int)->int:
    '''
    '''
    N = len(graph)-1
    mincost = [INF] * (N+1)
    que = []
    # element: (cost, node)
    heappush(que, (0, s))
    mincost[s] = 0

    while que:
        cost,now = heappop(que)
        if now == t:
            return cost
        if cost > mincost[now]: # during queued, there was visit
            continue

        for nxt,lc in graph[now]:
            # nxt: next node, lc: link cost
            if cost + lc >= mincost[nxt]: continue
            heappush(que, (cost+lc, nxt))
            mincost[nxt] = cost+lc

    return -1 # we cannot reach the goal


N,M = map(int, input().split())
graph = [[] for k in range(N+1)]
# node-0 is not used. ie, graph[0] is always [].
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s,t = map(int, input().split())

print(solve(graph, s, t))
