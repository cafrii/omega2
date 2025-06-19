'''

훨씬 더 간단하고 세련된 방법으로 보임.

https://www.acmicpc.net/source/95301792

'''


N, B = map(int, input().split())
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))

mul = lambda m1, m2: [[sum([m1[i][k]*m2[k][j] for k in range(N)])%1000 for j in range(N)] for i in range(N)]

I = [[int(i==j) for j in range(N)] for i in range(N)]

def m_pow(b):
    if b == 1: return mul(m, I)

    x = m_pow(b//2)
    if b%2: return mul(mul(x, x), m)
    else: return mul(x, x)

res = m_pow(B)
for r in res:
    print(" ".join(map(str, r)))


