
from collections import deque
import sys
input = sys.stdin.readline

def solve(box:list[list])->int:
    N,M = len(box), len(box[0])

    visited = [ [ -1 for c in range(M) ] for r in range(N) ]
    # days when the tomato in the cell is matured
    # -1 if not visited

    que = deque()  # element: tuple (row, col)
    # 시작 상태의 모든 익은 토마토를 큐에 넣기
    for r in range(N):
        for c in range(M):
            if box[r][c] == 1:
                que.append((r,c))
                visited[r][c] = 0 # matured at day 0

    deltas = [(-1,0), (1,0), (0,-1), (0,1)]
    d = -1
    while que:
        y,x = que.popleft()
        d = visited[y][x]

        for dy,dx in deltas:
            ny,nx = y+dy,x+dx
            if not (0<=ny<N and 0<=nx<M):
                continue
            if visited[ny][nx] >= 0: # already matured
                continue
            if box[ny][nx] == -1: # no tomato here
                continue

            que.append((ny,nx))
            visited[ny][nx] = d+1

    # box[][] 가 0 이면서 visited 못한 cell 이 있다면 not-finish!
    if sum(1 if (box[y][x] == 0 and visited[y][x] < 0) else 0
            for y in range(N) for x in range(M)):
        return -1

    return max(max(r) for r in visited)


M,N = map(int, input().split())
# N rows, M columns

box = []
for _ in range(N):
    box.append(list(map(int, input().split())))
    assert len(box[-1]) == M

print(solve(box))
