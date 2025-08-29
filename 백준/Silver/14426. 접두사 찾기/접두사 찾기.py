import sys, bisect

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    S,A = [],[]
    for _ in range(N):
        S.append(input().rstrip())
    for _ in range(M):
        A.append(input().rstrip())
    return S,A

def solve(S:list[str], A:list[str]):
    '''
    '''
    S.sort()
    num_s = len(S)
    matched = 0
    for a in A:
        idx = bisect.bisect_left(S, a)
        if idx < num_s and S[idx][:len(a)] == a:
            matched += 1
    return matched

if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)
