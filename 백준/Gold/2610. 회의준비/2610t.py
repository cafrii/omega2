'''
test-runner

'''

import subprocess,sys,os
from random import seed,randint,shuffle

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def test_compare(inp:str):
    kwargs={'stdin':subprocess.PIPE,
        'stdout':subprocess.PIPE,
        'text':True}
    p1 = subprocess.Popen(args=["time", "python3", "2610a.py"], **kwargs)
    out1,out1e = p1.communicate(inp)
    p2 = subprocess.Popen(args=["time", "python3", "2610b.py"], **kwargs)
    out2,out2e = p2.communicate(inp)
    if out1.rstrip() != out2.rstrip():
        print(f'assert failed!')
        print(f'inp: =={inp}==')
        print(f'out1: **{out1.rstrip()}**, ##{out1e.rstrip() if out1e else ''}##')
        print(f'out2: **{out2.rstrip()}**, ##{out2e.rstrip() if out2e else ''}##')
        assert False, "answer mismatch"
    log("==== ok, same!")
    # print(out1.rstrip())




def generate_tc():
    N,M = 5,8
    # N,M = 5,7
    orders = list(range(1,N+1)) # 1~N
    shuffle(orders)
    edges = [ (orders[k-1],orders[k]) for k in range(1,len(orders)) ]
    while len(edges) < M:
        i,j = randint(1,N),randint(1,N)
        if i == j: continue
        edges.append((i,j))
    shuffle(edges)

    lines = []
    lines.append(f'{N}\n{M}\n')
    for i,j in edges:
        lines.append(f'{i} {j}\n')
    return lines


# seed(time.time())
seed(1000)

T = int(os.getenv("_T", "1"))
for i in range(T):
    log(f'**** {i}/{T}')

    lines = generate_tc()
    inpstr = ''.join(lines)
    test_compare(inpstr)

log('done')
