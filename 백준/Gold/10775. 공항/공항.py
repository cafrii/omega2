import sys
from typing import Iterator

def get_input():
    input = sys.stdin.readline
    G = int(input().rstrip())
    P = int(input().rstrip())
    def gen():
        for i in range(P):
            gi = int(input().rstrip())
            yield i,gi
        return
    return G,P,gen()

def solve(G:int, P:int, it:Iterator)->int:
    '''
    it: iterator which yield (seq,gi) where
        gi is gate index (1-based) for plane will arrive at,
        seq is sequence index of iteration (start from 0)
    '''
    gates = list(range(G+1))
    # gates[k]: k번 gate 의 상태 정보
    #   k: 이 gate가 available 하면 자신 gate 번호.
    #   <k: 이 gate가 occupied 이면, 자신 번호보다 작은 gate 중,
    #       available 한 (available 할 것으로 예상하는) gate 번호
    #   0: 이 gate 포함 이전 gate 모두 full occupied
    # gates[0] is always 0 (fixed!)

    def find_root(a:int)->int:
        if a == gates[a]: return a
        stack = []
        while a != gates[a]:
            stack.append(a)
            a = gates[a]
        for s in stack: gates[s] = a
        return a

    for i,a in it:
        ra = find_root(a)
        if ra == 0: return i  # all gates (< a) occupied
        gates[ra] = find_root(ra-1)

    return P


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)

