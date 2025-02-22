import sys
readline = sys.stdin.readline
T = int(readline().rstrip()) # 1 ~ 1,000,000
for _ in range(T):
    A,B = map(int, readline().split()) # 1 ~ 1,000
    print(A + B)
