'''

2146c.py 의 제출 답안이 fail 되어서
fail 되는 문제를 랜덤으로 찾기 위한 스크립트.


'''

import subprocess,sys,os,time
from random import seed,randint,shuffle

seed(time.time())
# seed(43)

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def test_compare(inp:str):
    kwargs={'stdin':subprocess.PIPE,
        'stdout':subprocess.PIPE,
        'text':True}
    p1 = subprocess.Popen(args=["time", "python3", "2146.py"], **kwargs)
    out1,out1e = p1.communicate(inp)
    p2 = subprocess.Popen(args=["time", "python3", "2146c.py"], **kwargs)
    out2,out2e = p2.communicate(inp)
    if out1.rstrip() != out2.rstrip():
        print(f'assert failed!')
        print(f'inp: =={inp}==')
        print(f'out1: **{out1.rstrip()}**, ##{out1e.rstrip() if out1e else ''}##')
        print(f'out2: **{out2.rstrip()}**, ##{out2e.rstrip() if out2e else ''}##')
        assert False, "answer mismatch"
    log("==== ok, same!")
    # print(out1.rstrip())


T = int(os.getenv("_T", "1000"))

for i in range(T):
    log(f'**** {i}/{T}')
    tc = []
    N = randint(2, 100)
    A = [ [0]*N for _ in range(N) ]
    num_cell = randint(1, N*N)
    for k in range(num_cell):
        A[randint(0,N-1)][randint(0,N-1)] = 1

    tc.append(f"{N}\n")
    for a in A:
        tc.append(' '.join(map(str, a)) + '\n')

    inpstr = ''.join(tc)
    log("********%s*********", inpstr)
    test_compare(inpstr)

log('done')
