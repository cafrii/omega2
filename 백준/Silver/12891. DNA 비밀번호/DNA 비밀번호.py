import sys

def get_input():
    input = sys.stdin.readline
    S,P = map(int, input().split())
    rstr = input().rstrip() # random string
    mc = list(map(int, input().split())) # min. count
    # assert len(mc) == 4, "wrong mc"
    return rstr,P,mc

from collections import defaultdict

def solve(rstr:str, P:int, mc:list[int])->int:
    '''
    '''
    N = len(rstr)
    s = 0 # start position of substr
    count = 0 # valid string count
    usecnt = defaultdict(int)

    def is_valid()->bool:
        return usecnt['A']>=mc[0] and usecnt['C']>=mc[1] and \
            usecnt['G']>=mc[2] and usecnt['T']>=mc[3]

    # initial pooling
    for k in range(s,s+P): # s ~ s+P-1
        usecnt[rstr[k]] += 1
    if is_valid():
        count += 1

    for s in range(1, N-P+1):
        # remove rstr[s-1] and add rstr[s+P]
        usecnt[rstr[s-1]] -= 1
        usecnt[rstr[s+P-1]] += 1
        if is_valid():
            count += 1

    return count


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)
