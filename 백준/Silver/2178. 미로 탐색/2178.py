'''
2178번

미로 탐색

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	192 MB	231527	108553	68111	45.190%

문제
NxM 크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는
최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다.
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
'''

'''
thinking..
노드 간 weight는 모두 1로 동일.
여러 경로 중 최소 경로만 구하면 됨.
너비우선 검색을 하여 첫번째로 발견되면 ok.
graph[(y,x)]로 만들 수도 있고
1xMN reshape 하여 graph[k]로 할 수도 있음. (k=y*M+x)
후자가 더 쉬워보인다.

노드의 최대 개수는 N*M = 10000. 별로 크지 않음.
'''

import sys
def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

from collections import deque

def solve(graph:list[list]):
    # graph[k]는 노드 k에서 이동 가능한 노드의 목록.
    # 노드 index는 0-base. 즉, 좌상단(시점)이 0, 우하단(종점)이 N*M-1.
    #
    K = len(graph) # K == N*M

    start = 0
    goal = N*M - 1

    visited = [0] * K
        # 0 또는 1. 1 이면 해당 index의 노드에 방문했음을 의미
    que = deque([ (0,1) ])
        # BFS 를 위한 선입선출 큐.
        # 큐의 요소는 (node, walked)의 튜플.
        # walked 는 시점에서부터의 이동 거리 (시점위치부터 1로 카운팅)

    while que:
        u,walked = que.popleft()
        if u < 0 or u >= K or visited[u]:
            continue

        visited[u] = 1

        if u == goal:
            log('reached goal %d, walked %d', u, walked)
            return walked

        # 다음 노드 검색.
        walked += 1
        for v in graph[u]: # 이동 가능한 이웃 목록 중
            # v는 아마도 u-1, u+1, u-M, u+M 중 일부일 것임.
            if v not in (u-1, u+1, u-M, u+M):
                log('[%d]: invalid neighbor %d', u, v)
                continue
            if v == u:
                log('[%d]: self neighbor?', v)
                continue
            if visited[v]:
                continue
            que.append((v, walked))

        # 그냥 아래와 같이 한번에 할 수도 있음. 예외 처리는 안함.
        # que.extend([ (a,walked) for a in graph[u] if not visited[a] ])
        log('[%d]: que %s', u, que)

    # 여기에 도달한다면 도착에 실패한 것임.
    log('failed to reach goal')
    return 0


N,M = map(int, input().split())

A = [ input().strip() for _ in range(N) ]
# 각 요소는 길이 M 이면서 0 과 1로만 구성된 문자열. ex: '1010100'

log('A:\n%s', '\n'.join(A))

# 그래프 생성
graph = [ [] for _ in range(N*M) ]
for y in range(N):
    for x in range(M):
        k = y*M + x
        if A[y][x] == '0':
            continue
        if x > 0 and A[y][x-1] == '1': # left
            graph[k].append(k-1)
        if x < M-1 and A[y][x+1] == '1': # right
            graph[k].append(k+1)
        if y > 0 and A[y-1][x] == '1': # up
            graph[k].append(k-M)
        if y < N-1 and A[y+1][x] == '1': # down
            graph[k].append(k+M)

        log('++ [%d]: (%d,%d), %s', k, y, x, graph[k])

log('graph:\n%s', graph)
print(solve(graph))


'''
예제 입력 1
4 6
101111
101010
101011
111011
예제 출력 1
15


4 6
110110
110110
111111
111101
예제 출력 2
9

예제 입력 3
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3
38

예제 입력 4
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
예제 출력 4
13

2 2
11
01
echo '2 2\n11\n01\n' | python3 2178.py
3

2 4
1010
1111
echo '2 4\n1010\n1111' | python3 2178.py
5


(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,M = 100,100
print(N, M)
get_01 = lambda p_of_1 : ('1' if randint(1, 100) <= p_of_1 else '0')
for _ in range(N):
    a = [ get_01(80) for _ in range(M) ]
    if _ == 0: a[0] = '1'
    if _ == N-1: a[-1] = '1'
    print(''.join(a))
EOF
) | time python3 2178.py 2> /dev/null


'''