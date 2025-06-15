
from typing import Generator
from collections import deque
import sys
input = sys.stdin.readline


def solve(graph:dict, N, K, X)->Generator[int]:
    '''
    output:
        generates answers as individual yield.
    '''
    que = deque()
    dist = [-1] * (N+1)

    que.append(X)
    dist[X] = 0

    while que:
        now = que.popleft()
        if dist[now] == K:
            yield now
            continue
        if dist[now] > K:
            return
        if now not in graph: # no next node
            continue
        for nxt in graph[now]:
            if dist[nxt] >= 0: # already visited
                continue
            que.append(nxt)
            dist[nxt] = dist[now]+1
    # note: yield nothing if no appropriate answer exist.
    return


N,M,K,X = map(int, input().split())

graph = {}
for _ in range(M):
    a,b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

ans = [ k for k in solve(graph, N, K, X) ]
if not ans: ans = [-1]
print('\n'.join( map(str, sorted(ans)) ))
