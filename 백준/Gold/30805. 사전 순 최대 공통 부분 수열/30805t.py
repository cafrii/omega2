'''

30805 (정답) 과 30805b (오답) 을 구분해 내는 문제를 만들어내기 위한 코드.

둘의 출력이 다를 때 까지 반복.

환경 변수 _T 에 반복 횟수 설정 가능.

예:
export _T=100

python3 30805t.py
...


'''

import subprocess,sys,os
from random import seed,randint


def test(inp:str):
    kwargs={'stdin':subprocess.PIPE,
        'stdout':subprocess.PIPE,
        'text':True}
    p1 = subprocess.Popen(args=["python3", "30805b.py"], **kwargs)
    out1,out1e = p1.communicate(inp)
    p2 = subprocess.Popen(args=["python3", "30805.py"], **kwargs)
    out2,out2e = p2.communicate(inp)
    if out1.rstrip() != out2.rstrip():
        print(f'assert failed!')
        print(f'inp: =={inp}==')
        print(f'out1: **{out1.rstrip()}**, ##{out1e.rstrip() if out1e else ''}##')
        print(f'out2: **{out2.rstrip()}**, ##{out2e.rstrip() if out2e else ''}##')
        assert False, "answer mismatch"
    print(f'ok, {out1.rstrip()}')

T = int(os.getenv("_T", "1"))

for i in range(T):
    print(f'**** {i}/{T}')
    N,M = 10,10 #randint(1,100),randint(1,100)
    tc = []
    tc.append(f'{N}\n')
    tc.append(' '.join([ str(randint(1, 10)) for k in range(N) ]) + '\n')
    tc.append(f'{M}\n')
    tc.append(' '.join([ str(randint(1, 10)) for k in range(M) ]) + '\n')
    inpstr = ''.join(tc)
    test(inpstr)

print('done')

