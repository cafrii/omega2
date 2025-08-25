import sys

'''
과목: 1~ 양수.
과목의 수: 1 ≤ N ≤ 1000
선수조건:  0 ≤ M ≤ 500_000
'''

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    links = []
    for _ in range(M):
        a,b = map(int, input().split())
        links.append((a,b))
    return N,links

def solve(N:int, links:list[tuple[int,int]])->list[int]:
    '''
    '''
    links.sort()
    dp = [1] * N
    for a,b in links:
        dp[b-1] = max(dp[a-1]+1, dp[b-1])
    return dp

if __name__ == '__main__':
    inp = get_input()
    lst = solve(*inp)
    print(' '.join(map(str, lst)))
