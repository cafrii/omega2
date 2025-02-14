
MAX_N = 1_000_000_000

N = int(input().strip())
m6 = 0
f_prev = 1

for L in range(1,MAX_N):
    f_next = f_prev + m6
    if N <= f_next:
        print(L)
        break
    f_prev = f_next
    m6 += 6