
import sys
input = sys.stdin.readline

from heapq import heappush, heappop

SZ = 501
GOAL = 500

# defined board[][], SZ+1 by SZ+1
board = [ [0 for y in range(SZ+1)] for x in range(SZ+1)]
# 0 for safe region
# 1 for risky region
# 2 for dead region

INF = (SZ * SZ) + 1

def solve():
    '''
    use global board var.
    '''
    min_cost = [ [INF for y in range(SZ+1)] for x in range(SZ+1)]

    que = []
    heappush(que, (0, (0,0)))
    min_cost[0][0] = 0

    delta = [(1,0),(-1,0),(0,1),(0,-1)]

    while que:
        cost,(y,x) = heappop(que)

        if y == GOAL and x == GOAL:
            # push 할 시점과 상황이 달라졌을 수 있으니, cost 대신 min_cost 를 써야 할 것 같음.
            return min_cost[y][x] # cost

        # push 할 시점에는 진행에 의미가 있었지만, 그 사이에 cost가 더 낮아지도록 변경되었을 수도 있으니 한번 더 체크.
        if min_cost[y][x] < cost:
            continue

        for dy,dx in delta:
            ny,nx = y+dy,x+dx # next location
            # check boundness
            if not (0<=ny<=GOAL and 0<=nx<=GOAL): continue
            # check dead region
            if board[ny][nx] == 2: continue
            # get next cost
            nc = (cost + 1) if board[ny][nx]==1 else cost
            # 이미 방문했던 지점인 경우, 더 나아지지 않았다면 재방문 의미 없음.
            if nc >= min_cost[ny][nx]:
                continue
            heappush(que, (nc, (ny,nx)))
            min_cost[ny][nx] = nc

    return -1 # 도달 불가


def fill(y1,x1,y2,x2,mark):
    y1,y2 = min(y1,y2),max(y1,y2)
    x1,x2 = min(x1,x2),max(x1,x2)
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            board[y][x] = mark


N = int(input().strip()) # risky region
for _ in range(N):
    x1,y1,x2,y2 = map(int, input().split())
    fill(x1,y1,x2,y2,1)

M = int(input().strip()) # dead region
for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    fill(x1,y1,x2,y2,2)

print(solve())
