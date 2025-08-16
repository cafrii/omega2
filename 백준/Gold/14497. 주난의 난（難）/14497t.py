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
    p1 = subprocess.Popen(args=["time", "python3", "14497.py"], **kwargs) # 제출본
    out1,out1e = p1.communicate(inp)
    p2 = subprocess.Popen(args=["time", "python3", "14497a.py"], **kwargs) # 속도 개선
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
    # N,M = 5,7
    N,M = 300,300
    grid = [ ['0']*M for _ in range(N) ]
    num_ones = int(N * M * 0.7)
    log(" %d x %d, %d ones", N, M, num_ones)

    k = 0
    while k < num_ones:
        y,x = randint(0,N-1),randint(0,M-1)
        if grid[y][x] == '1': continue
        grid[y][x] = '1'
        k += 1

    sh = (randint(0,N-1),randint(0,M-1))
    st = (randint(0,N-1),randint(0,M-1))
    while st == sh:
        st = (randint(0,N-1),randint(0,M-1))

    grid[sh[0]][sh[1]] = '#'
    grid[st[0]][st[1]] = '*'

    lines = []
    lines.append(f'{N} {M}\n')
    lines.append(f'{st[0]+1} {st[1]+1} {sh[0]+1} {sh[1]+1}\n')
    for y in range(N):
        lines.append(''.join(grid[y]) + '\n')

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

