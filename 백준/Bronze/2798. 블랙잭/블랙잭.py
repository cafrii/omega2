
N, M = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
result = 0

for i in range(N):
    if A[i] > M:
        break
    for j in range(i+1, N):
        if A[i] + A[j] > M:
            break
        for k in range(j+1, N):
            if A[i] + A[j] + A[k] <= M:
                result = max(result, A[i] + A[j] + A[k])
            else:
                break

print(result)
