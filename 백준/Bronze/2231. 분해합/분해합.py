def solve(N):
    for i in range(1, N):
        if i + sum(map(int, str(i))) == N:
            return i
    return 0

N = int(input())
print(solve(N))
