'''
15991번
1, 2, 3 더하기 6, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	3419	1679	1362	47.806%

문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다.
합을 나타낼 때는 수를 1개 이상 사용해야 한다. 단, 합은 대칭을 이루어야 한다.

1+1+1+1
1+2+1
2+2

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.
n은 양수이며 100,000보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.


----

12:24~12:45  채점까지 ok

----
1,2,3 더하기 시리즈 문제 중 하나.
특이 조건: 더하기 식이 좌우 대칭 형태인 것만 포함하기

일단은 구현 및 예제 확인 완료.
검증 완료.

'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

MOD = 1_000_000_009

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    A = []
    for _ in range(C):
        n = int(input().rstrip())
        A.append(n)
    return A,

def solve(A:list[int])->list[str]:
    '''
    Returns: answer. list of string.
    '''
    max_n = max(A)
    alloc_n = max(max_n, 5)
    dp = [0]*(alloc_n + 1)

    '''
    dp[k]는 다음과 같은 조합으로 생성될 수 있음.
        dp[k-2] 의 양쪽에 1+...+1 을 더하기
        dp[k-4] 의 양쪽에 2+...+2
        dp[k-6] 의 양쪽에 3+...+3
    dp[6] 까지는 미리 구해두고, dp[7] 부터 점화식.
    '''

    dp[0] = 1  # 이 자체는 정답에 사용이 안되지만 x+?+x 형태로 계산에는 사용될 수 있음.
    dp[1] = 1  # 1
    dp[2] = 2  # 1+1  2
    dp[3] = 2  # 1+1+1  3
    dp[4] = 3  # 1+1+1+1 1+2+1  2+2
    dp[5] = 3  # 1+1+1+1+1 1+3+1  2+1+2
    # dp[6] = 6 # 1+1+1+1+1+1 1+1+2+1+1 1+2+2+1  2+1+1+2 2+2+2  3+3

    for k in range(6, max_n+1):
        dp[k] = (dp[k-2] + dp[k-4] + dp[k-6]) % MOD
        # log("dp[%d]: %s", k, dp[k])
    ans = [ str(dp[n]) for n in A ]
    return ans

if __name__ == '__main__':
    # r = solve(*get_input())
    # print('\n'.join(map(str, r)))
    print('\n'.join(solve(*get_input())))


'''
예제 입력 1
3
4
7
10
예제 출력 1
3
6
20
---

run=(python3 15991.py)

echo '3\n4\n7\n10' | $run
# 3
# 6
# 20

---
echo '5\n1\n2\n3\n4\n5' | $run
# 1 2 2 3 3

echo '2\n100000\n99999' | $run
# 483652833
# 136937594

'''
