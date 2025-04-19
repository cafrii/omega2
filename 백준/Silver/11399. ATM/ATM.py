
N = int(input().strip())
P = list(map(int, input().strip().split()))
# assert len(P) == N
P.sort()
# P: 0 ~ N-1
psum = [0] * (N+1)
for k in range(1, N+1): # 1 ~ N
    psum[k] = psum[k-1] + P[k-1]
print(sum(psum))
