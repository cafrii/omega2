
import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
assert N == len(A)

set1 = set(A)

dict1 = {}
acc_sum = 0 # 누적 개수 합
for k in sorted(list(set1)):
    dict1[k] = acc_sum
    acc_sum += 1

# print
for i in range(N):
    A[i] = dict1[A[i]]
print(*A)
