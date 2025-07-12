import math
import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve_dp(N:int)->int:
    dp = [9]*(N+1)
    dp[1] = 1

    # populate power of integers
    is_power_num = [0]*(N+1)  # 0~N
    for i in range(1,int(math.sqrt(N))+1):
        i2 = i*i
        if i2 <= N:
            is_power_num[i2] = i

    for i in range(2, N+1):
        # check if i is square number
        if is_power_num[i]:
            dp[i] = 1
            # log("[%d]: -> %d", i, dp[i])
            continue

        # i-1 부터 0을 향해 거슬러 올라가면서 검색
        candidates = []
        for k in range(1,i):
            n = i - k*k
            if n < 1: break
            candidates.append(dp[n])

            # pruning. 자체 제곱수가 아닌 이상, 후보에서 1이 나오면 그게 최선이다.
            if dp[n]==1: break

        dp[i] = min(candidates)+1
        # log("[%d]: %s -> %d", i, candidates, dp[i])

    return dp[N]


'''
solve_dp 가 시간 제한 초과하여 좀 더 최적화.

-> 내 pc 에선 시간 내 완료 되는데 온라인 채점에선 시간 초과됨.

'''
def solve_optimized(N: int) -> int:
    dp = [9] * (N + 1)
    dp[0:1] = [0,1]

    # 제곱수들을 미리 계산
    squares = []
    is_squares = [0]*(N+1)
    for i in range(1, int(math.sqrt(N)) + 1):
        i2 = i*i
        squares.append(i2)
        if i2 <= N: is_squares[i2] = i

    for i in range(2, N + 1):
        # 제곱수인지 빠르게 확인
        if is_squares[i]:
            dp[i] = 1
            continue

        # 최솟값을 직접 추적
        min_count = 9
        # 제곱수 리스트를 사용하여 더 효율적으로 탐색
        for square in squares:
            if square >= i:
                break
            remaining = i - square
            min_count = min(min_count, dp[remaining])
            if min_count == 1:
                break

        dp[i] = min_count + 1

    return dp[N]


'''

'''
def solve_fast(N: int) -> int:

    def is_square(n):
        # n이 완전제곱수인지.
        sqrt_n = int(math.sqrt(n))
        return sqrt_n * sqrt_n == n

    def is_sum_of_two_squares(n):
        # n이 두 제곱수의 합으로 표현 가능한지.
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            remaining = n - i * i
            if remaining > 0 and is_square(remaining):
                return True
        return False

    def is_sum_of_three_squares(n):
        # n이 세 제곱수의 합으로 표현 가능한지.
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            remaining = n - i * i
            if remaining > 0 and is_sum_of_two_squares(remaining):
                return True
        return False

    if is_square(N):
        return 1
    if is_sum_of_two_squares(N):
        return 2
    if is_sum_of_three_squares(N):
        return 3
    return 4



N = int(input().strip())
# print(solve_dp(N))
# print(solve_optimized(N))
print(solve_fast(N))
