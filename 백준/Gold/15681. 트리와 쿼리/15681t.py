
import subprocess,sys,os
from random import seed,randint,shuffle

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def test_compare(inp:str):
    kwargs={'stdin':subprocess.PIPE,
        'stdout':subprocess.PIPE,
        'text':True}
    p1 = subprocess.Popen(args=["time", "python3", "15681.py", "recursive"], **kwargs)
    out1,out1e = p1.communicate(inp)
    p2 = subprocess.Popen(args=["time", "python3", "15681.py"], **kwargs)
    out2,out2e = p2.communicate(inp)
    if out1.rstrip() != out2.rstrip():
        print(f'assert failed!')
        print(f'inp: =={inp}==')
        print(f'out1: **{out1.rstrip()}**, ##{out1e.rstrip() if out1e else ''}##')
        print(f'out2: **{out2.rstrip()}**, ##{out2e.rstrip() if out2e else ''}##')
        assert False, "answer mismatch"
    log("==== ok, same!")
    # print(out1.rstrip())


def test(inp:str):
    kwargs={'stdin':subprocess.PIPE,
        'stdout':subprocess.PIPE,
        'text':True,
        # 'shell':True,
        }
    # p1 = subprocess.Popen(args=["python3", "15681.py", "2>&1" ], **kwargs)
    p1 = subprocess.Popen(args=["time", "python3", "15681.py"], **kwargs)
    out1,out1e = p1.communicate(inp)
    log("==== ok")
    print(out1.rstrip())



T = int(os.getenv("_T", "1"))

for i in range(T):
    log(f'**** {i}/{T}')

    N,Q = int(1e5),int(1e5)
    # N,Q = 100,100
    # N = 9
    # Q = randint(1,N)

    R = randint(1,N)

    tc = []
    tc.append(f'{N} {R} {Q}\n')

    in_tree = []
    orders = list(range(1,N+1))
    shuffle(orders)
    for n in orders:
        if in_tree:
            par = in_tree[randint(0,len(in_tree)-1)]
            tc.append(f'{par} {n}\n')
        in_tree.append(n)

    for _ in range(Q):
        tc.append(f'{randint(1,N)}\n')

    # tc is ready
    inpstr = ''.join(tc)
    # print(inpstr, end='', file=sys.stderr)

    # test(inpstr)
    test_compare(inpstr)

log('done')

