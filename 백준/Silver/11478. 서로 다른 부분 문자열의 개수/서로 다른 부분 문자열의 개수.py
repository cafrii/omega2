
import sys

def solve_fast(s:str)->int:
    n = len(s)
    cnt = 0
    for sn in range(1,n+1): # substr length
        ss = set() # substring set
        for k in range(n+1-sn):
            ss.add(s[k:k+sn])
        cnt += len(ss)
    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    s = input().rstrip()
    print(solve_fast(s))
