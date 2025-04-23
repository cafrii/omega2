import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = [0] * M

def populate(len_a:int):
    if len_a == M:
        print(*A)
        return
    for k in range(1,N+1):
        A[len_a] = k
        populate(len_a + 1)

populate(0)
