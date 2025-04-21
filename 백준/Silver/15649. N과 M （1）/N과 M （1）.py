
import sys
def log(fmt, *arg):
    print(fmt % arg, file=sys.stderr)

# greedy
def solve_greedy_recursive(N, M):
    # construct length M array [1, 2, 3, .., M]
    A = [i for i in range(1, M+1)]

    def incr(L) -> bool:
        # 길이 L 의 숫자 배열 A (즉, A[0:L]) 를 하나 증가.
        # 더 이상 증가를 못하면 False 리턴
        if L <= 0:
            return False
        if A[0] > N:
            return False

        # 맨 끝 자리 하나 증가
        A[L-1] = A[L-1] + 1
        # 허용 가능 수: 1~N
        if A[L-1] > N: # 마지막 자리가 넘침. carry 처리.
            if not incr(L-1):
                return False
            A[L-1] = 1
            # 1 또한 중복 체크 해야 하니 계속 진행

        if A[L-1] in A[:L-1]: # 중복 체크
            return incr(L)
        else:
            return True # ok

    while True:
        print(*A)
        if incr(M) == False:
            break

N,M = map(int, input().split())
solve_greedy_recursive(N, M)
