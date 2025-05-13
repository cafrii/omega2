'''
11660번

구간 합 구하기 5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	93625	43113	31790	44.086%

문제

N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

1	2	3	4
2	3	4	5
3	4	5	6
4	5	6	7

여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

입력
첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000)
둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다.
다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다.
표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

출력
총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

약 30분.

'''

import sys
input = sys.stdin.readline


def solve(A):
    ''' calculate partial sum matrix
        which is the sum of (0,0)~(y,x) elements for each (y,x).
        return the partial matrix.
    '''
    H,W = len(A),len(A[0])
    psum = [[0 for x in range(W)] for y in range(H)]
    # for y == 0
    psum[0][0] = A[0][0]
    for x in range(1,W):
        psum[0][x] = psum[0][x-1] + A[0][x]

    for y in range(1,H):
        psum[y][0] = psum[y-1][0] + A[y][0]
        for x in range(1,W):
            psum[y][x] = psum[y-1][x] + (psum[y][x-1] - psum[y-1][x-1]) + A[y][x]

    return psum


N,M = map(int, input().split())

# A[0][] and A[][0] is zero-filled.
A = [ [0]*(N+1) ]
for y in range(N):
    A.append([0] + list(map(int, input().split())))


psum = solve(A)
# for a in psum:
#     print(' '.join([ f'{e:2}' for e in a ]))

for m in range(M):
    # y가 행, x가 열로 naming.
    y1,x1,y2,x2 = map(int, input().split())
    answer = psum[y2][x2] - psum[y1-1][x2] - psum[y2][x1-1]+ psum[y1-1][x1-1]
    print(answer)


'''


echo '4 3\n1 2 3 4\n2 3 4 5\n3 4 5 6\n4 5 6 7\n2 2 3 4\n3 4 3 4\n1 1 4 4' | python3 11660.py
-> 27 6 64

예제 입력 1
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
예제 출력 1
27
6
64

예제 입력 2
2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2
예제 출력 2
1
2
3
4

'''