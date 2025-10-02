'''
중간 구현 버전들.


'''

import sys


def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    return N,K


def solve(N:int, K:int)->str:
    '''
    Args:
        N: target goal
        K: allowed steps
    Returns:
        str
    '''

    def find_prev(n:int)->int:
        '''
        find i, which i + (i//2) == n
        return >N if not exist
        '''
        f,i = n/3,n//3
        if f == i:
            return i*2
        i = int(f*2)
        # there are lower canidates: i, i+1
        if i + i//2 == n: return i
        if (i+1) + (i+1)//2 == n: return i+1
        return N+1

    dp = [0] * (N+1)
    dp[N] = 1
    mn,mx = N,N

    for k in range(1, K+1):
        dpx = [0] * (N+1)
        mn2 = mx  # next mn value
        for n in range(mx, mn-1, -1):
            if not dp[n]: continue
            nx1, nx2 = n-1, find_prev(n)
            if nx1 >= 0:
                dpx[nx1] = 1
                mn2 = min(mn2, nx1)
            if nx2 <= N:
                dpx[nx2] = 1
                mn2 = min(mn2, nx2)
        dp = dpx
        mn,mx = mn2, mx-1
        # log("k %3d, (%d~%d): dp %s", k, mn,mx, dp)

    # dp[0]에 K번째 도달 가능 여부 정보가 저장되어 있음
    return 'minigimbob' if dp[0] > 0 else 'water'


def solve_timeout(N:int, K:int)->str:
    dp = [0] * (N+1)
    dp[0] = 1
    mn,mx = 0,0

    for k in range(1, K+1):
        dpx = [0] * (N+1)
        for n in range(mn, mx+1):
            if not dp[n]: continue
            nx1, nx2 = n+1, n + n//2
            if nx1 <= N: dpx[nx1] = 1
            if nx2 <= N: dpx[nx2] = 1

        dp = dpx
        mx = min(N, max(mx+1, mx+mx//2))
        log("k %3d, mx %3d: dp %s", k, mx, dp)

    return 'minigimbob' if dp[N] > 0 else 'water'


if __name__ == '__main__':
    # r = solve(*get_input())
    # print(r)
    print(solve(*get_input()))

