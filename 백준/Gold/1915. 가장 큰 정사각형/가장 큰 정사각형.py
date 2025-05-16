
import sys
input = sys.stdin.readline

#def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve(arr:list[str]):
    N,M = len(arr),len(arr[0])
    dp = [ [ 0 for x in range(M+1) ] for y in range(N+1) ]
    # dp[y][x] 는 (y,x) 위치를 우하단으로 하는 최대 정사각형의 한변의 길이
    max_area = 0
    for y in range(1, N+1):
        for x in range(1, M+1):
            if arr[y-1][x-1] == '1':
                dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1
            max_area = max(max_area, dp[y][x]**2)
        # log('[%d] %s, max %d', y, dp[y], max_area)
    return max_area

N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input().strip())
    assert len(arr[-1]) == M

print(solve(arr))
