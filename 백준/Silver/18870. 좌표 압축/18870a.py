
# more simple answer

import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = sorted(list(set(A)))

D = {val: i for i, val in enumerate(B)}
E = [str(D[i]) for i in A]

print(' '.join(E))

