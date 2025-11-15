import sys, bisect

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    return N,M,A,B

def solve(Nhi:int, Narc:int, Ahi:list[int], Aarc:list[int])->list[int]:
    '''
    Args:
    Returns:
    '''
    ans = [0]*3  # HI winner, ARC winner, draw
    # 길이가 좀 더 긴 쪽을 이분탐색의 대상으로 하자.
    if Nhi > Narc:
        Ahi.sort()
        for a in Aarc:
            lf = bisect.bisect_left(Ahi, a)
            rg = bisect.bisect_right(Ahi, a)
            ans[1] += lf # arc winner
            ans[2] += (rg - lf)
            ans[0] += Nhi - rg
    else: # Nhi <= Narc
        Aarc.sort()
        for a in Ahi:
            lf = bisect.bisect_left(Aarc, a)
            rg = bisect.bisect_right(Aarc, a)
            ans[0] += lf # hi winner
            ans[2] += (rg - lf)
            ans[1] += Narc - rg

    return ans

if __name__ == '__main__':
    print(*solve(*get_input()))
