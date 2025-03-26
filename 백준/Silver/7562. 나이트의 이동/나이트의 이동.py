
from collections import deque

def solve(sz:int, s:tuple[int,int], e:tuple[int,int]):
    '''
    sz: size of board (w, h)
    s: staring point (y, x)
    e: goal point (y, x)
    return: minimum number of walked
    '''

    que = deque()
    que.append((s, 0))
    visited = [ [0]*sz for _ in range(sz) ]

    while que:
        (y,x),walked = que.popleft()
        if (y,x) == e:
            return walked

        deltas = [ (-1,-2),(-2,-1),(-2,1),(-1,2),
                   (1,-2),(2,-1),(2,1),(1,2) ]
        for d in deltas:
            y2,x2 = y+d[0],x+d[1]
            if (not 0 <= y2 < sz) or (not 0 <= x2 < sz):
                continue
            if visited[y2][x2]:
                continue
            que.append(((y2,x2), walked+1))
            visited[y2][x2] = 1

    return -1 # cannot reach to goal!

MIN_L,MAX_L = 4,300

T = int(input().strip())
for _ in range(T):
    L = int(input().strip())
    if (not MIN_L <= L <= MAX_L):
        break # wrong input
    s = tuple(map(int, input().split()))
    e = tuple(map(int, input().split()))
    print(solve(L, s, e))
