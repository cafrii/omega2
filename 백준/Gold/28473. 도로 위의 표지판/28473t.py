
# import subprocess,sys,os
# from random import seed,randint,shuffle
# def log(fmt, *args): print(fmt % args, file=sys.stderr)

import time
from random import seed,randint,shuffle

seed(time.time())
# seed(43)

# N,M = 200_000, 500_000 # max
N,M = 10,20

# MAX_W = int(1e6)
MAX_W = int(1e3)

edgemap = [ [] for i in range(N+1) ]
edges = []

if randint(1,100) <= 50:
    # mst 가 생성이 됨을 보장하는 케이스.
    A = list(range(1,N+1))
    shuffle(A)
    for k in range(1,N):
        x,y = A[k-1],A[k]
        z = randint(1,9)
        w = randint(0,MAX_W)
        edges.append((x,y,z,w))
        if len(edges) >= M:
            break
    # 일단 N-1 개 만 채워 놓고, 나머지는 아래에서.

while len(edges) < M:
    x = randint(1,N)
    y = randint(1,N)
    while y == x:
        y = randint(1,N)
    if y < x:
        x,y = y,x
    if y not in edgemap[x]:
        z = randint(1,9)
        w = randint(0,MAX_W)
        edges.append((x,y,z,w))

print(N,M)
for e in edges:
    print(*e)
