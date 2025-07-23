
import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().strip())
    # N: 2 ~ 100_000
    A = list(map(int, input().split()))
    assert len(A) == N, "wrong length"
    return A

MAX_SUM = 1_000_000_000*2 + 1

def solve_twopointer(A:list[int])->tuple[int,int]:
    '''
    '''
    N = len(A)
    min_sum = MAX_SUM
    min_sum_pair:tuple[int,int] = (0,0)

    s,e = 0,N-1 # two index
    while s < e:
        sum1 = A[s]+A[e]
        if sum1 == 0:
            return (A[s],A[e])
        sum2 = abs(sum1)
        if sum2 < min_sum:
            min_sum,min_sum_pair = sum2,(A[s],A[e])
        if sum1 < 0:
            s += 1
        else:
            e -= 1
    return min_sum_pair


if __name__ == '__main__':
    inp = get_input()
    print(*solve_twopointer(inp))
