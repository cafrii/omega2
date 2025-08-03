'''
17472번
다리 만들기 2 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	34025	12881	8279	34.384%

문제
섬으로 이루어진 나라가 있고, 모든 섬을 다리로 연결하려고 한다.
이 나라의 지도는 NxM 크기의 이차원 격자로 나타낼 수 있고,
격자의 각 칸은 땅이거나 바다이다.

섬은 연결된 땅이 상하좌우로 붙어있는 덩어리를 말하고,
아래 그림은 네 개의 섬으로 이루어진 나라이다. 색칠되어있는 칸은 땅이다.

다리는 바다에만 건설할 수 있고, 다리의 길이는 다리가 격자에서 차지하는 칸의 수이다.
다리를 연결해서 모든 섬을 연결하려고 한다.
섬 A에서 다리를 통해 섬 B로 갈 수 있을 때, 섬 A와 B를 연결되었다고 한다.
다리의 양 끝은 섬과 인접한 바다 위에 있어야 하고, 한 다리의 방향이 중간에 바뀌면 안된다.
또, 다리의 길이는 2 이상이어야 한다.

다리의 방향이 중간에 바뀌면 안되기 때문에, 다리의 방향은 가로 또는 세로가 될 수 밖에 없다.
방향이 가로인 다리는 다리의 양 끝이 가로 방향으로 섬과 인접해야 하고,
방향이 세로인 다리는 다리의 양 끝이 세로 방향으로 섬과 인접해야 한다.

섬 A와 B를 연결하는 다리가 중간에 섬 C와 인접한 바다를 지나가는 경우에
섬 C는 A, B와 연결되어있는 것이 아니다.

아래 그림은 섬을 모두 연결하는 올바른 2가지 방법이고, 다리는 회색으로 색칠되어 있다.
섬은 정수, 다리는 알파벳 대문자로 구분했다.

다리의 총 길이: 13

D는 2와 4를 연결하는 다리이고, 3과는 연결되어 있지 않다.

다리의 총 길이: 9 (최소)

다음은 올바르지 않은 3가지 방법이다

C의 방향이 중간에 바뀌었다.
D의 길이가 1이다.
가로 다리인 A가 1과 가로로 연결되어 있지 않다.

다리가 교차하는 경우가 있을 수도 있다.
교차하는 다리의 길이를 계산할 때는 각 칸이 각 다리의 길이에 모두 포함되어야 한다.
아래는 다리가 교차하는 경우와 기타 다른 경우에 대한 2가지 예시이다.

A의 길이는 4이고, B의 길이도 4이다.
총 다리의 총 길이: 4 + 4 + 2 = 10

다리 A: 2와 3을 연결 (길이 2)
다리 B: 3과 4를 연결 (길이 3)
다리 C: 2와 5를 연결 (길이 5)
다리 D: 1과 2를 연결 (길이 2)
총 길이: 12

나라의 정보가 주어졌을 때, 모든 섬을 연결하는 다리 길이의 최솟값을 구해보자.

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다.
둘째 줄부터 N개의 줄에 지도의 정보가 주어진다.
각 줄은 M개의 수로 이루어져 있으며, 수는 0 또는 1이다.
0은 바다, 1은 땅을 의미한다.

출력
모든 섬을 연결하는 다리 길이의 최솟값을 출력한다.
모든 섬을 연결하는 것이 불가능하면 -1을 출력한다.

제한
1 ≤ N, M ≤ 10
3 ≤ NxM ≤ 100
2 ≤ 섬의 개수 ≤ 6

----

6:44~8:25


----
먼저 각 섬 간의 최소 다리 비용을 구한다.
그 다음 mst 로 트리 비용을 구한다.

다리 비용은 모든 섬 조합에 대해서 진행.

'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    grid = []
    for _ in range(N):
        m = list(map(int, input().split()))
        assert len(m) == M, "wrong m sz"
        grid.append(m)
    return grid


def solve(grid:list[list[int]])->int:
    '''

    '''
    N,M = len(grid),len(grid[0])
    log("%d x %d", N, M)

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
        log("mark island %d from (%d,%d)..", id, y0, x0)

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

    def grid2str(mat:list[list[int]], indent:str)->str:
        s = [ (indent + ' '.join(map(str, m))) for m in mat ]
        return '\n'.join(s)

    log("total %d islands", num_island)
    log("%s", grid2str(mat, '  '))
    log("island1: cells %s, exts %s", islands[0][0], islands[0][1])

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
            log("h bridge (%d,%d)-(%d,%d), dist %d, mindist %d", y0,x0, y0,x, x0-x-1, min_dist)
            break
        for x in range(x0+1, M):  # right
            if mat[y0][x] == 0: continue # sea
            if mat[y0][x] != target: break # unwanted island!
            if x - x0 <= 2: break # too short bridge
            min_dist = min(min_dist, x - x0 - 1)
            log("h bridge (%d,%d)-(%d,%d), dist %d, mindist %d", y0,x0, y0,x, x-x0-1, min_dist)
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
            log("v bridge (%d,%d)-(%d,%d), dist %d, mindist %d", y0,x0, y,x0, y0-y-1, min_dist)
            break
        for y in range(y0+1, N):  # down
            if mat[y][x0] == 0: continue # sea
            if mat[y][x0] != target: break # unwanted island!
            if y - y0 <= 2: break # too short bridge
            min_dist = min(min_dist, y - y0 - 1)
            log("v bridge (%d,%d)-(%d,%d), dist %d, mindist %d", y0,x0, y,x0, y-y0-1, min_dist)
            break
        return min_dist


    def calc_bridge_cost(is1_id:int, is2_id:int)->int:
        '''
        두 섬 is1 과 is2 사이의 다리 연결 가능성을 검사.
        is1 의 모든 지점에서 is2 에 이어질 수 있는지 확인.
        연결 가능하면 다리 길이를 리턴 (>=2)
        연결이 불가능하면 -1 을 리턴
        '''
        log("**** calc bridge %d-%d", is1_id, is2_id)
        is1,is2 = islands[is1_id-1], islands[is2_id-1]

        # check x or y overlap
        ext1,ext2 = is1[1],is2[1]
        # ext:  min_y,max_y,min_x,max_x

        y_overlap = max(ext1[0],ext2[0]) <= min(ext1[1],ext2[1])
        x_overlap = max(ext1[2],ext2[2]) <= min(ext1[3],ext2[3])

        if not (y_overlap or x_overlap): # they are apart diagonally!
            log("island %d and %d apart diagonally", is1_id, is2_id)
            return -1

        log("y, x, overlap: %s %s", y_overlap, x_overlap)
        cell1,cell2,target1,target2 = is1[0],is2[0],is1_id,is2_id
        if len(cell1) > len(cell2):
            # swap! 더 적은 쪽에서 연결 시도하는 것이 유리함.
            log("!!!! swap")
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
            log("  -> island %d and %d can be connected, min dist %d", is1_id, is2_id, min_dist)
            return min_dist
        return -1


    costs = []  # tuple(is1, is2, dist)

    for j in range(1,num_island+1):
        for k in range(j+1, num_island+1):
            c = calc_bridge_cost(j, k)
            if c >= 2:
                costs.append((j, k, c))

    costs.sort(key = lambda x: x[2])
    log("costs: %s", costs)

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


'''
예제 입력 1
7 8
0 0 0 0 0 0 1 1
1 1 0 0 0 0 1 1
1 1 0 0 0 0 0 0
1 1 0 0 0 1 1 0
0 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
예제 출력 1
9

