import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    #assert len(A) == N
    return N,A

def solve(N:int, A:list[int])->int:
    '''
    Args:
        N: length of array A
        A: list of numbers of length N.
            last number is what we should make by composing numbers.
    Returns:
        number of valid expressions possible
    Logic:
        A[0] 부터 A[N-1] 까지의 총 N개의 배열이 주어지는데
        사실 A[N-2] 까지가 조합(수식)에 사용할 수 있는 숫자들이고
        마지막 A[N-1]은 만들어야 하는 타겟 목표이다.
        따라서 dp는 입력 A에 맞게 0부터 N-2 까지만 돌리고,
        dp[N-2][] 중에서 목표 A[N-1]에 해당하는 것을 택하면 정답이 된다.
    '''
    dp = [ [0]*21 for _ in range(N) ]
    dp[0][A[0]] = 1

    for k in range(1, N-1): # k: 1 ~ N-2
        # dp[k][j] 를 만드는 방법은 dp[k-1][i]에 A[k]를 + 또는 - 연산을 수행.
        for i in range(0, 21): # i: 0~20
            if dp[k-1][i] == 0: continue
            if i+A[k] <= 20:
                dp[k][i+A[k]] += dp[k-1][i]
            if i-A[k] >= 0:
                dp[k][i-A[k]] += dp[k-1][i]

    return dp[N-2][A[N-1]]

if __name__ == '__main__':
    print(solve(*get_input()))
