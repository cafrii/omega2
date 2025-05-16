'''
11057번

오르막 수 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	62524	30745	23870	47.760%

문제
오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.

예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.

수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

입력
첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

출력
첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.


15분

'''

import sys
input = sys.stdin.readline

# MAX_N = 1000
MOD = 10007

def solve_0(N):
    # N==1 일 때의 각 끝자리 별 경우의 수
    dp = [1]*10  # answer for N==1
    prev = [0]*10

    for k in range(2, N+1):
        prev,dp = dp,prev
        for j in range(10):
            dp[j] = sum(prev[:j+1]) % MOD

    return sum(dp) % MOD

def solve(N):
    # N==1 일 때의 각 끝자리 별 경우의 수
    dp = [1]*10  # answer for N==1

    for k in range(2, N+1):
        for j in range(9,-1,-1):
            dp[j] = sum(dp[:j+1]) % MOD

    return sum(dp) % MOD


N = int(input().strip())
print(solve(N))



'''
예제 입력 1
1
예제 출력 1
10
예제 입력 2
2
예제 출력 2
55
예제 입력 3
3
예제 출력 3
220
'''

