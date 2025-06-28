
import sys
input = sys.stdin.readline
import bisect

MAX_N = 1_000_000

MIN_A = -1_000_000_000
MAX_A =  1_000_000_000
NONE_A = MIN_A - 1


def solve(A:list[int])->int:
    '''
    '''
    N = len(A)

    D = [NONE_A] * N
    # D[i]: A[:i+1] 까지만 고려했을때, 끝자리 숫자가 A[i]인 LIS의 길이

    # L[k]: 길이가 k인 lis의 맨 끝자리 숫자 중 최소값.
    L = [NONE_A] * (MAX_N+1)
    sz_l = 1

    # 첫번째 A[0]은 따로 고려해 준다.
    D[0] = 1
    L[sz_l] = A[0]
    sz_l += 1

    # 두번째 숫자부터는 루프.
    for i in range(1, N):
        #
        # L[:] 중에서 A[i]보다 작은 최대요소를 찾고, 그 LIS길이에 +1을 하면 됨.
        idx = bisect.bisect_left(L, A[i], lo=0, hi=sz_l)

        # 발견한 자리의 인덱스 idx가 새 LIS 길이. (즉, +1까지 고려된 길이)
        D[i] = idx

        # L 업데이트.
        L[idx] = A[i] # 길이가 idx인 lis의 끝자리 숫자.
        # 기존에 L2[idx]에 있던 숫자는 A[i]보다 크거나 같음이 보장됨.
        # 즉, A[i]는 현재까지 L2[idx]에 올 수 있는 최소값.

        sz_l = max(sz_l, idx+1)
        # L2 의 실제로 데이터가 저장된 길이 추적

    return sz_l-1


N = int(input().strip())
A = list(map(int, input().split()))
assert len(A) == N
print(solve(A))
