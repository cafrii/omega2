
import sys
from collections import deque
from typing import Deque,Iterator

def get_input():
    input = sys.stdin.readline
    N = int(input().strip())
    for _ in range(N):
        yield input().strip()
    return

def solve(it:Iterator):
    # it: input iterator
    # return generator of answer output
    que:Deque[int] = deque()

    for line in it:
        words = line.split()
        cmd = words[0]
        param = int(words[1]) if len(words)>1 else 0
        if cmd == 'push':
            que.append(param)
        elif cmd == 'pop':
            yield que.popleft() if que else -1
        elif cmd == 'size':
            yield len(que)
        elif cmd == 'empty':
            yield 0 if que else 1
        elif cmd == 'front':
            yield que[0] if que else -1
        elif cmd == 'back':
            yield que[-1] if que else -1
    return

for ln in solve(get_input()):
    print(ln)
