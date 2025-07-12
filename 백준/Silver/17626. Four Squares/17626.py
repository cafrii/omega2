'''
17626번
Four Squares 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초 (추가 시간 없음)	512 MB	40042	17671	13978	43.902%

문제
라그랑주는 1770년에 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명하였다.
어떤 자연수는 복수의 방법으로 표현된다.
예를 들면, 26은 52과 12의 합이다; 또한 42 + 32 + 12으로 표현할 수도 있다.

역사적으로 암산의 명수들에게 공통적으로 주어지는 문제가 바로 자연수를 넷 혹은 그 이하의 제곱수 합으로 나타내라는 것이었다.
1900년대 초반에 한 암산가가 15663 = 1252 + 62 + 12 + 12라는 해를 구하는데 8초가 걸렸다는 보고가 있다.
좀 더 어려운 문제에 대해서는 56초가 걸렸다: 11339 = 1052 + 152 + 82 + 52.

자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램을 작성하시오.

입력
입력은 표준입력을 사용한다. 입력은 자연수 n을 포함하는 한 줄로 구성된다. 여기서, 1 ≤ n ≤ 50,000이다.

출력
출력은 표준출력을 사용한다. 합이 n과 같게 되는 제곱수들의 최소 개수를 한 줄에 출력한다.


----

10:06~45



'''


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





'''
run=(python3 17626.py)

예제 입력 1
25
예제 출력 1
1
예제 입력 2
26
예제 출력 2
2
예제 입력 3
11339
예제 출력 3
3
예제 입력 4
34567
예제 출력 4
4

echo '34567' | time $run 2> /dev/null

echo '50000' | time $run 2> /dev/null

'''
