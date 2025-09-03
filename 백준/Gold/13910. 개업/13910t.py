
'''
test-runner

'''

import time
import subprocess,sys,os
from random import seed,randint,shuffle

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def test_compare(inp:str):
    kwargs={'stdin':subprocess.PIPE,
        'stdout':subprocess.PIPE,
        'text':True}
    p1 = subprocess.Popen(args=["time", "python3", "13910.py"], **kwargs) # 제출본
    out1,out1e = p1.communicate(inp)
    p2 = subprocess.Popen(args=["time", "python3", "13910_bfs.py"], **kwargs)
    out2,out2e = p2.communicate(inp)
    if out1.rstrip() != out2.rstrip():
        print(f'assert failed!')
        print(f'inp: =={inp}==')
        print(f'out1: **{out1.rstrip()}**, ##{out1e.rstrip() if out1e else ''}##')
        print(f'out2: **{out2.rstrip()}**, ##{out2e.rstrip() if out2e else ''}##')
        assert False, "answer mismatch"
    log("==== ok, same! %s", out1)
    # print(out1.rstrip())




def generate_tc():
    # N,M = 5,7
    # N,M,wmax = 10_000,100,10_000
    # N,M,wmax = 10_000,10,10
    # N,M,wmax = 10_000,100,2

    # N,M,w = 10_000,100,(11,19)  # range
    N,M,w = 10_000,100,[3]       # specific list

    # W = [ randint(1,wmax) for m in range(M) ]
    W = [ randint(*w) if isinstance(w, tuple) else w[randint(0,len(w)-1)] for m in range(M) ]

    log("%d %d, %s", N, M, W)

    lines = []
    lines.append(f'{N} {M}\n')
    lines.append(' '.join(map(str, W)) + '\n')

    return lines



seed(time.time())
# seed(43)

T = int(os.getenv("_T", "1"))
for i in range(T):
    log(f'**** {i}/{T}')

    lines = generate_tc()
    inpstr = ''.join(lines)
    test_compare(inpstr)

log('done')



