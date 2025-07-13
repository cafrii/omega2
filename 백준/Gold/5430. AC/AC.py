
import sys
input = sys.stdin.readline

from collections import deque


def solve(cmd:str, n:int, arrstr:str)->str:
    '''
    '''
    que = deque()
    s1 = arrstr.strip('[]')
    if s1:
        que = deque(map(int, s1.split(',')))
    assert len(que) == n

    is_reversed = False
    for c in cmd:
        if c == 'R':
            is_reversed = not is_reversed
        elif c == 'D':
            if not que:
                return 'error'
            if is_reversed:
                que.pop()
            else:
                que.popleft()
        else:
            assert False

    # compose to final string
    if is_reversed:
        s1 = ','.join( map(str, reversed(que)) )
    else:
        s1 = ','.join( map(str, que) )
    return '[' + s1 + ']'


T = int(input().strip())
for _ in range(T):
    cmd = input().strip()
    n = int(input().strip())
    arr = input().strip()
    print(solve(cmd, n, arr))
