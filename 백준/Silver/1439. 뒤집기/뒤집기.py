
import sys

def solve(S:str)->int:
    # count number of changes, 0->1 or 1->0
    num = sum( (1 if S[i-1]!=S[i] else 0) for i in range(1,len(S)) )
    return ((num+1) // 2)

if __name__ == '__main__':
    input = sys.stdin.readline
    S = input().rstrip()
    print(solve(S))
