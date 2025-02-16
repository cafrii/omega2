N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# A = sorted(A) # it is not necessary

DA = {} # used as sparse array

for i in range(N):
    if A[i] in DA:
        DA[A[i]] += 1
    else:
        DA[A[i]] = 1

for i in range(M):
    if B[i] in DA:
        B[i] = DA[B[i]]
    else:
        B[i] = 0

print(' '.join(map(str, B)))
