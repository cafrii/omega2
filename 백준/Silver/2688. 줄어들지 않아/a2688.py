'''
2688번
줄어들지 않아 다국어, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	7582	4111	3462	53.098%

문제
어떤 숫자가 줄어들지 않는다는 것은 그 숫자의 각 자리 수보다 그 왼쪽 자리 수가 작거나 같을 때 이다.

예를 들어, 1234는 줄어들지 않는다.

줄어들지 않는 4자리 수를 예를 들어 보면 0011, 1111, 1112, 1122, 2223이 있다.
줄어들지 않는 4자리수는 총 715개가 있다.

이 문제에서는 숫자의 앞에 0(leading zero)이 있어도 된다.
0000, 0001, 0002는 올바른 줄어들지 않는 4자리수이다.

n이 주어졌을 때, 줄어들지 않는 n자리 수의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T(1 <= T <= 1,000)이 주어진다.
각 테스트 케이스는 숫자 하나 n으로 이루어져 있다. (1 <= n <= 64)

출력
각 테스트 케이스에 대해 한 줄에 하나씩 줄어들지 않는 n자리 수의 개수를 출력한다.

-----
10:11~10:22

채점 확인.

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    A = []
    for _ in range(C):
        A.append(int(input().rstrip()))
    return A,

def solve(A:list[int])->list[int]:
    '''
    '''
    MAX_N = 64
    # N = len(A)
    max_n = max(A) # real max

    dp = [ [0]*10 for _ in range(MAX_N+1) ]
    # dp[k][j]는 길이 k 인 non-decreasing 숫자들 중, 끝자리가 j 인 것들의 개수

    dp[1] = [1]*10  # 길이가 1이면 한 가지 경우 밖에 없음. 그냥 그 숫자.

    for k in range(2, max_n+1):
        # dp[k][0] = dp[k-1][0]
        # dp[k][1] = dp[k-1][0] + dp[k-1][1]
        # ...
        for j in range(10): # j: 0 ~ 9
            dp[k][j] = sum( dp[k-1][:j+1] )

    # ans = []
    # for a in A:
    #     ans.append(sum(dp[a]))
    # return ans

    return [ sum(dp[a]) for a in A ]

if __name__ == '__main__':
    # R = solve(*get_input())
    # for r in R: print(r)

    print('\n'.join(map(str, solve(*get_input()))))


'''
예제 입력 1
3
2
3
4
예제 출력 1
55
220
715

---
run=(python3 a2688.py)

echo '3\n2\n3\n4' | $run
# 55 220 715

echo '2\n1\n64' | $run
# 10 97082021465


'''

