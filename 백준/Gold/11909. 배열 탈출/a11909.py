'''
11909번
배열 탈출 성공, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	2806	1143	859	39.658%

문제
상수는 2차원 배열 A[1..n][1..n] (n≥2, n은 자연수)을 가지고 있습니다.
이 배열의 각 원소는 1 이상 222 이하의 정수입니다.

배열을 가지고 놀던 상수를 본 승현이는, 질투심이 불타올라 상수를 A[1][1]에 가둬 버렸습니다!
최소한의 양심이 있던 승현이는 A[n][n]에 출구를 만들어 놓고 이 사실을 상수에게 알려줬습니다.

[그림 1] n=4라면 상수는 A[1,1]에 있고, 출구는 A[4][4]에 있습니다.

상수는 가능한 한 빨리 출구인 A[n][n]에 도달하고자 합니다.
상수가 A[i][j]에 있다고 가정했을 때, 상수는 최단 경로로 이동하기 위해 아래와 같은 조건을 만족하며 이동합니다.

1≤i,j<n이라면, 상수는 A[i][j+1] 또는 A[i+1][j]로만 건너갑니다.
i=n,1≤j<n이라면, A[i][j+1]로만 건너갑니다.
1≤i<n,j=n이라면 A[i+1][j]로만 건너갑니다.
i=j=n인 경우 바로 출구로 갑니다.

[그림 2] n=5라고 가정합시다. (ㄱ)는 1번 조건을 만족하고, (ㄴ)는 2번 조건을 만족하며, (ㄷ)는 3번 조건을 만족합니다.

그러나 건너갈 때에도 제약이 따릅니다.
상수가 A[a][b]에서 A[c][d]로 건너가려면 A[a][b]>A[c][d]를 만족해야 합니다.
상수는 왜인지 이런 조건을 만족하면서 이동할 수 없을 것 같았습니다.
다행히도, 승현이가 상수를 배열에 가둬버리기 전에, 상수는 배열의 각 원소에 버튼을 만들어 놓아서,
이 버튼을 누르면 해당 원소의 값이 1 증가하도록 했습니다.
(물론 상수는 자신이 위치해 있는 원소의 버튼만 누를 수 있습니다.)
이 버튼 덕분에, 상수는 항상 배열을 탈출할 수 있습니다!

[그림 3] n=2라고 가정합시다. A[1][1]=5>A[1][2]=2이므로, 상수는 A[1][1]에서 A[1][2]로 건너갈 수 있습니다.
상수가 A[1][1]에서 A[2][1]로 건너가려면, A[1][1]에 있는 버튼을 두 번 눌러 A[1][1]의 값을 7로 만들면 됩니다.

하지만 버튼을 한 번 누르는 데에는 1원의 비용이 듭니다.
상수는 돈을 가능한 한 적게 들이면서 배열을 탈출하고자 합니다. 상수를 도와주세요.

입력
첫 번째 줄에 n이 주어집니다. (n ≤ 2,222)

다음에 n개 줄이 주어집니다.
이 중 i(1≤i≤n)번째 줄에는 n개의 수 A[i][1],A[i][2],⋯,A[i][n-1],A[i][n]이 공백을 사이로 두고 차례대로 주어집니다.

출력
첫 번째 줄에 상수가 배열을 탈출하기 위해 들여야 할 최소 비용(원 단위)을 출력합니다.

--------

2025/9/19, 7:46~

--------
그냥 평범하게 2d-dp 로 풀면 된다. 대략 2~3초 내에서 pass 된다.


'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
        # assert len(A[-1]) == N
    return N,A


def solve(N:int, A:list[list[int]])->int:
    '''
    Args:
        A: matrix to escape. NxN
    Returns:
        minimum costs (total number of button presses)
    '''

    dp = [ [0]*(N) for _ in range(N) ]
    # dp[y][x] 는 (0,0) 에서 (y,x) 위치까지 오기 까지 필요로 하는 버튼 누름 수
    # dp[0][0] 은 0 이다.

    y = 0
    for x in range(1, N):
        costx = A[y][x] - A[y][x-1] + 1
        dp[y][x] = dp[y][x-1] + (costx if costx >= 0 else 0)
    x = 0
    for y in range(1, N):
        costy = A[y][x] - A[y-1][x] + 1
        dp[y][x] = dp[y-1][x] + (costy if costy >= 0 else 0)

    for y in range(1, N):
        for x in range(1, N):
            costx = A[y][x] - A[y][x-1] + 1
            costy = A[y][x] - A[y-1][x] + 1
            dp[y][x] = min(
                dp[y][x-1] + (costx if costx >= 0 else 0),
                dp[y-1][x] + (costy if costy >= 0 else 0),
            )
    return dp[N-1][N-1]


'''
그래프 탐색 알고리즘 (변형 BFS) 로 시도
정답은 제대로 출력하지만 대체로 시간이 dp 에 비해 더 소요된다.
그래서 이 답안은 제출하지 않았음.

