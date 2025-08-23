
import sys

def solve(s:str)->int:
    n = len(s)
    ss = set() # substring set
    for i in range(n):
        for j in range(i+1,n+1):
            ss.add(s[i:j])
    return len(ss)

if __name__ == '__main__':
    input = sys.stdin.readline
    s = input().rstrip()
    print(solve(s))
