
import sys

def read_quiz():
    input = sys.stdin.readline
    N = int(input().strip())
    A = list(map(int, input().split()))
    assert len(A) == N, "wrong number of A elem."
    M = int(input().strip())
    B = list(map(int, input().split()))
    assert len(B) == M, "wrong number of B elem."
    return A,B


def index2(iterable, x, defval=-1):
    for i, item in enumerate(iterable):
        if item == x:
            return i
    return defval

def get_lgcs2(A:list[int], B:list[int])->list[int]:
    '''
    using recursive
    '''
    if not (A and B): # both should not be empty
        return []
    if len(A) == len(B) == 1:
        return [A[0]] if A[0]==B[0] else []
    for n in range(100,-1,-1):
        ia = index2(A, n)
        if ia < 0: continue
        ib = index2(B, n)
        if ib < 0: continue
        return [n] + get_lgcs2(A[ia+1:], B[ib+1:])
    return [] # no lgcs


def solve_recursive(A:list[int], B:list[int])->list[int]:
    return get_lgcs2(A, B)


if __name__ == '__main__':
    A,B = read_quiz()
    K = solve_recursive(A,B)
    print(len(K))
    if K:
        print(' '.join(str(k) for k in K))

