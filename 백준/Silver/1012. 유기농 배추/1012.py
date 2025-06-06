'''
유기농 배추 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	222571	92884	61320	39.300%

문제
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다.
농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에,
한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어,
그 배추들 역시 해충으로부터 보호받을 수 있다.
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다.
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

1	1	0	0	0	0	0	0	0	0
0	1	0	0	0	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	1	1	0	0	0	1	1	1
0	0	0	0	1	0	0	1	1	1

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50),
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.
그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
두 배추의 위치가 같은 경우는 없다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

'''

import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve():
    T = int(input().strip())
    ans = [0]*T
    for t in range(T):
        M,N,K = map(int, input().split())
        # create N by M 2-d array
        A = [ [0 for x in range(M)] for y in range(N) ]
        for _ in range(K):
            x,y = map(int, input().split())
            A[y][x] = 1
        ans[t] = solve_tc(A)

    print(*ans, sep='\n')


def solve_tc(A:list[list]) -> int:
    '''
    Solve one test case.
    Args: A - 2d map
    Returns: number of segment
    '''
    N,M = len(A),len(A[0])

    idmap = [[0 for x in range(M)] for y in range(N)]
    # idmap[][] == 0 means that it is not visited yet.

    deltas = [(1,0), (-1,0), (0,1), (0,-1)]

    def mark(y0, x0, id):
        # starting from (y0, x0), mark area (1-segment) with id
        # id should be > 0
        stack = [ (y0, x0) ]
        idmap[y0][x0] = id
        extent = 1

        while stack:
            # log('    stack %s', stack)
            y,x = stack.pop()
            for dy,dx in deltas:
                ny,nx = y+dy,x+dx
                if not (0<=ny<N and 0<=nx<M): # out of map
                    continue
                if A[ny][nx] == 0: # cannot be area
                    continue
                if idmap[ny][nx] > 0: # already visited
                    continue

                stack.append((ny,nx))
                idmap[ny][nx] = id
                extent += 1

        return extent # just for debugging

    num_region = 0
    for y in range(N):
        for x in range(M):
            if A[y][x] == 1 and idmap[y][x] == 0:
                num_region += 1
                extent = mark(y, x, num_region)
                # log('(%d,%d) mark as id %d, area extent %d', y, x, num_region, extent)
    return num_region

solve()


'''
예제 입력 1
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
예제 출력 1
5
1

echo '1\n10 8 17\n0 0\n1 0\n1 1\n4 2\n4 3\n4 5\n2 4\n3 4\n7 4\n8 4\n9 4\n7 5\n8 5\n9 5\n7 6\n8 6\n9 6' | python3 1012.py
-> 5


예제 입력 2
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
예제 출력 2
2

echo '1\n2 2 4\n0 0\n0 1\n1 0\n1 1'  | python3 1012.py
-> 1



(python3 <<EOF
import time,sys
from random import seed,randint
# seed(43)
seed(time.time())
T = 1
print(T)
for _ in range(T):
    M,N = 50,50
    K = randint(1,2500)
    set1 = { (randint(0,N-1), randint(0,M-10)) for k in range(K) }
    K2 = len(set1) # len(set1) can be < K because of redundancy. so update it.
    print(M,N,K2)   ;print(K,K2,file=sys.stderr)
    for y,x in set1:
        print(x,y)
EOF
) | time python3 1012.py


'''

