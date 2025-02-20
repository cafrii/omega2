# 두 집합의 intersection을 구하는 문제
N, M = map(int, input().split())
A = set(input() for _ in range(N))
B = set(input() for _ in range(M))
C = A & B # C = A.intersection(B)
print(len(C))
for name in sorted(C): # sorted() returns a list
    print(name)
