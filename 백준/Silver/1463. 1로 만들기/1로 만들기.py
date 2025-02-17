

def solve(N):
    A = [ N ] * (N + 1)
    A[0] = 0 # not used
    A[1] = 0 # already reached to 1

    # construction approach
    for i in range(1, N+1):
        if i * 3 <= N:
            A[i*3] = min(A[i*3], A[i]+1)
        if i * 2 <= N:
            A[i*2] = min(A[i*2], A[i]+1)
        if i + 1 <= N:
            A[i+1] = min(A[i]+1, A[i+1])
    return A

N = int(input())

A = solve(N)

print(A[N])

