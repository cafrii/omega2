import sys
import itertools

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    return N,K,A

def solve(N:int, K:int, A:list[int])->int:
    '''
    Args:
    Returns:
    '''
    # moving sum
    msum = sum(itertools.islice(A, 0, K))
    # max sum
    maxsum = msum

    for j in range(N-K): # j: 0 ~ N-K-1
        msum = msum - A[j] + A[j+K]
        maxsum = max(maxsum, msum)
    return maxsum

if __name__ == '__main__':
    print(solve(*get_input()))

