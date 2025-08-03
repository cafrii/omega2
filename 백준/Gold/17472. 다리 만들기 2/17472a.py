'''

제출용

'''



import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    grid = []
    for _ in range(N):
        m = list(map(int, input().split()))
        grid.append(m)
    return grid


def solve(grid:list[list[int]])->int:
    '''
    '''
    N,M = len(grid),len(grid[0])

    # our matrix: it has map information
    mat = [ [0]*M for n in range(N) ]

    def mark_island(y0, x0, id):
        '''
        (y0,x0)에서부터 시작하여 연결된 육지 지점들을 id로 마크.
        returns:
            tuple of cell cordinates list, extents.
        '''
        cells = [] # cell coordinates: 이 섬에 해당하는 모든 셀 좌표 수집
        exts = [N,-1,M,-1]  # extents: min_y,max_y,min_x,max_x

        def mark(y, x, id):
            # mark one cell location
            mat[y][x] = id
            cells.append((y, x))
            exts[:] = [min(exts[0],y),max(exts[1],y),min(exts[2],x),max(exts[3],x)]

        stack = [(y0, x0)]
        mark(y0, x0, id)

        while stack:
            cy,cx = stack.pop() # current y,x
            for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]: # delta y,x
                ny,nx = cy+dy,cx+dx  # next y,x
                if not (0<=ny<N and 0<=nx<M): continue # bound check
                if grid[ny][nx] == 0: continue # check if sea
                if mat[ny][nx] > 0: continue # check if already marked to island
                stack.append((ny, nx))
                mark(ny, nx, id)
        return cells,exts

    num_island = 0
    islands = []  # (cells, exts)
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 0: continue
            if mat[y][x] > 0: continue
            cells,exts = mark_island(y, x, num_island+1)
            islands.append((cells, exts))
            num_island += 1

    INF = 999

    def measure_horz_dist(y0:int, x0:int, target:int)->int:
        '''
        return INF if fail
        '''
        min_dist = INF
        for x in range(x0-1, -1, -1):  # left
            if mat[y0][x] == 0: continue # sea
            if mat[y0][x] != target: break # unwanted island!
            if x0 - x <= 2: break # too short bridge
            min_dist = min(min_dist, x0 - x - 1)
            break
        for x in range(x0+1, M):  # right
            if mat[y0][x] == 0: continue # sea
            if mat[y0][x] != target: break # unwanted island!
            if x - x0 <= 2: break # too short bridge
            min_dist = min(min_dist, x - x0 - 1)
            break
        return min_dist

    def measure_vert_dist(y0:int, x0:int, target:int)->int:
        '''
        return INF if failed
        '''
        min_dist = INF
        for y in range(y0-1, -1, -1):  # up
            if mat[y][x0] == 0: continue # sea
            if mat[y][x0] != target: break # unwanted island!
            if y0 - y <= 2: break # too short bridge
            min_dist = min(min_dist, y0 - y - 1)
            break
        for y in range(y0+1, N):  # down
            if mat[y][x0] == 0: continue # sea
            if mat[y][x0] != target: break # unwanted island!
            if y - y0 <= 2: break # too short bridge
            min_dist = min(min_dist, y - y0 - 1)
            break
        return min_dist


    def calc_bridge_cost(is1_id:int, is2_id:int)->int:
        '''
        두 섬 is1 과 is2 사이의 다리 연결 가능성을 검사.
        is1 의 모든 지점에서 is2 에 이어질 수 있는지 확인.
        연결 가능하면 다리 길이를 리턴 (>=2)
        연결이 불가능하면 -1 을 리턴
        '''
        is1,is2 = islands[is1_id-1], islands[is2_id-1]

        # check x or y overlap
        ext1,ext2 = is1[1],is2[1]
        # ext:  min_y,max_y,min_x,max_x

        y_overlap = max(ext1[0],ext2[0]) <= min(ext1[1],ext2[1])
        x_overlap = max(ext1[2],ext2[2]) <= min(ext1[3],ext2[3])

        if not (y_overlap or x_overlap): # they are apart diagonally!
            return -1

        cell1,cell2,target1,target2 = is1[0],is2[0],is1_id,is2_id
        if len(cell1) > len(cell2):
            # swap! 더 적은 쪽에서 연결 시도하는 것이 유리함.
            cell1,cell2,target1,target2 = cell2,cell1,target2,target1

        min_dist = INF
        for y,x in cell1:
            if y_overlap:
                dist = measure_horz_dist(y, x, target2)
                if dist<INF: min_dist = min(min_dist, dist)
            # 주의! x 와 y 둘 다 overlap 될 수 있음! ㄷ 자 형태로 감싸는 경우!
            if x_overlap:
                dist = measure_vert_dist(y, x, target2)
                if dist<INF: min_dist = min(min_dist, dist)

        if min_dist < INF:
            return min_dist
        return -1

    costs = []  # tuple(is1, is2, dist)

    for j in range(1,num_island+1):
        for k in range(j+1, num_island+1):
            c = calc_bridge_cost(j, k)
            if c >= 2:
                costs.append((j, k, c))

    costs.sort(key = lambda x: x[2])

    # 다리 비용 정보가 완성되면 kruscal 방식으로 최소 비용을 계산한다.
    # 섬의 번호는 1부터 시작.
    roots = list(range(num_island+1))

    def find_root(a:int)->int:
        if roots[a] == a:
            return a
        ra = roots[a] = find_root(roots[a])
        return ra

    # 비용이 적은 bridge 부터 시작하여 모든 bridge 검사
    total_costs = 0
    num_conn_bridges = 0
    for a,b,c in costs:
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue # already connected
        roots[b] = roots[rb] = ra
        total_costs += c
        num_conn_bridges += 1
        if num_conn_bridges >= num_island-1:
            break
    return total_costs if num_conn_bridges >= num_island-1 else -1


if __name__ == '__main__':
    inp = get_input()
    r = solve(inp)
    print(r)



