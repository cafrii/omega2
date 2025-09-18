import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N,

def solve2(N:int)->int:
    '''
    내려 보기 방식. 현재 dp 를 구하기 위해 과거 dp 값을 참고.
    '''
    max_n = 100
    # dp[k]: cost k에서의 A 표시 최대 출력 수

    dp = [ k for k in range(max_n+1) ]
    # A 키만 사용하는 경우: cost k, value k

    for k in range(1, N+1): # k: 1 ~ 100
        # dp[k]:
        #  dp[k-3]*2, dp[k-4]*3, dp[k-5]*4, .. dp[1]*? 들 중에서 최대 값 선택.
        if k <= 3: continue
        dp[k] = max(dp[k],
                    max( dp[j]*(k-j-1) for j in range(k-3,0,-1) )
                )
    return dp[N]


if __name__ == '__main__':
    print(solve2(*get_input()))

