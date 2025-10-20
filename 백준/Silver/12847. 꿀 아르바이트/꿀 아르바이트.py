import sys, itertools

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    #assert len(A) == N
    return N,M,A

def solve(N:int, M:int, A:list[int])->int:
    '''
    Args:
    Returns:
    '''
    profit = sum(itertools.islice(A, M))
    max_profit = profit

    for k in range(M, N):
        profit = profit + A[k] - A[k-M]
        if profit > max_profit: max_profit = profit

    return max_profit

if __name__ == '__main__':
    print(solve(*get_input()))
