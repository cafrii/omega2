

from collections import deque

MAX_NK = 100_000

def solve(N, K):

    if N == K:
        return 0
    if K < N:
        return N-K

    que = deque()
        # element of que is tuple of (node, trace_history).
        # trace history is for debugging purpose only.
        # if memory exceed limit, try with removing it.
    visited = [ 0 ] * (MAX_NK+1)
        # 1 if we visited this node.
        # it is possible that this list contains step count also.
        # however, we are using trace history, so just bool (0 or 1) is enough.

    que.append( (N,[]) )
    visited[N] = 1
    iter_count = 0 # it is also debugging purpuse

    while que:
        v,hist = que.popleft()
        if v == K:
            #log('reached K %d, %s', K, hist)
            return len(hist) # skip first start node

        hist = hist + [ v ]
        iter_count += 1

        # consider next
        for w in [ v-1, v+1, 2*v ]:
            if w < 0 or w > MAX_NK:
                continue
            if visited[w]:
                continue
            visited[w] = 1
            que.append( (w, hist) )

    # cannot reach K
    return -1

N, K = map(int, input().split())
print(solve(N, K))
