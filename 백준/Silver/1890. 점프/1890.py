'''
1890

점프

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	55365	17947	13810	31.251%

문제
N×N 게임판에 수가 적혀져 있다. 이 게임의 목표는 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 점프를 해서 가는 것이다.

각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미한다. 반드시 오른쪽이나 아래쪽으로만 이동해야 한다.
0은 더 이상 진행을 막는 종착점이며, 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야 한다.
한 번 점프를 할 때, 방향을 바꾸면 안 된다. 즉, 한 칸에서 오른쪽으로 점프를 하거나, 아래로 점프를 하는 두 경우만 존재한다.

가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 이동할 수 있는 경로의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 게임 판의 크기 N (4 ≤ N ≤ 100)이 주어진다. 그 다음 N개 줄에는 각 칸에 적혀져 있는 수가 N개씩 주어진다.
칸에 적혀있는 수는 0보다 크거나 같고, 9보다 작거나 같은 정수이며, 가장 오른쪽 아래 칸에는 항상 0이 주어진다.

출력
가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 문제의 규칙에 맞게 갈 수 있는 경로의 개수를 출력한다. 경로의 개수는 263-1보다 작거나 같다.
'''



import sys

def solve_greedy(A:list[list]):

    N = len(A)

    def count(y, x):
        if y == N-1 and x == N-1:
            return 1
        if y < 0 or y >= N or x < 0 or x >= N:
            return 0
        if A[y][x] == 0:
            return 0
        dist = A[y][x]

        # return count(y+dist, x) + count(y, x+dist)

        cnt_d = count(y+dist, x)
        cnt_r = count(y, x+dist)
        cnt = cnt_d + cnt_r

        # print(f'[{y},{x}]:{dist} = {cnt_d} + {cnt_r} = {cnt}')
        return cnt

    return count(0, 0)




def solve(A:list[list]):
    '''
    우 하단 부분 채워 나감.
    채워가는 순서:
        3x3 이라면 다음 순서로.
            8  7  6
            5  4  3
            2  1  0
    '''
    N = len(A)
    C = [ [0 for x in range(N)] for y in range(N) ]

    C[N-1][N-1] = 1

    for y in range(N-1, -1, -1):
        for x in range(N-1, -1, -1):
            if A[y][x] == 0: # cannot move
                continue
            dist = A[y][x]

            count = 0
            # 아래방향 점프
            if y+dist < N: # and C[y+dist][x] != -1:
                count += C[y+dist][x]
            # 오른쪽 방향 점프
            if x+dist < N: # and C[y][x+dist] != -1:
                count += C[y][x+dist]

            C[y][x] = count

    # for c in C:
    #     print(c, file=sys.stderr)

    return C[0][0]


N = int(input().strip())
A = []
for _ in range(N):
    A.append(list(map(int, input().strip().split())))
# print(A, file=sys.stderr)

print(solve(A))
# print(solve_greedy(A))


'''
예제 입력 1
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0

예제 출력 1
3

5
1 2 1 2 1
2 1 2 1 2
1 1 1 2 1
2 1 2 1 2
1 2 2 1 0

4
1 0 0 0
1 1 1 0
0 0 1 0
0 0 1 0

4
1 0 0 0
1 1 0 0
0 0 1 0
0 0 1 0


시간 측정

(N=10 python3 <<EOF
import time,os
from random import seed,randint
seed(time.time())
N = int(os.getenv('N', 10))
print(N)
for k in range(N):
    a = [ str(randint(1, 2)) for _ in range(N) ]
    if k == N-1:
        a[N-1] = '0'
    print(' '.join(a))
EOF
) | time python3 a.py

python3 a.py  0.31s user 0.02s system 99% cpu 0.335 total

N 이 17 부터는 느려지는 게 확실히 보임.

'''