
import sys
input = sys.stdin.readline


def solve(A:list[str]):
    N = len(A)
    assert len(A[0]) == N

    # A를 좌상단 1씩 여백 확장. 단순이 인덱스 맞추기 위함이니 내용은 상관 없음.
    A[:0] = [ '.' * (N+1) ] # insert row
    for k in range(1, N+1): # extend each row
        A[k] = '.' + A[k]

    dp = [ [ [0,0,0] for c in range(N+1) ] for r in range(N+1) ]
    # dp[r][c][type]
    # type  0:가로, 1:세로, 2:대각선
    dp[1][2][0] = 1 # 초기 상태

    for r in range(1, N+1):
        cs,ce = (1,N) if r>1 else (3,N)
        for c in range(cs, ce+1):
            if A[r][c] == '0':
                dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2] # 가로
                dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2] # 세로
            if A[r][c] == '0' and A[r][c-1] == '0' and A[r-1][c] == '0':
                dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]
    return sum(dp[N][N])



N = int(input().strip())
A = []
for _ in range(N):
    A.append(input().strip().replace(' ', ''))

print(solve(A))
