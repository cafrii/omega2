import sys

MOD = 1_000_000_009

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    A = []
    for _ in range(C):
        n,m = map(int, input().split())
        A.append((n,m))
    return A,

def solve2(A:list[tuple[int,int]])->list[int]:
    '''
    좀 더 개선된 버전.
    j 루프 중간에 더 이상 계산할 의미가 없는 조건이 되면 loop-out
    '''
    max_n = max(A, key=lambda x:x[0])[0]

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

    ans = [ dp[n][m] for n,m in A ]
    return ans

if __name__ == '__main__':
    print('\n'.join(map(str, solve2(*get_input()))))
