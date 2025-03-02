
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)

count = 0
for a in A:
    count += K // a
    K %= a

print(count)