'''

'''



import subprocess,sys,os
from random import seed,randint,shuffle
import time, os

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def test_compare(inp:str):
    kwargs={'stdin':subprocess.PIPE,
        'stdout':subprocess.PIPE,
        'text':True}
    # p1 = subprocess.Popen(args=["time", "python3", "1939.py"], **kwargs) # dijkstra
    p1 = subprocess.Popen(args=["time", "python3", "1939_dsu2.py"], **kwargs) # dsu improved
    out1,out1e = p1.communicate(inp)
    p2 = subprocess.Popen(args=["time", "python3", "1939_dsu.py"], **kwargs)
    out2,out2e = p2.communicate(inp)
    if out1.rstrip() != out2.rstrip():
        print(f'assert failed! answer mismatch!')
        print(f'inp: =={inp}==')
        print(f'out1: **{out1.rstrip()}**, ##{out1e.rstrip() if out1e else ''}##')
        print(f'out2: **{out2.rstrip()}**, ##{out2e.rstrip() if out2e else ''}##')
        assert False, "answer mismatch"
    log("==== ok, same!")
    # print(out1.rstrip())



def generate_tc():
    '''
    '''
    # seed(time.time())
    # seed(43)

    MAX_N,MAX_M = 10_000,100_000
    N,M = randint(2,MAX_N), randint(1,MAX_M)

    # env var override
    N = int(os.getenv('_N', str(N)))
    M = int(os.getenv('_M', str(M)))

    # N,M = 10,20
    MAX_WEIGHT = 100

    orders = list(range(1,N+1)) # [1,2,..,N]
    shuffle(orders)

    edges = []
    fac = [0,0]

    for k in range(1, N): # index: 1 ~ N-1
        w = randint(1, MAX_WEIGHT)
        edges.append((orders[k-1], orders[k], w))

    if len(edges) > M:
        del edges[M:]
        fac = edges[M-1][0],edges[0][1]
    else:
        while len(edges) < M:
            a,b,w = randint(1,N),randint(1,N),randint(1,MAX_WEIGHT)
            if a == b: continue
            edges.append((a,b,w))
        shuffle(orders)
        fac = orders[0],orders[1]

    lines = []
    lines.append(f'{N} {M}\n')
    # print(N, M)
    shuffle(orders)
    for a,b,w in edges:
        lines.append(f'{a} {b} {w}\n')
        # print(a, b, w)
    lines.append(f'{fac[0]} {fac[1]}\n')
    # print(*fac)
    return lines


#-----------

# seed(time.time())
seed(43)

T = int(os.getenv("_T", "1"))

for i in range(T):
    log(f'**** {i}/{T}')

    lines = generate_tc()
    inpstr = ''.join(lines)
    test_compare(inpstr)

log('done')
