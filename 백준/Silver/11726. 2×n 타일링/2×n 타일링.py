
MOD = 10_007

def solve2(N:int):
    # 첫 구현과 다르게, 아예 H case, V case 를 합쳐서 기록하자.
    # 또한, 매 기록 마다 mod 연산 적용.
    A = [ 0 for _ in range(N+1) ]

    A[1] = 1  # V
    if N == 1:
        return 1

    A[2] = 2  # HH, VV

    for k in range(3, N+1):
        A[k] = (A[k-2] + A[k-1]) % MOD

    return A[N]


N = int(input().strip()) # N:1~1000
print(solve2(N))
