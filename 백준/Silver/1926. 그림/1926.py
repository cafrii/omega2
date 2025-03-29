'''
1926번

그림 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	57102	25767	17492	43.512%

문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자.
가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다.
그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다.
두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다.
(단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
'''



def solve(map1:list[list[int]]):
    #
    N,M = len(map1),len(map1[0])
    visited = [ [0]*M for _ in range(N) ]

    def mark_group(sy, sx):

        stack = [(sy, sx)] # (y, x)
        visited[sy][sx] = 1
        extent = 1
        deltas = [(0,-1),(0,1),(-1,0),(1,0)]

        while stack:
            y2,x2 = stack.pop()

            for d in deltas:
                ny,nx = y2+d[0],x2+d[1]
                if not (0<=ny<N and 0<=nx<M):
                    continue
                if visited[ny][nx] or map1[ny][nx] == 0:
                    continue
                stack.append((ny,nx))
                visited[ny][nx] = 1
                extent += 1
            #
        return extent

    num_group = 0
    max_extent = 0

    for y in range(N):
        for x in range(M):
            if not map1[y][x] or visited[y][x]:
                continue
            group_extent = mark_group(y,x)
            num_group += 1
            max_extent = max(max_extent, group_extent)

    return num_group, max_extent



N,M = map(int, input().split())
map1 = []
for _ in range(N):
    map1.append(list(map(int, input().split())))

num, extent = solve(map1)
print(num)
print(extent)

'''
예제 입력 1
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

예제 출력 1
4
9

6 5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 0
1 1 0 0 1
1 0 1 0 1
0 1 1 0 0
3
17

시간초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,M = 500,500
print(N, M)
for _ in range(N):
    print( ' '.join([ str(randint(0,1)) for _ in range(M) ]) )
EOF
) | time python3 1926.py
python3 1926.py  0.10s user 0.01s system 59% cpu 0.183 total

'''
