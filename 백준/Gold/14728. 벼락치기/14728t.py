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
    p1 = subprocess.Popen(args=["time", "python3", "14728.py"], **kwargs) # 제출본
    out1,out1e = p1.communicate(inp)
    p2 = subprocess.Popen(args=["time", "python3", "14728b.py"], **kwargs) # 속도 개선
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
    # N = int(os.getenv('_N','10'))
    # T = int(os.getenv('_T','100'))
    # N,T = 10,100
    N,T = 100,10000

    lines = []
    lines.append(f'{N} {T}\n')
    # print(N,T)

    for _ in range(N):
        # r,s = randint(1,max(10,T//10)), randint(1,100)
        r,s = randint(1,10000), randint(1,100)
        # print(r, s)
        # print(randint(1,100),1)
        lines.append(f'{r} {s}\n')

    return lines



seed(time.time())
# seed(43)

TC = int(os.getenv("_TC", "1"))
for i in range(TC):
    log(f'**** {i}/{TC}')

    lines = generate_tc()
    inpstr = ''.join(lines)
    test_compare(inpstr)

log('done')

