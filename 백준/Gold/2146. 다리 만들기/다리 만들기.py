import sys
from collections import deque

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    return grid

def solve_fast(grid:list[list[int]])->int:
    '''
    1. identify all lands in this country
    2. extending lands to calculate min distance.
    '''
    N = len(grid)
    landmap = [ [0]*N for _ in range(N) ] # our land map
    deltas = [(0,1),(0,-1),(1,0),(-1,0)]
    edge_cells = deque() # (y,x), sea-sided cells

    INF = int(100*100) + 1
    distmap = [ [INF]*N for _ in range(N) ]

    def mark_land(y:int, x:int, land_id:int):
        '''
        (y, x) 에서 시작하여 연결된 모든 셀 탐색하여 id 지정.
        Arguments:
            land_id: identifier of current land. (>0)
        '''
        stack = [(y, x)]
        landmap[y][x] = land_id
        while stack:
            cy,cx = stack.pop()
            seaside = False
            for dy,dx in deltas:
                ny,nx = cy+dy,cx+dx
                if not (0<=ny<N and 0<=nx<N): continue # out of bound
                if grid[ny][nx] == 0: seaside = True; continue # sea
                if landmap[ny][nx] > 0: continue # already identified

                stack.append((ny, nx))
                landmap[ny][nx] = land_id
            if seaside:
                distmap[cy][cx] = 0
                edge_cells.append((cy,cx))
        return

    # 1. 이 나라의 모든 land 를 식별한다.
    num_lands = 0
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 0: continue # sea
            if landmap[y][x] > 0: continue # already identified
            mark_land(y, x, num_lands+1)
            num_lands += 1

    # 2. edge cell 에서부터 영토 확장하여 distance 계산
    que = edge_cells
    min_dist = INF
    prev_dist = -1
    while que:
        cy,cx = que.popleft()
        land_id = landmap[cy][cx]
        dist = distmap[cy][cx]
        if dist != prev_dist:
            # check completion condition
            if min_dist < INF:
                break
            prev_dist = dist

        for dy,dx in deltas:
            ny,nx = cy+dy,cx+dx
            if not (0<=ny<N and 0<=nx<N): continue # out of bound
            if landmap[ny][nx] == land_id: continue # same land
            if landmap[ny][nx] > 0: # we reached to other land!
                min_dist = min(min_dist, dist + distmap[ny][nx])
                # dist 값이 변경되는 시점 까지는 계속 진행해야 함. 더 작은 값이 존재할 수 있음.
                continue
            landmap[ny][nx] = land_id
            que.append((ny, nx))
            distmap[ny][nx] = dist+1
    return min_dist

if __name__ == '__main__':
    m = get_input()
    print(solve_fast(m))
