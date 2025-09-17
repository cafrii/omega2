'''
4883번
삼각 그래프 다국어, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	12350	3375	2670	26.446%

문제
이 문제는 삼각 그래프의 가장 위쪽 가운데 정점에서 가장 아래쪽 가운데 정점으로 가는 최단 경로를 찾는 문제이다.

삼각 그래프는 사이클이 없는 그래프로 N ≥ 2 개의 행과 3열로 이루어져 있다.
삼각 그래프는 보통 그래프와 다르게 간선이 아닌 정점에 비용이 있다.
어떤 경로의 비용은 그 경로에서 지나간 정점의 비용의 합이다.

오른쪽 그림은 N = 4인 삼각 그래프이고,
가장 위쪽 가운데 정점에서 가장 아래쪽 가운데 정점으로 경로 중 아래로만 가는 경로의 비용은 7+13+3+6 = 29가 된다.
삼각 그래프의 간선은 항상 오른쪽 그림과 같은 형태로 연결되어 있다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 그래프의 행의 개수 N이 주어진다. (2 ≤ N ≤ 100,000)
다음 N개 줄에는 그래프의 i번째 행에 있는 정점의 비용이 순서대로 주어진다.
비용은 정수이며, 비용의 제곱은 1,000,000보다 작다.

입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 테스트 케이스에 대해서, 가장 위쪽 가운데 정점에서 가장 아래쪽 가운데 정점으로 가는 최소 비용을
테스트 케이스 번호와 아래와 같은 형식으로 출력한다.

k. n
k는 테스트 케이스 번호, n은 최소 비용이다.


---------

9:41~9:55

채점 통과


'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    C = [] # test cases
    while True:
        N = int(input().rstrip())
        if N == 0: break
        A = []
        for _ in range(N):
            a,b,c = map(int, input().split())
            A.append([a,b,c])
        C.append(A)
    return C,

def solve(A:list[list[int]])->int:
    '''
    Args: A: cost matrix, dim: N by 3
    Returns: min cost, from G[0][1]->G[N-1][1]
    '''
    MAX_C = 1000
    N = len(A)

    dp = [ [0,0,0] for _ in range(N) ]
    # dp[k][j]: accululated cost at graph location of row k, column j

    dp[0][0] = MAX_C #A[0][0]
    dp[0][1] = A[0][1]
    dp[0][2] = A[0][1] + A[0][2]

    # k = 0
    # log("[%d] %s", k, dp[k])

    for k in range(1, N): # k: 1 ~ N-1
        dp[k][0] = min( dp[k-1][0], dp[k-1][1] ) + A[k][0]
        dp[k][1] = min( dp[k][0], dp[k-1][0], dp[k-1][1], dp[k-1][2] ) + A[k][1]
        dp[k][2] = min( dp[k][1], dp[k-1][1], dp[k-1][2] ) + A[k][2]

        # log("[%d] %s", k, dp[k])

    return dp[N-1][1]


if __name__ == '__main__':
    C, = get_input()
    print('\n'.join( f'{i+1}. {solve(c)}' for i,c in enumerate(C) ))



'''
예제 입력 1
4
13 7 5
7 13 6
14 3 12
15 6 16
0
예제 출력 1
1. 22

---
run=(python3 a4883.py)

echo '4\n13 7 5\n7 13 6\n14 3 12\n15 6 16\n0' | $run
# 1. 22


'''

