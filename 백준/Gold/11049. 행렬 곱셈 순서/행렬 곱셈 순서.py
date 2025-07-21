import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve_dp(A:list[tuple[int,int]])->int:
    '''

    '''
    N = len(A)
    # A 목록에는 총 N 개의 행렬이 존재. A[0]..A[N-1]

    INF = 2**31

    dp = [ [INF]*N for k in range(N) ]
    # dp[i][k] 는 행렬 A[i] 부터 A[k] 까지의 부분 행렬 리스트 만의 행렬 곱 최소 계산량

    # diff == 0
    for i in range(N):
        dp[i][i] = 0

    # distance 가 1, 부분 행렬의 길이가 2.
    # (ri1 x ci1) 행렬과 (ri2 x ci2) 행렬의 곱.
    #   ci1 == ri2 이어야 하며
    # 계산량은 ri1 x ci1 x ci2 로 고정된 수식.
    for i in range(N-1):
        dp[i][i+1] = A[i][0] * A[i][1] * A[i+1][1]

    for d in range(2, N):  # 1 ~ N-1
        # d (diff) 는 부분 행렬의 길이 - 1

        for k in range(d, N): # d ~ N-1
            i = k - d
            '''
            x  0  1  2  3  4  5  .. -> k
            0  0  01 02 03 04 05 ..
            1  _  0  12 13 14 15
            2  _  _  0  23 24 25
            3  _  _  _  0  34 35  |
            4  _  _  _  _  0  45  v i
            5  _  _  _  _  _  0
            ..
            dp[i][k]:
                A[i] 부터 A[k] 의 부분 행렬들의 행렬 곱을 생각할 때
                    A[i] * A[i+1] * .. * A[k]
                이 부분 행렬 곱 계산시 계산량의 최소값.

            a_i 부터 시작해서 a_k 로 끝나는 부분 행렬 곱
                a_i   a_{i+1}   a_{i+2}   ..  a_{k-1}   a_k
                    ^         ^         ^             ^
            j       i         i+1       i+2           k-1

            최종 행렬 곱 연산이 수행되는 위치를 j 라고 하고
            다음과 같이 가능한 모든 j 경우 중 최소 값을 선택하여 dp 에 저장.
            j=i
                i / i+1   -> (dp[i][i]) + dp[i+1][k] + r_i*c_i*c_k
            j=i+1
                i+1 / i+2 -> dp[i][i+1] + dp[i+2][k] + r_i*c_{i+1}*c_k
                ...
            j=k-1
                k-1 / k   -> dp[i][k-1] + (dp[k-1][k-1]) + r_i*c_{k-1}*c_k
            '''

            minval = INF
            for j in range(i, k):
                val = dp[i][j] + dp[j+1][k] + A[i][0]*A[j][1]*A[k][1]
                if val < minval: minval = val
            dp[i][k] = minval
        pass

    return dp[0][N-1]


N = int(input().strip())
A = []
for _ in range(N):
    r,c = map(int, input().split())
    #if A:
    #    assert A[-1][1] == r, "row/col mismatch"
    A.append((r, c))

print(solve_dp(A))
