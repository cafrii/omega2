
def get_input():
    import sys
    input = sys.stdin.readline
    N,M = map(int, input().split()) # N행, M열
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
        #assert len(A[-1]) == M
    return N,M,A

def solve(N:int, M:int, A:list[list[int]])->int:
    '''
    Args:
        A: N by M matrix with 0 or 1 element. 1 is safe.
    Returns:
        possible safe paths mode mod MOD
    '''
    MOD = 1_000_000_007

    # 아래에서 위, 또는 위에서 아래 상관 없음. 나는 위에서 아래로..
    # x축 (행)의 양 끝 계산의 편의를 위해 양쪽에 빈 공간을 둔다. 폭이 M+2 라고 가정.

    dp = [ [0]*(M+2) for _ in range(N) ]
    # 하나의 행 dp[y][..]는 [0]부터 [M+1]까지 총 M+2 의 폭을 가진다.
    # 이 중에서 양 끝 [0]과 [M+1]은 항상 0의 값을 가진다.

    # 첫번째 행은 강화유리 여부가 경로 수와 같음.
    dp[0][1:M+1] = A[0]

    for y in range(1, N):  # y: 1 ~ N-1
        for x in range(1, M+1):  # x: 1 ~ M
            if A[y][x-1] == 0: continue # 강화 유리 아님
            dp[y][x] = (dp[y-1][x-1] + dp[y-1][x] + dp[y-1][x+1]) % MOD

    return sum(dp[N-1]) % MOD

if __name__ == '__main__':
    print(solve(*get_input()))
