'''
15990번
1, 2, 3 더하기 5 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	34053	11508	8199	31.065%

문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.

1+2+1
1+3
3+1

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 100,000보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.


--------
코딩, 17분

'''

import sys
input = sys.stdin.readline

MAX_N = 100_000
# n은 양수이며 100,000보다 작거나 같다.

MOD = 1_000_000_009

'''
dp[k]: 정수 k를 1,2,3 의 합으로 나타내는 방법의 수 계산에 필요한 정보
    dp[k][0]: 위 조건의 수 중 끝자리가 1로 끝나는 경우의 수
    dp[k][1]: 위 조건의 수 중 끝자리가 2로 끝나는 경우의 수
    dp[k][2]: 위 조건의 수 중 끝자리가 3로 끝나는 경우의 수
dp[0] 은 미사용.
'''
dp = [ [0,0,0] for k in range(MAX_N+1) ]

dp[1] = [ 1, 0, 0 ] # 1
dp[2] = [ 0, 1, 0 ] # 2
dp[3] = [ 1, 1, 1 ] # 1+2, 2+1, 3

dp_valid_until = 3

def solve(N):
    '''

    '''
    global dp, dp_valid_until

    if dp_valid_until < N:
        # populate dp[] until index N
        #
        for n in range(dp_valid_until+1, N+1):
            dp[n][0] = (dp[n-1][1] + dp[n-1][2]) % MOD # +1 를 하려면 끝자리 1은 사용할 수 없음.
            dp[n][1] = (dp[n-2][0] + dp[n-2][2]) % MOD # +2 하는 경우
            dp[n][2] = (dp[n-3][0] + dp[n-3][1]) % MOD # +3 하는 경우

        dp_valid_until = N

    return sum(dp[N]) % MOD

# main

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(solve(N))



'''
예제 입력 1
3
4
7
10

예제 출력 1
3
9
27


4
100000
100000
33019
3

-> 437690554
-> 724163842


'''
