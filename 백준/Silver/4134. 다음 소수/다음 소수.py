
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

input = __import__('sys').stdin.readline
N = int(input().rstrip())

for _ in range(N):
    n = int(input())
    while not is_prime(n):
        n += 1
    print(n)
