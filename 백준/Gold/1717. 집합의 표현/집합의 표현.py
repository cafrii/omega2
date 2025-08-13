import sys
from typing import Iterator

def get_input()->tuple[int,Iterator]:
    input = sys.stdin.readline
    N,M = map(int, input().split())
    def gen():
        for _ in range(M):
            c,a,b = map(int, input().split())
            yield c,a,b
        return
    return N,gen()

def solve(N:int,it:Iterator)->Iterator:
    '''
    '''
    roots = list(range(N+1))

    def find_root(a:int):
        if a == roots[a]: return a
        stack = []
        while a != roots[a]:
            stack.append(a)
            a = roots[a]
        for s in stack: roots[s] = a
        return a

    for cmd,a,b in it:
        ra,rb = find_root(a),find_root(b)
        if cmd == 1:
            yield 'YES' if ra == rb else 'NO'
        else:
            if ra == rb: continue
            roots[b] = roots[rb] = ra
    return

if __name__ == '__main__':
    inp = get_input()
    for s in solve(*inp): print(s)
