
import sys
input = sys.stdin.readline

def solve(A)->int:
    N = len(A)

    hist = [0]*10
    # hist[i]: 주어진 구간에서 숫자 i의 과일 개수
    # hist[0]은 사용되지 않음.

    maxdist = 0

    # 포인터 j, k 운용. (j, k] 사이의 구간을 계산
    j = -1
    for k in range(N):
        hist[A[k]] += 1

        # hist 에서 개수가 0 이상인 숫자들의 개수.
        while len([ h for h in hist if h>0 ]) > 2:
            j += 1  # proceed j
            hist[A[j]] -= 1

        dist = k-j
        maxdist = max(maxdist, dist)

    return maxdist


N = int(input().strip())
A = list(map(int, input().split()))

print(solve(A))
