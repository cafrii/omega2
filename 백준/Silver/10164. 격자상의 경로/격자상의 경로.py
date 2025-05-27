
def factorial(n):
    return n*factorial(n-1) if n>1 else 1

def solve(N, M):
    n,m = N-1,M-1
    # 우측으로 n 회, 아래로 m 회의 조합의 수
    # (n+m)! / n! / m!
    return factorial(n+m)//factorial(n)//factorial(m)

N,M,K = map(int, input().split())
if K == 0:
    print(solve(N, M))
else:
    r,c = (K-1)//M,(K-1)%M
    print(solve(r+1, c+1) * solve(N-r, M-c))
