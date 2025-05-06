
from collections import deque

def solve(N):
    que = deque(x for x in range(1,N+1))

    while que:
        if len(que) == 1:
            return que[0]
        que.popleft() # drop
        que.append(que.popleft()) # rotate
    return 0

N = int(input().strip())
print(solve(N))
