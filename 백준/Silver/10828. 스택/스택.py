
import sys
from typing import Iterator

input = sys.stdin.readline

def get_input():
    input = sys.stdin.readline
    N = int(input().strip())
    # N: 1~10000

    for _ in range(N):
        yield input().strip()
    return

def solve(it:Iterator):
    # it: input iterator
    # return generator of answer output
    stack:list[int] = []

    for line in it:
        words = line.split()
        cmd = words[0]
        param = int(words[1]) if len(words)>1 else 0
        if cmd == 'push':
            stack.append(param)
        elif cmd == 'pop':
            yield stack.pop() if stack else -1
        elif cmd == 'size':
            yield len(stack)
        elif cmd == 'empty':
            yield 0 if stack else 1
        elif cmd == 'top':
            yield stack[-1] if stack else -1
    return


for ln in solve(get_input()):
    print(ln)
