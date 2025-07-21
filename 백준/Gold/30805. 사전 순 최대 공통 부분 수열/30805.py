'''

30805번
사전 순 최대 공통 부분 수열 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	6907	2171	1812	31.540%

문제
어떤 수열이 다른 수열의 부분 수열이라는 것은 다음을 의미합니다.
...



------

처음에 dp 로 구현은 했는데, tc 검증 단계에서 실패!
잘 생각해 보니 구현 알고리즘에 문제가 있어서 정답을 내지 못하는 경우가 발견됨.

이 코드는 30805b.py 로 유지 관리함.


'''



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

