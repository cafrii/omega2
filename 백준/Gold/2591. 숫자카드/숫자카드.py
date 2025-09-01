
import sys

def get_input():
    input = sys.stdin.readline
    A = input().rstrip()
    return A,  # return as tuple[str]

def solve(A:str):
    '''
    Args:
        A: list of digits, max len(A) 40
    Returns:
        number of possible method that compose the digits using card 1~34
    '''
    N = len(A) # number of digits
    dp = [0] * (N+1)
    dp[0] = 1
    for k in range(1, N+1):
        # dp[k] 는 첫 k개의 숫자 (A[:k], 즉 A[0]~A[k-1]) 를 생성하는 조합 경우의 수
        # 1. A[:k-1] 로 만든 경우의 수에 A[k-1]을 추가 고려하는 경우
        # 2. A[:k-2] 로 만든 경우의 수에 A[k-2],A[k-1] 을 추가 고려하는 경우
        n1 = int(A[k-1]) if k >= 1 else 0
        n2 = int(A[k-2:k]) if k >= 2 else 0
        if 1 <= n1 <= 9:
            dp[k] += dp[k-1]
        if 10 <= n2 <= 34:
            dp[k] += dp[k-2]
    return dp[N]

if __name__ == '__main__':
    print(solve(*get_input()))

