
from collections import deque
import sys
input = sys.stdin.readline


def solve(box:list[list[list]])->int:
    H,N,M = len(box),len(box[0]),len(box[0][0])

    stat = [ [ [ -1 for m in range(M) ] for n in range(N) ] for h in range(H) ]
    # -1: not visit
    # >=0: the day when tomato in the cell matured

    maxdays = -1
    que = deque() # (h,y,x)

    # add initially matured tomatos
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 1:
                    que.append((h,n,m))
                    stat[h][n][m] = 0
                    maxdays = 0

    deltas = [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)]

    while que:
        z,y,x = que.popleft()
        day = stat[z][y][x]

        for dz,dy,dx in deltas:
            nz,ny,nx = z+dz,y+dy,x+dx # next of z/y/x

            # boundary check
            if not (0<=nz<H and 0<=ny<N and 0<=nx<M): continue
            # already visit?
            if stat[nz][ny][nx] >= 0: continue
            # no tomato or already matured?
            if box[nz][ny][nx] != 0: continue

            que.append((nz,ny,nx))
            stat[nz][ny][nx] = day+1
            maxdays = max(maxdays, day+1)

    # check if all tomato matured
    num_unmatured = sum( (1 if stat[z][y][x] == -1 else 0)
        for z in range(H) for y in range(N) for x in range(M) if box[z][y][x] >= 0)
    if num_unmatured:
        return -1
    return maxdays


M,N,H = map(int, input().split())

box = [ ]
for h in range(H):
    plane = []
    for n in range(N):
        plane.append(list(map(int, input().split())))
        assert len(plane[-1]) == M
    box.append(plane)

print(solve(box))

