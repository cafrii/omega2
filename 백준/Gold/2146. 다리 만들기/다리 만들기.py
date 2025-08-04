import sys
from collections import deque

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
        assert len(grid[-1]) == N, "wrong input len"
    return grid


def solve(grid:list[list[int]])->int:
    '''
    1. identify all lands in this country
    2. for every pair of two lands, calculate min distance.
    '''
    N = len(grid)
    map1 = [ [0]*N for _ in range(N) ]  # land map
    deltas = [(0,1),(0,-1),(1,0),(-1,0)]

    def mark_land(y0:int, x0:int, land_id:int):
        '''
        (y0, x0) 에서 시작하여 연결된 모든 셀 탐색하여 id 지정.
        Arguments:
            land_id: identifier of current land. (>0)
        Returns:
            (edge_cells, minmax)
        '''
        edge_cells = [] # (y,x)
        lmt = [N, -1, N, -1]  # limits: min_y, max_y, min_x, max_x

        def mark_cell(y:int, x:int):
            map1[y][x] = land_id
            # cells.append((y, x))
            lmt[:] = [min(lmt[0],y),max(lmt[1],y),min(lmt[2],x),max(lmt[3],x)]

        stack = [(y0, x0)]
        mark_cell(y0, x0)

        while stack:
            cy,cx = stack.pop()
            seaside = False
            for dy,dx in deltas:
                ny,nx = cy+dy,cx+dx
                if not (0<=ny<N and 0<=nx<N): continue # out of bound
                if grid[ny][nx] == 0: seaside = True; continue # sea
                if map1[ny][nx] > 0: continue # already identified

                stack.append((ny, nx))
                mark_cell(ny, nx)
            if seaside:
                edge_cells.append((cy,cx))

        return (edge_cells, lmt)

    # 1. 이 나라의 모든 land 를 식별한다.
    num_lands = 0
    lands = []  # (cells, limits), ...

    for y in range(N):
        for x in range(N):
            if grid[y][x] == 0: continue # sea
            if map1[y][x] > 0: continue # already identified
            cells,limits = mark_land(y, x, num_lands+1)
            num_lands += 1
            lands.append((cells, limits))

    INF = int(100*100) + 1

    def bfs(y:int, x:int, target_id:int, my_id:int, min_dist:int)->int:
        '''
        return minimum distance between (y,x) to any cell of target_id land.
        if cannot reach, or dist exceed min_dist, return INF.
        '''
        distmap = [ [-1]*N for _ in range(N) ]
        que = deque() # tuple(y,x)
        que.append((y, x))
        distmap[y][x] = 0
        # 오직 첫번째 큐에 들어가는 cell 만 land 임이 허용되며, 그 이후에는 모두 sea 이어야 함.
        while que:
            cy,cx = que.popleft()
            dist = distmap[cy][cx]
            if dist > min_dist: return INF
            for dy,dx in deltas:
                ny,nx = cy+dy,cx+dx
                if not (0<=ny<N and 0<=nx<N): continue # out of bound
                if distmap[ny][nx] >= 0: continue # already visited
                if dist >= 1 and map1[ny][nx] == target_id: # we reached to target!
                    return dist
                if grid[ny][nx]: continue # not sea
                que.append((ny, nx))
                distmap[ny][nx] = dist+1
        return INF

    def cal_bridge(land1_id:int, land2_id:int, min_dist:int)->int:
        '''
        land1 에서 land2 로의 최소 bridge 계산
        land1 의 모든 edge cell 에서 land2 로 도달하는 경우의 수에 대해 검사
        bfs 탐색 사용
        '''
        cells1,cells2 = lands[land1_id-1][0],lands[land2_id-1][0]
        target1,target2 = land1_id,land2_id

        if len(cells1) > len(cells2): # 더 작은 쪽에서 시작하도록 swap
            cells1,cells2,target1,target2 = cells2,cells1,target2,target1

        for y,x in cells1:
            dist = bfs(y, x, target2, target1, min_dist)
            min_dist = min(min_dist, dist)
        return min_dist

    # 2. 이제 모든 land 간에 최단 다리를 탐색한다.
    min_dist = INF
    for j in range(1, num_lands):
        for k in range(j+1, num_lands+1):
            # pruning. y 거리, x 거리 중 하나라도 min_dist 보다 크면 skip.
            lm1,lm2 = lands[j-1][1],lands[k-1][1]
            # 두 land 간 이론적인 최소 거리 (직선 거리로 가정한 경우)
            y_dist,x_dist = -1,-1
            if lm1[1] < lm2[0]: y_dist = lm2[0] - lm1[1] - 1
            elif lm1[0] > lm2[1]: y_dist = lm1[0] - lm2[1] - 1
            if lm1[3] < lm2[2]: x_dist = lm2[2] - lm1[3] - 1
            elif lm1[2] > lm2[3]: x_dist = lm1[2] - lm2[3] - 1
            # 최소 거리가 min_dist 보다 크다면 drop!
            dist = max(y_dist, x_dist)
            if dist > min_dist: continue # early drop

            dist = cal_bridge(j, k, min_dist)
            min_dist = min(min_dist, dist)

    return min_dist


if __name__ == '__main__':
    m = get_input()
    print(solve(m))
