
import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    #assert len(A) == N, f"wrong size {len(A)}, {N}"
    return A

MAX_VAL = 1_000_000

def solve_fast(A:list[int])->list[int]:
    '''
    implement without mod(%) operation
    '''
    N = len(A)
    indices = [-1]*(MAX_VAL+1)
    for i,a in enumerate(A):
        indices[a] = i
    # A.sort()
    # mn,mx = A[0],A[-1]
    mx = max(A)

    scores = [0]*(MAX_VAL+1)
    for a in A:
        if a+a > mx:
            continue
        for b in range(a+a,mx+1,a):
            if indices[b] >= 0: # only if b is in A
                scores[b] -= 1
                scores[a] += 1

    # re-arrange scores
    result = [0]*N
    for a in A:
        result[indices[a]] = scores[a]
    return result


if __name__ == '__main__':
    inp = get_input()
    res = solve_fast(inp)
    print(' '.join(map(str, res)))