예제 입력 2
7 8
0 0 0 1 1 0 0 0
0 0 0 1 1 0 0 0
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
예제 출력 2
10

예제 입력 3
7 8
1 0 0 1 1 1 0 0
0 0 1 0 0 0 1 1
0 0 1 0 0 0 1 1
0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0
0 1 1 1 0 0 0 0
1 1 1 1 1 1 0 0
예제 출력 3
9

예제 입력 4
7 7
1 1 1 0 1 1 1
1 1 1 0 1 1 1
1 1 1 0 1 1 1
0 0 0 0 0 0 0
1 1 1 0 1 1 1
1 1 1 0 1 1 1
1 1 1 0 1 1 1
예제 출력 4
-1



run=(python3 17472.py)

echo '7 8\n0 0 0 0 0 0 1 1\n1 1 0 0 0 0 1 1\n1 1 0 0 0 0 0 0\n1 1 0 0 0 1 1 0\n0 0 0 0 0 1 1 0\n0 0 0 0 0 0 0 0\n1 1 1 1 1 1 1 1' | $run
# -> 9
echo '7 8\n0 0 0 1 1 0 0 0\n0 0 0 1 1 0 0 0\n1 1 0 0 0 0 1 1\n1 1 0 0 0 0 1 1\n1 1 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n1 1 1 1 1 1 1 1' | $run
# -> 10
echo '7 8\n1 0 0 1 1 1 0 0\n0 0 1 0 0 0 1 1\n0 0 1 0 0 0 1 1\n0 0 1 1 1 0 0 0\n0 0 0 0 0 0 0 0\n0 1 1 1 0 0 0 0\n1 1 1 1 1 1 0 0' | $run
# -> 9
echo '7 7\n1 1 1 0 1 1 1\n1 1 1 0 1 1 1\n1 1 1 0 1 1 1\n0 0 0 0 0 0 0\n1 1 1 0 1 1 1\n1 1 1 0 1 1 1\n1 1 1 0 1 1 1' | $run
# -> -1

echo '7 8\n1 1 1 1 0 0 0 1\n1 0 0 0 0 1 0 0\n1 1 0 0 1 1 0 0\n1 0 1 1 0 1 0 1\n1 0 0 0 1 1 0 0\n1 0 0 0 0 0 1 0\n1 1 1 0 0 1 1 0' | $run
# -> 11
  1 1 1 1 0 0 0 2
  1 0 0 0 0 3 0 0
  1 1 0 0 3 3 0 0
  1 0 4 4 0 3 0 5
  1 0 0 0 3 3 0 0
  1 0 0 0 0 0 6 0
  1 1 1 0 0 6 6 0
costs: [(1, 3, 2), (1, 4, 2), (1, 6, 2), (2, 5, 2), (1, 2, 3)]


'''

