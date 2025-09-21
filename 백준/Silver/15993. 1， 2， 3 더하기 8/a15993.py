'''
15993번
1, 2, 3 더하기 8, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	1893	1038	857	53.562%

문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 100,000보다 작거나 같다.

출력
각 테스트 케이스마다, n을 나타낼 때 사용한 수의 개수가 홀수인 방법의 수, 짝수인 방법의 수를 공백으로 구분해 출력한다.
방법의 수는 1,000,000,009로 나눈 나머지를 출력해야 한다.


----
1,2,3 더하기 시리즈 문제 중 하나.

특이 조건: n을 만드는 경우의 수를 바로 구하는 것이 아니고
n을 만들 때 사용한 덧셈 항의 수가 홀수인 경우, 짝수인 경우를 나누어서 세기.

기본 코드 구조에 대한 설명은 15592.py 참고.

구현 완료. 예제 검증 완료. 채점 완료.

'''

import sys
# from typing import Generator

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
    Args:
        list of test case. [ n1, n2, .. ]
    Returns:
        answer string list. [ "<cases_odd> <cases_even>", ... ]
    '''
    max_n = max(A)
    # log("max_n: %d", max_n)
    # alloc_n = 100_000
    alloc_n = max(4, max_n)

    dp = [ [0,0] for k in range(alloc_n+1) ]
    # dp[k][0]: 1,2,3 을 짝수개 사용하여 n을 만든 경우의 수
    # dp[k][1]: 홀수개 사용

    # dp[0][*] = 0
    dp[1][0] = 0
    dp[1][1] = 1 # 1

    dp[2][0] = 1 # 1+1
    dp[2][1] = 1 # 2

    dp[3][0] = 2 # 2+1 1+2
    dp[3][1] = 2 # 1+1+1 3

    # dp[4][0] = 4 # 1+1+1+1 3+1 2+2 1+3
    # dp[4][1] = 3 # 2+1+1 1+2+1 1+1+2

    # dp[k] 는 dp[k-1]에 +1, dp[k-2]에 +2, dp[k-3]에 +3 하는 경우가 존재함.
    # 각 경우마다 숫자 하나만을 추가하는 것이므로 홀/짝이 바뀐다는 점에 유의.

    for k in range(4, max_n+1): # k: 4 ~ max_n
        dp[k][0] = (dp[k-1][1] + dp[k-2][1] + dp[k-3][1]) % MOD
        dp[k][1] = (dp[k-1][0] + dp[k-2][0] + dp[k-3][0]) % MOD

    # for n in A:
    #     # yield dp[n][1],dp[n][0]
    #     yield f'{dp[n][1]} {dp[n][0]}'

    return [ f'{dp[n][1]} {dp[n][0]}' for n in A ]

if __name__ == '__main__':
    # print('\n'.join([ f'{b} {a}' for a,b in solve(*get_input()) ]) )
    print('\n'.join( solve(*get_input()) ))



'''
예제 입력 1
3
4
7
10
예제 출력 1
3 4
22 22
137 137

----
run=(python3 a15993.py)

echo '3\n4\n7\n10' | $run
# 3 4
# 22 22
# 137 137

---
echo '5\n1\n2\n3\n4\n5' | $run
# 1 0
# 1 1
# 2 2
# 3 4
# 7 6

echo '3\n100000\n99999\n99998' | $run
# 615575470 615575471
# 211337756 211337756
# 871744821 871744821




'''
