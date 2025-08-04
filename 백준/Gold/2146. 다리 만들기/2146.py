'''
2146번
다리 만들기 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	192 MB	51845	20040	12589	35.442%

문제
여러 섬으로 이루어진 나라가 있다. 이 나라의 대통령은 섬을 잇는 다리를 만들겠다는 공약으로 인기몰이를 해 당선될 수 있었다.
하지만 막상 대통령에 취임하자, 다리를 놓는다는 것이 아깝다는 생각을 하게 되었다.
그래서 그는, 생색내는 식으로 한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고,
그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다.

이 나라는 NxN크기의 이차원 평면상에 존재한다.
이 나라는 여러 섬으로 이루어져 있으며, 섬이란 동서남북으로 육지가 붙어있는 덩어리를 말한다.
다음은 세 개의 섬으로 이루어진 나라의 지도이다.

위의 그림에서 색이 있는 부분이 육지이고, 색이 없는 부분이 바다이다.
이 바다에 가장 짧은 다리를 놓아 두 대륙을 연결하고자 한다.
가장 짧은 다리란, 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리를 말한다.
다음 그림에서 두 대륙을 연결하는 다리를 볼 수 있다.

물론 위의 방법 외에도 다리를 놓는 방법이 여러 가지 있으나,
위의 경우가 놓는 다리의 길이가 3으로 가장 짧다.
(물론 길이가 3인 다른 다리를 놓을 수 있는 방법도 몇 가지 있다).

지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.

입력
첫 줄에는 지도의 크기 N(100이하의 자연수)가 주어진다.
그 다음 N줄에는 N개의 숫자가 빈칸을 사이에 두고 주어지며, 0은 바다, 1은 육지를 나타낸다.
항상 두 개 이상의 섬이 있는 데이터만 입력으로 주어진다.

출력
첫째 줄에 가장 짧은 다리의 길이를 출력한다.

-----

6:12~7:14

이 버전은 통과는 하였지만, 시간이 4초 정도로 꽤 길게 소요됨.
python 으로도 훨씬 더 빨리 실행되는 제출 답안들이 있음.

속도 개선된 버전은 2146c.py 참고.

'''


import sys
from collections import deque

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
        assert len(grid[-1]) == N, "wrong input len"
    return grid


def grid2str(mat:list[list[int]], indent:str='  ')->str:
    s = [ (indent + ' '.join(map(str, m))) for m in mat ]
    return '\n'.join(s)



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

    # 이 나라의 모든 land 를 식별한다.
    num_lands = 0
    lands = []  # (cells, limits), ...

    for y in range(N):
        for x in range(N):
            if grid[y][x] == 0: continue # sea
            if map1[y][x] > 0: continue # already identified
            cells,limits = mark_land(y, x, num_lands+1)
            num_lands += 1
            lands.append((cells, limits))

    log("total %d lands", num_lands)
    log("map:\n%s", grid2str(map1))
    for k in range(min(3, num_lands)):
        log("land[%d]: limits %s, edge cells %s", k+1, lands[k][1], lands[k][0])

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
        log("  (%d,%d)", y, x)
        while que:
            cy,cx = que.popleft()
            dist = distmap[cy][cx]
            if dist > min_dist:
                log("    drop")
                return INF
            for dy,dx in deltas:
                ny,nx = cy+dy,cx+dx
                if not (0<=ny<N and 0<=nx<N): continue # out of bound
                if distmap[ny][nx] >= 0: continue # already visited
                if dist >= 1 and map1[ny][nx] == target_id: # we reached to target!
                    log("    reached (%d,%d) dist %d", ny, nx, dist)
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
            log("!!!! swap")
            cells1,cells2,target1,target2 = cells2,cells1,target2,target1

        # min_dist = INF
        for y,x in cells1:
            dist = bfs(y, x, target2, target1, min_dist)
            min_dist = min(min_dist, dist)
        return min_dist

    # 이제 모든 land 간에 최단 다리를 검색.
    min_dist = INF
    for j in range(1, num_lands):
        for k in range(j+1, num_lands+1):
            # log("**** checking land %d to %d", j, k)

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
            if dist > min_dist: # early drop
                # log("! early drop! %d", dist)
                continue

            dist = cal_bridge(j, k, min_dist)
            min_dist = min(min_dist, dist)
            log("====> dist %d, min %d", dist, min_dist)

    return min_dist


if __name__ == '__main__':
    m = get_input()
    print(solve(m))




'''
예제 입력 1
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
예제 출력 1
3


run=(python3 2146.py)

echo '10\n1 1 1 0 0 0 0 1 1 1\n1 1 1 1 0 0 0 0 1 1\n1 0 1 1 0 0 0 0 1 1\n0 0 1 1 1 0 0 0 0 1\n0 0 0 1 0 0 0 0 0 1\n0 0 0 0 0 0 0 0 0 1\n0 0 0 0 0 0 0 0 0 0\n0 0 0 0 1 1 0 0 0 0\n0 0 0 0 1 1 1 0 0 0\n0 0 0 0 0 0 0 0 0 0' | $run

----
# 다양한 edge case

echo '2\n1 0\n0 1' | $run
-> 1

echo '3\n1 0 0\n0 0 0\n0 0 1' | $run
-> 3

echo '3\n1 1 0\n0 1 0\n0 0 1' | $run
-> 1

echo '2\n1 1\n0 1' | $run
-> 10001  # 문제 자체가 섬이 하나밖에 없어서 잘못된 것임.


# worst case. 대각선 양 끝 두 개의 섬.

(python3 <<EOF
N = 100
print(N)
A = [ [0]*N for _ in range(N) ]
A[0][0] = A[N-1][N-1] = 1
for a in A:
    print(' '.join(map(str, a)))
EOF
) | time $run 2> /dev/null

solve 일반 버전
->
$run  0.02s user 0.01s system 94% cpu 0.030 total

solve_fast 버전
->
$run 2> /dev/null  0.07s user 0.00s system 97% cpu 0.078 total

# 위 경우는 solve_fast 버전이 더 느림..


(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
seed(43)
N = 100
print(N)
A = [ [0]*N for _ in range(N) ]
for k in range(N*N//2):
    A[randint(0,N-1)][randint(0,N-1)] = 1
for a in A:
    print(' '.join(map(str, a)))
EOF
) | time $run

solve ->
$run  0.33s user 0.03s system 97% cpu 0.365 total

solve_fast ->
$run  0.03s user 0.01s system 56% cpu 0.062 total





38
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0


echo '38\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0' | $run
-> 2


'''

