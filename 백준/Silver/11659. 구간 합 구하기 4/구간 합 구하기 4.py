import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))

# calculate partial sum
sums = [0] * (N+1)
# sums[k]: == sum(A[:k]), 앞의 k개 요소의 부분합. 즉, A[0] 부터 A[k-1] 까지의 합
for k in range(1, N+1):
    sums[k] = sums[k-1] + A[k-1]

for _ in range(M):
    i,j = map(int, input().split())
    # i번째 수 부터 j번째 수 까지의 합 == j번째 수 까지의 부분합 - (i-1)번째 수 까지의 부분합
    print(sums[j] - sums[i-1])
