
import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())

map1 = []
goal = None
for y in range(N):
    map1.append(list(map(int, input().split())))

def solve():
    '''
    Globals:
        map1, N, M
    Returns: visited
    '''

    goal = None  # find goal
    for y,m in enumerate(map1):
        try: goal = (y, m.index(2))
        except: pass
    assert goal is not None

    visited = [[-1 for x in range(M)] for y in range(N)]
    # -1: not visited (or cannot reach)
    #  0: goal or wall
    # >0: distance

    # mark wall
    for y in range(N):
        for x in range(M):
            if map1[y][x] == 0:
                visited[y][x] = 0

    que = deque()

    que.append(goal)
    visited[goal[0]][goal[1]] = 0

    delta = [(1,0), (0,1), (-1,0), (0,-1)]

    while que:
        y,x = que.popleft()
        dist = visited[y][x]

        for dy,dx in delta:
            ny,nx = y+dy,x+dx
            if not (0<=ny<N and 0<=nx<M):
                continue
            if map1[y][x] == 0: # it is wall. cannot move.
                continue
            # check it is already visited
            if visited[ny][nx] >= 0:
                continue
            que.append((ny,nx))
            visited[ny][nx] = dist+1

    return visited

ans = solve()
for a in ans:
    print(*a)