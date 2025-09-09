
'''
test-runner

2025.9.5

'''

import time
import subprocess,sys,os
from random import seed,randint,shuffle

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def test_compare(inp:str):
    kwargs={'stdin':subprocess.PIPE,
        'stdout':subprocess.PIPE,
        'text':True}
    p1 = subprocess.Popen(args=["time", "python3", "2565.py"], **kwargs) # 제출본
    out1,out1e = p1.communicate(inp)
    p2 = subprocess.Popen(args=["time", "python3", "2565_wrong.py"], **kwargs)
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
    # N = 5; M = max(N, 99)
    N = 10; M = max(N, 99)

    R,S = list(range(1,M)),list(range(1,M))
    shuffle(R); shuffle(S)
    R,S = R[:N],S[:N]

    log("N %d, M %d, %s %s", N, M, R,S)

    lines = []
    lines.append(f'{N}\n')
    for a,b in zip(R,S):
        lines.append(f'{a} {b}\n')

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



