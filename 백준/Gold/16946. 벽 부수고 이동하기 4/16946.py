'''
16946
벽 부수고 이동하기 4

시리즈 문제
- 2206 벽 부수고 이동하기
- 14442 벽 부수고 이동하기 2
- 16933 벽 부수고 이동하기 3
- 16946 벽 부수고 이동하기 4

이 문제는 기존의 벽 부수기 문제랑은 다른 문제이다.

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	29410	8585	5987	25.807%

문제
NxM의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
한 칸에서 다른 칸으로 이동하려면, 두 칸이 인접해야 한다. 두 칸이 변을 공유할 때, 인접하다고 한다.

각각의 벽에 대해서 다음을 구해보려고 한다.

벽을 부수고 이동할 수 있는 곳으로 변경한다.
그 위치에서 이동할 수 있는 칸의 개수를 세어본다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다.

출력
맵의 형태로 정답을 출력한다. 원래 빈 칸인 곳은 0을 출력하고, 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력한다.
'''


import sys
def log(fmt, *args):
    print(fmt % args, file=sys.stderr)


def solve(map1:list[str]):
    #
    N,M = len(map1),len(map1[0])
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    # area map. it stores area id (>= 0)
    map_a = [ [-1 for x in range(M)] for y in range(N) ]

    def mark_area(sy, sx, area_id):
        # starting from (sy,sx), find adjacent free connected areas
        #  and mark area id in the cell.
        # also, calculate the extent of the area and return it.
        # area id should be >= 0
        # area id of -1 means that the cell is not marked yet.

        # log("mark area starting (%d,%d), id %d ..", sy, sx, area_id)
        stack = [(sy,sx)]
        map_a[sy][sx] = area_id
        extent = 1

        while stack:
            y,x = stack.pop()
            for d in neighbors:
                y2,x2 = y+d[0],x+d[1]
                if not (0 <= y2 < N and 0 <= x2 < M):
                    continue
                if map1[y2][x2] == '1' or map_a[y2][x2] >= 0:
                    continue
                map_a[y2][x2] = area_id
                extent += 1
                stack.append((y2,x2))

        return extent

    area_extents = [] # area_extents[k]: extent of area-k
    for y in range(N):
        for x in range(M):
            if map1[y][x] == '1' or map_a[y][x] >= 0:
                continue
            extent = mark_area(y,x, area_id=len(area_extents))
            area_extents.append(extent)
            # save each area's extent

    log('area map:')
    for y in range(N):
        log('  ' + ''.join( [ (str(x) if x >= 0 else '.') for x in map_a[y] ] ))
    log('area extents: %s', area_extents)

    # generate answer
    result:list[str] = []

    for y in range(N):
        ls = []
        for x in range(M):
            if map1[y][x] == '0':
                ls.append('0')
                continue
            # map1[y][x] == '1'
            area_ids = set()
            for d in neighbors:
                y2,x2 = y+d[0],x+d[1]
                if not (0 <= y2 < N and 0 <= x2 < M):
                    continue
                if map1[y2][x2] == '1':
                    continue
                if map_a[y2][x2] < 0:
                    log("!!(%d,%d) area_ids %d", y2, x2, map_a[y2][x2])
                    sys.exit(1)
                area_ids.add(map_a[y2][x2])
            merged_extent = 1
            for id in area_ids:
                merged_extent += area_extents[id]
            ls.append(str(merged_extent % 10))
        #
        result.append(''.join(ls))

    return result


N,M = map(int, input().split())
map1 = [] # map
for _ in range(N):
    map1.append(input().strip())

# log('map: %s', str(map1))
map2:list[str] = solve(map1)
for s in map2:
    print(s)



'''
예제 입력 1
3 3
101
010
101
예제 출력 1
303
050
303

예제 입력 2
4 5
11001
00111
01010
10101
예제 출력 2
46003
00732
06040
50403

1 1
1
-> 1

3 3
111
111
111
->
111
111
111

3 3
000
010
000
->
000
090
000

3 3
100
010
001
->
700
070
007

시간 초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,M=1000,1000
print(N,M)
a = []
for _ in range(N):
    a.append([ str(randint(0,100)//80) for k in range(M) ])
for k in range(N):
    print(''.join(a[k]))
EOF
) | time python3 16946.py  2> /dev/null

'''