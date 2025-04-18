N = int(input().strip())
A = list(map(int, input().split()))
# assert(sum(A) == N)
T, P = map(int, input().split())

num_pack = 0
for a in A:
    num_pack += (a + T-1) // T
print(num_pack)
print( N//P, N%P)
