
N_MIN = -1000

def solve(nums):
    # 두 개의 값을 계산하면서 윈도우를 증가.
    # v1: 윈도우 우측 끝에 붙은 부분수열의 최대 값.
    # v2: 부분수열의 최대 값.
    v1, v2 = N_MIN-1, N_MIN-1

    for n in nums:
        v1 = max(v1 + n, n)
        v2 = max(v2, v1)

    return max(v1, v2)


N = int(input().strip())
A = map(int, input().strip().split())

print(solve(A))
