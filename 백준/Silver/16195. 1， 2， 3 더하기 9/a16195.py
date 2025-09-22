'''
16195번
1, 2, 3 더하기 9, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	2456	1188	952	48.276%

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
단, 사용한 수의 개수는 m개 이하 이어야 한다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n과 m이 주어진다.
n은 양수이며 1,000보다 작거나 같다. m도 양수이며, n보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.
단, 사용한 수의 개수는 m개 이하 이어야 한다.

----------

5:39~

1차 틀림.
2차 통과. 검증 완료.


'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

MOD = 1_000_000_009

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    A = []
    for _ in range(C):
        n,m = map(int, input().split())
        A.append((n, m))
    return A,

def solve(A:list[tuple[int,int]])->list[int]:
    '''
    Args:    A: [ (n,m), .. ]
    Returns: list of answers
    '''
    max_n = max(A, key=lambda x:x[0])[0]
    alloc_n = max(4, max_n)

    dp = [ [0]*(alloc_n+1) for k in range(alloc_n+1) ]
    # dp[k]: k 를 1,2,3 합으로 나타내는 방법 중 m개만 사용하는 경우의 수

    dp[1][1] = 1
    dp[2][1:3] = [1,1]
    dp[3][1:4] = [1,2,1]

    for k in range(4, max_n+1):

        for m in range(k, 0, -1): # m: k ~ 1
            dp[k][m] = (dp[k-1][m-1] + dp[k-2][m-1] + dp[k-3][m-1]) % MOD

            if dp[k][m] == 0: # early exit
                break
        # log("[%d]: %s", k, dp[k][:k+1])

    # ans = []
    # for n,m in A:
    #     ans.append( sum( dp[n][:m+1] ) % MOD )

    ans = [ (sum(dp[n][:m+1]) % MOD) for n,m in A ]
    return ans

if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))


'''
예제 입력 1
3
4 2
7 5
10 6
예제 출력 1
3
37
151

예제 입력 2
4
4 1
4 2
4 3
4 4
예제 출력 2
0
3
6
7

예제 입력 3
7
7 1
7 2
7 3
7 4
7 5
7 6
7 7
예제 출력 3
0
0
6
22
37
43
44

예제 입력 4
10
10 1
10 2
10 3
10 4
10 5
10 6
10 7
10 8
10 9
10 10
예제 출력 4
0
0
0
10
61
151
228
264
273
274

-----
run=(python3 a16195.py)

echo '3\n4 2\n7 5\n10 6' | $run
# 3 37 151

echo '4\n4 1\n4 2\n4 3\n4 4' | $run
# 0 3 6 7

echo '7\n7 1\n7 2\n7 3\n7 4\n7 5\n7 6\n7 7' | $run
# 0 0 6 22 37 43 44

echo '10\n10 1\n10 2\n10 3\n10 4\n10 5\n10 6\n10 7\n10 8\n10 9\n10 10' | $run
# 0 0 0 10 61 151 228 264 273 274

----
echo '4\n1 1\n2 1\n3 1\n4 1' | $run
# 1 1 1 0


'''


