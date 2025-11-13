import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        s,e = map(int, input().split())
        A.append((s, e))
    _ = int(input().rstrip())
    Q = list(map(int, input().split()))
    return N,A,Q

def solve(N:int, A:list[tuple[int,int]], Q:list[int])->list[str]:
    '''
    Args:
    Returns:
    '''
    MAX_T = 1_000_000
    # differential sum
    D = [0] * (MAX_T + 2)
    max_t = 0

    # s, e 는 zero-based 이다.
    # s는 공부를 시작한 시각, e는 공부를 끝낸 시각+1
    for s,e in A:
        D[s] += 1
        D[e+1] -= 1
        if max_t < e: max_t = e

    for k in range(1, max_t+2): # k: 1 ~ max_t+1
        D[k] = D[k-1] + D[k]
    #assert D[max_t+1] == 0

    return [ str(D[q]) for q in Q ]

if __name__ == '__main__':
    print('\n'.join(solve(*get_input())))
