def solve(N, K):
    A = list(range(1, N+1))
    result = []
    idx = 0
    K -= 1
    while A:
        idx = (idx + K) % len(A)
        result.append(A[idx])
        del A[idx]
    return result

N,K = map(int, input().split())
ans:list[int] = solve(N,K)

print('<', ', '.join(list(map(str, ans))), '>', sep='')
