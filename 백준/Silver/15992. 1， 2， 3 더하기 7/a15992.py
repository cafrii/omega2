'''
15992번
1, 2, 3 더하기 7, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.25 초	512 MB	2608	1355	1087	52.512%

문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1

정수 n과 m이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
단, 사용한 수의 개수는 m개 이어야 한다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n과 m이 주어진다.
n은 양수이며 1,000보다 작거나 같다. m도 양수이며, n보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.
단, 사용한 수의 개수는 m개 이어야 한다.

----

9:38~10:11

----
1,2,3 더하기 시리즈 문제 중 하나.
특이 조건은 지정한 숫자 m개 만 사용하는 경우만 찾는 것.

검증 완료.

'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

MOD = 1_000_000_009
MAX_N = 1000

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    A = []
    for _ in range(C):
        n,m = map(int, input().split())
        A.append((n,m))
    return A,


def solve(A:list[tuple[int,int]])->list[int]:
    '''
    초기 구현
    '''
    max_n = max(A, key=lambda x:x[0])[0]

    # log("max_n: %d", max_n)

    dp = [ [0]*(k+1) for k in range(max_n+1) ]
    # 삼각형 형태로 할당. 나름 필요한 영역만 할당하겠다는 전략인데..
    # 사실 이게 나중에 구현 복잡도를 높이고 있음!

    dp[1][1] = 1 # 1

    dp[2][1] = 1 # 2
    dp[2][2] = 1 # 1+1

    dp[3][1] = 1 # 3
    dp[3][2] = 2 # 1+2 2+1
    dp[3][3] = 1 # 1+1+1

    dp[4][1] = 0
    dp[4][2] = 3 # 1+3 2+2 3+1       # dp[3][1]+dp[2][1]+dp[1][1]
    dp[4][3] = 3 # 1+1+2 1+2+1 2+1+1 # dp[3][2]+dp[2][2]+dp[1][2]
    dp[4][4] = 1 # 1+1+1+1

    # dp[5][1] = 0          # dp[4][0]+dp[3][0]+dp[2][0]
    # dp[5][2] = 3 #0+1+1   # dp[4][1]+dp[3][1]+dp[2][1]
    # dp[5][3] = 6 #3+2+1   # dp[4][2]+dp[3][2]+dp[2][2]
    # dp[5][4] = 4 #3+1     # dp[4][3]+dp[3][3]
    # dp[5][5] = 1          # dp[4][4] = 1

    # dp[6][1] = dp[5][0]+dp[4][0]+dp[3][0]
    # dp[6][2] = dp[5][1]+dp[4][1]+dp[3][1]
    # dp[6][3] = dp[5][2]+dp[4][2]+dp[3][2]
    # dp[6][4] = dp[5][3]+dp[4][3]+dp[3][3]
    # dp[6][5] = dp[5][4]+dp[4][4]
    # dp[6][6] = dp[5][5]

    for k in range(5,max_n+1):
        # dp[k][1] = 0
        for j in range(k, 0, -1): # j: k ~ 1
            dp[k][j] = 0   # what we should find out
            for i in range(k-1, k-4, -1):  # i: k-1, k-2, k-3
                if i >= j-1:
                    dp[k][j] += dp[i][j-1]
            dp[k][j] %= MOD
        log("dp[%d]: %s", k, dp[k])

    ans = [ dp[n][m] for n,m in A ]
    return ans


def solve2(A:list[tuple[int,int]])->list[int]:
    '''
    좀 더 개선된 버전. 2d dp map을 삼각형 꼴이 아닌 정사각형 폼으로 할당
    j 루프 중간에 더 이상 계산할 의미가 없는 조건이 되면 loop-out
    '''
    max_n = max(A, key=lambda x:x[0])[0]

    log("max_n: %d", max_n)

    dp = [ [0]*(max_n+1) for k in range(max_n+1) ]
    # dp[k][j] 는 1,2,3 을 j 개 사용하여 숫자 k를 만드는 방법의 수.

    dp[1][1] = 1 # 1

    dp[2][1] = 1 # 2
    dp[2][2] = 1 # 1+1

    dp[3][1] = 1 # 3
    dp[3][2] = 2 # 1+2 2+1
    dp[3][3] = 1 # 1+1+1

    for k in range(4,max_n+1): # k: 4 ~ max_n
        for j in range(k, 0, -1): # j: k ~ 1
            dp[k][j] = (dp[k-1][j-1] + dp[k-2][j-1] + dp[k-3][j-1]) % MOD
            if dp[k][j] == 0: break # early exit

        log("dp[%d]: %s", k, dp[k][:k+1])

    ans = [ dp[n][m] for n,m in A ]
    return ans

'''
n == 10 일 때, dp 형태.
dp[4] : [0, 0, 3, 3, 1]
dp[5] : [0, 0, 2, 6, 4, 1]
dp[6] : [0, 0, 1, 7, 10, 5, 1]
dp[7] : [0, 0, 0, 6, 16, 15, 6, 1]
dp[8] : [0, 0, 0, 3, 19, 30, 21, 7, 1]
dp[9] : [0, 0, 0, 1, 16, 45, 50, 28, 8, 1]
dp[10]: [0, 0, 0, 0, 10, 51, 90, 77, 36, 9, 1]
'''


if __name__ == '__main__':
    # print('\n'.join(map(str, solve(*get_input()))))
    print('\n'.join(map(str, solve2(*get_input()))))


'''
예제 입력 1
3
4 2
7 5
10 6
예제 출력 1
3
15
90
예제 입력 2
4
4 1
4 2
4 3
4 4
예제 출력 2
0
3
3
1

----
run=(python3 a15992.py)

echo '3\n4 2\n7 5\n10 6' | $run
# 3 15 90

echo '4\n4 1\n4 2\n4 3\n4 4' | $run
# 0 3 3 1

---

echo '4\n10 10\n10 7\n10 4\n10 3' | $run
# 1 77 10 0


'''
