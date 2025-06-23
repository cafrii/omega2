def factorial(n):
    if n <= 1: return 1
    return n*factorial(n-1)

def solve(N, K):
    assert K <= N
    return factorial(N) // (factorial(N-K) * factorial(K))

N,K = map(int, input().split())
print(solve(N, K))
