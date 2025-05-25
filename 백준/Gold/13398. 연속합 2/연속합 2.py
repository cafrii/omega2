
import sys
input = sys.stdin.readline

MIN_VAL = -1000
MAX_N = 100_000
MIN = MIN_VAL*MAX_N-1

N = int(input().strip())
A = list(map(int, input().split()))
assert len(A) == N

def solve()->int:
    s = [ MIN, MIN, MIN, MIN ]
    for k in range(N):
        # s[0]: A[x:k+1] 의 최대 합
        # s[1]: A[y:k] 의 최대 합
        # s[2]: A[z:k+1] 중 하나를 제거하는 경우를 포함한 최대 합
        # s[3]: 최대 값 추척
        ns = [MIN]*4  # next of s
        ns[0] = max(s[0]+A[k], A[k])
        ns[1] = s[0]
        ns[2] = max(ns[0], ns[1], s[2]+A[k])
        ns[3] = max(s[3], ns[2])
        s = ns
    return s[3]

print(solve())