'''

from heapq import heappush,heappop

def solve2_bfs(N:int, A:list[list[int]])->int:
    '''
    Args:

    Returns:

    '''

    INF = int(1e10)  # 222 * 2222 * 2222 + 1
    mc = [ [INF]*N for _ in range(N) ]  # min cost

    que = [ (0,0,0) ]
    # max length:
    #  2222 * 2222 = 5M
    #  sizeof(e) = 3xsizeof(int) = 24
    #  total 120M

    cost = 0
    while que:
        cost,y,x = heappop(que)
        log("(%d, %d) cost %d, A %d", y, x, cost, A[y][x])

        if y == N-1 and x == N-1:
            log("reached to exit")
            break
        if cost >= mc[y][x]: # already visited with smaller cost
            continue
        mc[y][x] = cost
        a = A[y][x]

        if x < N-1:
            cx = A[y][x+1] - a + 1
            ncx = cost + (cx if cx>=0 else 0)
            if ncx < mc[y][x+1]:
                log("    (%d, %d) ncx %d, override %d", y, x+1, ncx, mc[y][x+1])
                heappush(que, (ncx, y, x+1))
        if y < N-1:
            cy = A[y+1][x] - a + 1
            ncy = cost + (cy if cy>=0 else 0)
            if ncy < mc[y+1][x]:
                log("    (%d, %d) ncy %d, override %d", y+1, x, ncy, mc[y+1][x])
                heappush(que, (ncy, y+1, x))
    return cost


if __name__ == '__main__':
    print(solve(*get_input()))
    # print(solve2_bfs(*get_input()))



#-------------------------

import time,os
from random import seed,randint,shuffle

def gen_worstcase_input():
    seed(time.time())
    seed(43)
    N = int(os.getenv('_N', '10'))
    A = [ [ randint(1,22) for x in range(N) ] for y in range(N) ]
    return N,A

def test():
    N,A = gen_worstcase_input()
    print(N)
    print('\n'.join( ' '.join(map(str, ln)) for ln in A ))




'''
예제 입력 1
4
5 2 4 3
6 5 1 2
3 4 5 3
7 4 3 1
예제 출력 1
3

예제 입력 2
5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
예제 출력 2
8

----
run=(python3 a11909.py)


echo '4\n5 2 4 3\n6 5 1 2\n3 4 5 3\n7 4 3 1' | $run
# 3

echo '5\n1 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1\n1 1 1 1 1' | $run
# 8

----
worst case simulation

_N=10 python3 -c "from a11909 import test; test()" | time $run

# _N=1000
# 4000
# $run  0.34s user 0.01s system 52% cpu 0.661 total  # solve()
# $run  1.16s user 0.02s system 78% cpu 1.491 total  # solve2_bfs

# _N=2222
# 8864
# $run  1.61s user 0.05s system 52% cpu 3.198 total  # solve()
# $run  6.15s user 0.09s system 79% cpu 7.808 total  # solve2_bfs


'''


