
'''
7562번

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	70699	38314	28443	52.977%

문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다.
체스판의 크기는 l x l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} x {0, ..., l-1}로 나타낼 수 있다.
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

9:38~10:01, 28min
'''

from collections import deque

def solve(sz:int, s:tuple[int,int], e:tuple[int,int]):
    '''
    sz: size of board (w, h)
    s: staring point (y, x)
    e: goal point (y, x)
    return: minimum number of walked
    '''

    que = deque()
    que.append((s, 0))
    visited = [ [0]*sz for _ in range(sz) ]

    while que:
        (y,x),walked = que.popleft()
        if (y,x) == e:
            return walked

        deltas = [ (-1,-2),(-2,-1),(-2,1),(-1,2),
                   (1,-2),(2,-1),(2,1),(1,2) ]
        for d in deltas:
            y2,x2 = y+d[0],x+d[1]
            if (not 0 <= y2 < sz) or (not 0 <= x2 < sz):
                continue
            if visited[y2][x2]:
                continue
            que.append(((y2,x2), walked+1))
            visited[y2][x2] = 1

    return -1 # cannot reach to goal!

MIN_L,MAX_L = 4,300

T = int(input().strip())
for _ in range(T):
    L = int(input().strip())
    if (not MIN_L <= L <= MAX_L):
        break # wrong input
    s = tuple(map(int, input().split()))
    e = tuple(map(int, input().split()))
    print(solve(L, s, e))


'''
echo '1\n4\n3 0\n0 3' | python3 7562.py
2
echo '1\n5\n4 0\n0 4' | python3 7562.py
4

echo '1\n300\n0 0\n299 299' | time python3 7562.py
200

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
T = 100
print(T)
for _ in range(T):
    print(300)
    print(randint(0,299),randint(0,299))
    print(randint(0,299),randint(0,299))
EOF
) | time python3 7562.py > /dev/ttys001

python3 7562.py > /dev/ttys001  2.67s user 0.01s system 99% cpu 2.693 total
# => for T=100, 2.67s elapsed -> 26 ms/test
'''
