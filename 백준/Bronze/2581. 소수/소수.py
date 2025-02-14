# [M,N] = map(int, input().split())
M = int(input())
N = int(input())
# M <= N

is_prime = bytearray(N+1)

is_prime[0] = is_prime[1] = 0
# fill is_prime with 1
for i in range(2,N+1):
    is_prime[i] = 1

for i in range(2, N+1):
    if is_prime[i]:
        for k in range(i+i, N+1, i):
            is_prime[k] = 0

primes = [ i for i in range(M,N+1) if is_prime[i] ]

print(sum(primes) if primes else -1)

if primes:
    print(min(primes))