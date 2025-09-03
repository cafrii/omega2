

import sys
from collections import deque

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    W = list(map(int, input().split())) # wok sizes
    assert len(W) == M, "wrong wok num"
    return N,W

def solve_bfs(N:int, W:list[int])->int:
    '''
    Args
        N: target num to compose. <= 10_000
        W: list of wok sizes. len <= 100, 1<=w<=N
    '''
    ws = set(W) # wok size set. 단독 사용

    # 웍 두개 조합 사용. 총합 만 중요.
    for j in range(1, len(W)):
        for i in range(j):
            w2 = W[i] + W[j]
            if w2 <= N: ws.add(w2)

    ws = sorted(list(ws), reverse=True)

    INF = max(10_001, N+1)
    dist = [ INF ] * (N+1)
    dist[0] = 0

    que = deque()
    que.extend(ws)
    for w in ws: dist[w] = 1

    if dist[N] < INF: return 1

    while que:
        cur = que.popleft()
        d = dist[cur]

        for w in ws:
            nxt = cur + w
            if nxt == N: dist[N] = d+1; break
            if nxt > N: continue
            if dist[nxt] < INF: continue # already visited
            que.append(nxt)
            dist[nxt] = d + 1

        if dist[N] < INF: break

    return dist[N] if dist[N]<INF else -1


if __name__ == '__main__':
    print(solve_bfs(*get_input()))
