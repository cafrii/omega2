'''
2206번

벽 부수고 이동하기 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	192 MB	166514	44896	28012	23.888%

랜덤 시뮬레이션에서 3초를 넘기는 경우들이 나와서 PyPy3로 제출했음.
실제로는 1.7초로 끝났는데 Python3 로도 되는지는 확인하지 않았음.

제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이
92092735	cafrii	2206	맞았습니다!!	282592	1752	PyPy3 / 수정	2639

문제

NxM의 행렬로 표현되는 맵이 있다.
맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
'''

import sys
from collections import deque


def solve_timeout(map1:list[str]):
    '''
    '''
    N,M = len(map1),len(map1[0])

    que = deque()
    # que 에는 (y,x,walked,chance)가 추가됨
    #    y,x 는 좌표. walked 는 이 지점까지의 걸음 수 (시점 포함),
    #    chance 는 벽을 부수는 skill 사용권. 아직 사용 안했으면 1, 이미 사용했으면 0

    visited = [ [0]*M for _ in range(N) ]
    # visited[y][x] 의 값 해석
    #    bit 0 (value 1): chance를 사용한 상태로 방문
    #    bit 1 (value 2): chance를 사용하지 않고 방문 (chance 1회 남은 상태))
    #    즉, chance_mask (1<<chance) 이며 각각 OR 가능함.

    reached = False
    que.append((0,0, 1, 1))
    chance = 1 # initial chance count
    visited[0][0] |= (1 << chance)

    def questr(que):
        return ' '.join([ f'{y}/{x}/w{w}/{c}' for y,x,w,c in que ])

    while que:
        # print(questr(que),file=sys.stderr) # warning! it takes time!
        y,x,walked,chance = que.popleft()

        # print(f'  ==> ({y},{x}) w{walked}, c{chance}, visited {visited[y][x]})',file=sys.stderr)

        if (y,x) == (N-1,M-1):
            return walked # chance를 썼던 안썼던 먼저 도달하기만 하면 됨.

        deltas = [(0,1),(0,-1),(1,0),(-1,0)]

        for d in deltas:
            y2,x2 = y+d[0],x+d[1]
            if (not 0 <= y2 < N) or (not 0 <= x2 < M):
                continue

            if map1[y2][x2] == '1':
                # 벽이지만, 아직 chance 를 사용할 수 있다면 사용하도록 시도할 수 있음.
                if chance <= 0: # 남은 chance 가 없다면 불가능
                    continue
                # 이 chance로 이미 방문한 경우라면.. skip
                if (visited[y2][x2] & (1 << chance)):
                    continue
                # chance skill을 하나 소진한 후 이동 가능.
                que.append((y2,x2, walked+1, chance-1))
                visited[y2][x2] |= (1 << (chance-1))
            else:
                if (visited[y2][x2] & (1 << chance)):
                    continue
                que.append((y2,x2,walked+1,chance))
                visited[y2][x2] |= (1 << chance)

    return -1



def solve(map1:list[str]):
    '''
    벽을 한번 부수는 것을 skill 이라고 하자.
    이 skill은 딱 한번만 사용 가능함.
    skill 이라는 변수로, 잔여 (사용 가능한) skill 수를 관리하며, 0 또는 1.

    solve_timeout() 대비 개선된 점:
        skill 사용 후에는 skill 사용 전 방문한 곳을 더 이상 고려하지 않음.

    개선 가능한 부분:
        visited 에 walked 도 저장하도록 했으나 실제로는 사용되지 않았음.
    '''
    N,M = len(map1),len(map1[0])

    que = deque()
    # que 에는 (y,x,walked,skill)가 추가됨
    #    y,x 는 좌표. walked 는 이 지점까지의 걸음 수 (시점 포함),
    #    skill 는 벽을 부수는 트릭 사용권. 아직 사용 안했으면 1, 이미 사용했으면 0

    visited = [ [ [0,0] for x in range(M) ] for y in range(N) ]
    # visited[y][x] 의 값: [ [walked_w_skill, walked_wo_skill]
    #    walked_w_skill: skill 사용한 상태로 방문 (남은 skill 0) 했을 때 walked
    #    walked_wo_skill: skill 사용하지 않고 방문 (skill 1회 남은 상태))

    reached = False
    que.append((0,0, 1, 1))
    skill = 1 # initial skill count
    visited[0][0][1] = 1

    # def questr(que):
    #     return ' '.join([ f'{y}/{x}/w{w}/{c}' for y,x,w,c in que ])

    while que:
        # print(questr(que),file=sys.stderr) # warning! it takes time!
        y,x,walked,skill = que.popleft()

        # print(f'  ==> ({y},{x}) w{walked}, c{skill}, visited {visited[y][x]})',file=sys.stderr)

        if (y,x) == (N-1,M-1):
            return walked # chance를 썼던 안썼던 먼저 도달하기만 하면 됨.

        deltas = [(0,1),(0,-1),(1,0),(-1,0)]

        for d in deltas:
            y2,x2 = y+d[0],x+d[1]
            if (not 0 <= y2 < N) or (not 0 <= x2 < M):
                continue

            if map1[y2][x2] == '1':
                # 벽이지만, 아직 skill을 사용할 수 있다면 사용하도록 시도할 수 있음.
                if skill <= 0: # 남은 skill 이 없다면 불가능
                    continue
                # skill 사용한 상태로 이미 방문한 경우라면.. skip
                if visited[y2][x2][0]:
                    continue
                # skill skill을 하나 소진한 후 이동 가능.
                que.append((y2,x2, walked+1, skill-1))
                visited[y2][x2][0] = walked+1
            else:
                # skill 사용하지도 않은 상태에서 이미 방문을 했다면 더 이상 볼 필요 없음.
                if visited[y2][x2][1]:
                    continue
                # skill 소진 상태에서 이미 여기를 방문 한 경우
                if skill <= 0 and visited[y2][x2][0]:
                    continue
                que.append((y2,x2,walked+1,skill))
                visited[y2][x2][skill] = walked+1

    return -1


input = sys.stdin.readline

N,M = map(int, input().rstrip().split())
map1 = [] # map
for _ in range(N):
    map1.append(input().rstrip()) # string with length M

# print('\n'.join(map1),'\n',solve(map1),file=sys.stderr)
print(solve(map1))


'''
예제 입력 1
6 4
0100
1110
1000
0000
0111
0000

예제 출력 1
15

예제 입력 2
4 4
0111
1111
1111
1110

예제 출력 2
-1

10 4
0000
1110
1100
1001
1011
1000
0000
0110
0101
0100

17

7 6
000000
011110
011110
011000
011011
011011
010000
12

6 5
00000
11110
00000
01111
01111
00010
18

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
a[0][0] = a[N-1][M-1] = '0'
for k in range(N):
    print(''.join(a[k]))
EOF
) | time python3 2206.py  2> /dev/null


'''