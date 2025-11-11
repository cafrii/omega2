import sys

def get_input():
    input = sys.stdin.readline
    N,B,A = map(int, input().split())
    P = list(map(int, input().split()))
    return N,B,A,P

def solve_short(N:int, budget:int, half:int, p:list[int])->int:
    p.sort()
    tsum,b = 0,0
    for c in range(N):
        tsum += p[c]//2
        if c - b + 1 > half:
            tsum += (p[b] // 2)
            b += 1
        if tsum > budget:
            return c
        elif tsum == budget:
            return c+1
    return N

if __name__ == '__main__':
    print(solve_short(*get_input()))
