
import sys

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input().rstrip()))
    return A,K


def solve_dp(A:list[int], K:int)->int:
    '''
    Args:
        A[]: list of unit price of each coin
        K: target value which we will compose using coins.
    Returns:
        the number of cases we can compose K using any number of provided coins.
    Algo:
        using 1-dimensional dp.
    '''
    N = len(A)

    dp = [0] * (K+1)
    # dp[k]는 목표 k를 만들어내는 경우의 수.

    dp[0] = 1  # 아무 동전도 사용하지 않는 경우 1가지.

    # dp 는 전체 dp array가 여러 단계에 걸쳐 점진적으로 누적 업데이트 된다.
    for i in range(N):
        c = A[i]
        for k in range(c, K+1): # 증가하는 방향으로만 가능.
            dp[k] += dp[k-c]
            
    return dp[K]


if __name__ == '__main__':
    inp = get_input()
    r = solve_dp(*inp)
    print(r)

