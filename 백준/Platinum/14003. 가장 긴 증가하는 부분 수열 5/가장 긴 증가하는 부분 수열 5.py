
import sys
input = sys.stdin.readline
write = sys.stdout.write

import bisect


MIN_A = -1_000_000_000
MIN = MIN_A - 1


def solve(A:list[int])->tuple[int,list]:
    '''
    '''
    N = len(A)

    D = [MIN] * N
    # D[i]: A[:i+1] 까지만 고려했을때, 끝자리 숫자가 A[i]인 LIS의 길이

    # L[k]: 길이가 k인 LIS의 맨 끝자리 숫자 중 최소값.
    L = [MIN] * (N+1)
    lsz = 1   # L의 실제로 유효한 요소의 개수

    # 첫번째 A[0]은 따로 고려해 준다.
    D[0] = 1

    L[lsz] = A[0]
    lsz += 1

    # 두번째 숫자부터는 루프.
    for i in range(1, N):
        #
        # L[:] 중에서 A[i]보다 작은 최대요소를 찾고, 그 LIS길이에 +1을 하면 됨.
        idx = bisect.bisect_left(L, A[i], lo=0, hi=lsz)

        # 발견한 자리의 인덱스 idx가 새 LIS 길이. (즉, +1까지 고려된 길이)
        D[i] = idx

        # L 업데이트.
        L[idx] = A[i] # 길이가 idx인 lis의 끝자리 숫자.
        # 기존에 L2[idx]에 있던 숫자는 A[i]보다 크거나 같음이 보장됨.
        # 즉, A[i]는 현재까지 L2[idx]에 올 수 있는 최소값.

        lsz = max(lsz, idx+1)
        # L2 의 실제로 데이터가 저장된 길이 추적

    # max(D)를 호출하는 것 보다 lsz 계산이 더 빠르다.
    # 현재 L 에는 L[0] 부터 L[lsz-1] 까지 lsz 개의 요소가 있음.
    # L의 인덱스가 LIS 길이 이므로, 최대 LIS 길이는 lsz-1 이다.
    max_d = lsz-1

    # create sample sequence of A[]
    B = [0] * max_d
    d = max_d
    for i in range(len(D)-1, -1, -1):
        if D[i] != d: continue
        B[d-1] = A[i]
        d -= 1
        if d == 0: break # early exit

    return max_d, B


N = int(input().strip())
A = list(map(int, input().split()))
assert len(A) == N
max_d,seq = solve(A)

write(f'{max_d}\n')
write(' '.join(map(str, seq)))
write('\n')
