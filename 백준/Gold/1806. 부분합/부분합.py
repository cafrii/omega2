
def solve6(N, S, A):
    # two pointer algorithm
    # refer https://butter-shower.tistory.com/226

    li = ri = 0 # left and right index
    sum = A[0]  # partial sum from A[li] to A[ri] inclusive
    min_len = N+1

    while ri < N:
        if sum < S:
            if ri == N-1:
                break
            ri += 1
            sum += A[ri]
        else: # if sum >= S:
            min_len = min(min_len, ri - li + 1)
            sum -= A[li]
            li += 1

    return min_len if min_len != N+1 else 0


N,S = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

print(solve6(N, S, A))
