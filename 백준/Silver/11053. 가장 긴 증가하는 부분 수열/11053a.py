'''
다시 풀이

'''

import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve(A:list):
    N = len(A)
    A = [0] + A
    # A[0] 은 특별한 용도로 필요하므로 reserve.

    dp = [0] * (N+1)
    # dp[i] 는 i번째 (1<=i<=N) 숫자를 마지막 숫자로 사용하는 LIS 의 길이

    for i in range(1, N+1):
        # num = A[i]  # 이 단계에서 새로 추가할 숫자

        # A[0:i] 중에서 A[i]를 이어 붙일 수 있는 후보 A[k]들을 검색
        #  대응되는 dp[k]의 최대 값 (길이가 가장 긴 LIS)을 찾음.

        dp[i] = max(dp[k] for k in range(i) if A[k]<A[i]) + 1

        log("A[%d]=%d, %s", i, A[i], dp[:i+1])

    return dp[N]


N = int(input().strip())
A = list(map(int, input().split()))
print(solve(A))


'''
예제 입력 1
6
10 20 10 30 20 50

예제 출력 1
4

run=(python3 11053a.py)

echo '6\n10 20 10 30 20 50' | $run
-> 4

echo '7\n4 5 6 1 2 3 4' | $run
-> 4

echo '7\n4 5 1 6 2 3 7 4 5' | $run
-> 4


'''