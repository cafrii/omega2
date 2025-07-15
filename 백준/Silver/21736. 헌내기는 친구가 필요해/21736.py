'''
21736번
헌내기는 친구가 필요해 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (하단 참고)	1024 MB	19319	11646	9674	60.109%

문제
2020년에 입학한 헌내기 도연이가 있다. 도연이는 비대면 수업 때문에 학교에 가지 못해 학교에 아는 친구가 없었다.
드디어 대면 수업을 하게 된 도연이는 어서 캠퍼스 내의 사람들과 친해지고 싶다.

도연이가 다니는 대학의 캠퍼스는 $N \times M$ 크기이며 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다.
예를 들어, 도연이가 ($x$, $y$)에 있다면 이동할 수 있는 곳은 ($x+1$, $y$), ($x$, $y+1$), ($x-1$, $y$), ($x$, $y-1$)이다.
단, 캠퍼스의 밖으로 이동할 수는 없다.

불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램을 작성해보자.

입력
첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수 $N$ ($ 1 \leq N \leq 600$), $M$ ($ 1 \leq M \leq 600$)이 주어진다.

둘째 줄부터
$N$개의 줄에는 캠퍼스의 정보들이 주어진다. O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.

출력
첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 TT를 출력한다.

----

4:14~4:30

'''


import sys
input = sys.stdin.readline


def solve(map1:list[str])->int:
    '''

    '''
    N,M = len(map1),len(map1[0])
    visited = [[0]*M for y in range(N)]
    # find location of 'I'
    cy,cx = next(
        ((y, row.index('I')) for y, row in enumerate(map1) if 'I' in row),
        (0, 0)
    ) # current y and x
    if map1[cy][cx] != 'I':
        return 0

    stack = [(cy,cx)]
    visited[cy][cx] = 1
    count = 0

    while stack:
        cy,cx = stack.pop()
        for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
            ny,nx = cy+dy,cx+dx
            if not (0<=ny<N and 0<=nx<M):
                continue
            if visited[ny][nx]:
                continue
            if map1[ny][nx] == 'X':
                continue
            # map[][] is now P or O
            if map1[ny][nx] == 'P':
                count += 1
            stack.append((ny,nx))
            visited[ny][nx] = 1

    return count


N,M = map(int, input().split())

map1 = []
for _ in range(N):
    map1.append(input().strip())
    assert len(map1[-1]) == M
count = solve(map1)
print(str(count) if count > 0 else 'TT')



'''
예제 입력 1
3 5
OOOPO
OIOOX
OOOXP
예제 출력 1
1
예제 입력 2
3 3
IOX
OXP
XPP
예제 출력 2
TT


run=(python3 21736.py)

echo '3 5\nOOOPO\nOIOOX\nOOOXP' | $run
echo '3 3\nIOX\nOXP\nXPP' | $run
-> 1
-> TT

'1 1\nI'




(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
# seed(43)
N,M = 600,600
print(N,M)
cell = ['O','O','O','O','X','P']
num_kind = len(cell)
map1 = []
for y in range(N):
    map1.append([ str( cell[randint(0,num_kind-1)] ) for x in range(M) ])
map1[randint(0,N-1)][randint(0,M-1)] = 'I'
for y in range(N):
    print( ''.join(map1[y]) )
EOF
) | time $run




'''

