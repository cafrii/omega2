'''

유사 문제
- 2206 벽 부수고 이동하기
- 14442 벽 부수고 이동하기 2
- 16933 벽 부수고 이동하기 3
- 16946 벽 부수고 이동하기 4

14442번

벽 부수고 이동하기 2 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	37391	10625	7085	27.160%

문제
NxM의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000), K(1 ≤ K ≤ 10)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
'''


import sys
from collections import deque

import sys
def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

def solve(map1:list[str], K:int):
    '''
    벽을 부수는 능력 skill 한번 쓸 때 마다 1씩 소진.
    초기값 K (K번 부술 수 있음), 사용 시 마다 -1 하여 0 까지 가능.
    '''
    N,M = len(map1),len(map1[0])

    que = deque()
    # que 에는 (y,x,walked,skill)가 추가됨
    #    y,x 는 좌표. walked 는 이 지점까지의 걸음 수 (시점 포함),
    #    skill 는 벽을 부수는 트릭 사용권. 아직 사용 안했으면 K, 모두 다 사용했으면 0

    visited = [ [ -1 for x in range(M) ] for y in range(N) ]
    # visited[y][x] 의 값:
    #    -1: 방문하지 않음
    #     0: skill을 다 소진한 상태에서 방문했음
    #     k: skill이 k번 남은 상태에서 방문
    #     K: skill을 한번도 쓰지 않은 상태에서 방문

    que.append((0, 0, 1, K))
    # skill = K # initial skill count
    visited[0][0] = K

    def questr(que):
        # return ' '.join([ f'{y}/{x}/w{w}/{c}' for y,x,w,c in que ])
        return ''
    stage = 1
    while que:
        # log(questr(que)) # warning! it takes time!
        y,x,walked,skill = que.popleft()
        if stage != walked:
            stage = walked
            # log('------------------------- stage %d', stage)

        # log(f'  ==> ({y},{x}) w{walked}, s{skill}, visited {visited[y][x]})')

        if (y,x) == (N-1,M-1):
            # log('++++ finished! walked %d, remaining skill %d', walked, skill)
            return walked # chance를 썼던 안썼던 먼저 도달하기만 하면 됨.

        # deltas = [(0,1),(0,-1),(1,0),(-1,0)]
        # 우하단으로 가는 방향을 먼저 que에 넣는게 시간 단축에 도움이 될 확률이 크다.
        deltas = [(0,1),(1,0),(0,-1),(-1,0)]

        for d in deltas:
            y2,x2 = y+d[0],x+d[1]
            if (not 0 <= y2 < N) or (not 0 <= x2 < M):
                continue

            if map1[y2][x2] == '1':
                # 벽이지만, 아직 skill을 사용할 수 있다면 사용하도록 시도할 수 있음.
                if skill <= 0: # 남은 skill 이 없다면 불가능
                    continue
                # 더 적은 skill 사용하여 여기에 이미 도달했었다면 skip
                if visited[y2][x2] >= skill-1:
                    continue
                # skill을 하나 소진한 후 이동 가능.
                que.append((y2,x2, walked+1, skill-1))
                visited[y2][x2] = skill-1
            else:
                # skill을 더 적게 사용하여 이미 방문을 했다면 더 이상 볼 필요 없음.
                if visited[y2][x2] >= skill:
                    continue
                que.append((y2,x2,walked+1,skill))
                visited[y2][x2] = skill

    return -1


input = sys.stdin.readline

N,M,K = map(int, input().rstrip().split())
map1 = [] # map
for _ in range(N):
    map1.append(input().rstrip()) # string with length M

# log('--------\n%s', '\n'.join(map1))
print(solve(map1,K))


'''
예제 입력 1
6 4 1
0100
1110
1000
0000
0111
0000
예제 출력 1
15

예제 입력 2
6 4 2
0100
1110
1000
0000
0111
0000
예제 출력 2
9
0 1 0 0
1 1 1 0
1 0 0 0
0 0 0 0
0 1 1 1
0 0 0 0

예제 입력 3
4 4 3
0111
1111
1111
1110
예제 출력 3
-1

5 5 4
01101
11100
00111
11110
00110
9


시간 초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,M,K=500,500,10
print(N,M,K)
a = []
for _ in range(N):
    a.append([ str(randint(0,100)//80) for k in range(M) ])
a[0][0] = a[N-1][M-1] = '0'
for k in range(N):
    print(''.join(a[k]))
EOF
) | time python3 14442.py  2> /dev/null

'''
