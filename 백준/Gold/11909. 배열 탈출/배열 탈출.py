import sys

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

if __name__ == '__main__':
    print(solve(*get_input()))
