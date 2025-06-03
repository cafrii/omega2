'''
10026번

적록색약 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	83169	48533	36404	57.137%

문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

--------

12:41~
문제 자체를 잘 이해 못해서 해멘 시간은 제외시킴.
2:49 ~ 3:12

'''


import sys
input = sys.stdin.readline

def solve(pic:list[str])->tuple[int,int]:
    N = len(pic)

    visited = [ [-1 for c in range(N)] for r in range(N)]

    def mark(y0, x0, id, pred):
        # (y0,x0) 에서부터 시작하는 연속 영역을 찾아서 id 로 마킹
        # visited[][] 에 id 기록

        stack = [(y0,x0)]
        visited[y0][x0] = id

        deltas = [(-1,0),(1,0),(0,-1),(0,1)]
        while stack:
            y,x = stack.pop()
            col = pic[y][x]

            for dy,dx in deltas:
                ny,nx = y+dy,x+dx
                if not (0<=ny<N and 0<=nx<N):
                    continue
                if visited[ny][nx] >= 0: # already visited
                    continue
                if not pred(pic[ny][nx], col):
                    continue
                stack.append((ny,nx))
                visited[ny][nx] = id

    def count_regions(pred):
        num = 0 # number of region
        for y in range(N):
            for x in range(N):
                if visited[y][x] >= 0:
                    continue
                mark(y, x, num, pred)
                num += 1
        return num

    # predicate for each cases
    def pred_normal(c1, c2):
        return c1 == c2
    def pred_weak(c1, c2):
        return (c1 == c2 or (c1,c2) == ('R','G') or (c1,c2) == ('G','R'))

    n1 = count_regions(pred_normal)

    # reset visited and check again
    for a in visited:
        a[:] = [-1 for c in range(N)]
    n2 = count_regions(pred_weak)

    return (n1, n2)


N = int(input().strip())
pic = []
for _ in range(N):
    pic.append(input().strip())
    assert len(pic[-1]) == N

print(*solve(pic))










'''

run=(python3 10026.py)


5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
-> 4 3

echo '5\nRRRBB\nGGBBB\nBBBRR\nBBRRR\nRRRRR' | $run


2
RG
BR
-> 4 2

2
RG
GR
-> 4 1

3
RGB
RGB
RGB
-> 3 2

1
R
-> 1 1



(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 100
print(N)
cols = 'RGB'
for k in range(N):
    print(''.join([ cols[randint(0,2)] for _ in range(N) ]))
EOF
) | time $run



'''

