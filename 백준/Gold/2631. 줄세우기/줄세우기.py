import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        A.append(int(input().rstrip()))
    return N,A

def solve(N:int, A:list[int])->int:
    '''
    Args:
        A: list of child number (not ordered)
    Returns:
        min number of child-moves to order
    Logic:
        get LIS (longest increasing sub-sequence)
        and return remaining numbers
    '''

    dp = [0] * (N)
    # dp[k]: k 번째 요소를 끝으로 하는 LIS 길이

    for k in range(N):
        if k == 0:
            dp[0] = 1
            continue
        lis = 1  # 최소 LIS 길이: A[k] 단독으로만 구성되는 경우
        for j in range(k):  # j: 0 ~ k-1
            if A[j] < A[k]:
                # A[k] 는 기존 LIS 에 덧붙일 수 있음.
                lis = max(lis, dp[j] + 1)  # 새 LIS 길이
        dp[k] = lis

    lis = max(dp)
    return N - lis

if __name__ == '__main__':
    print(solve(*get_input()))
