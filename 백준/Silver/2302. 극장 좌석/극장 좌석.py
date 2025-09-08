
import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip()) # 1 ~ 40
    M = int(input().rstrip()) # 0 ~ N
    A = []
    for _ in range(M):
        A.append(int(input().rstrip()))
    return N,A

def solve(N:int, A:list[int])->int:
    '''
    Args:
        N: number of seats (1~N)
        A: seat number of VIPs
    Returns:
        number of allowed cases
    '''

    L = [1] # guarantee non-empty
    # normal seats between two vips
    # record only >=2 numbers

    b = 1  # pre-a
    for a in A:
        L.append(a-b) if a-b>1 else None
        b = a+1
    L.append(N+1-b) if N+1-b>1 else None

    max_l = max(L)
    alloc_l = max(max_l, 3)
    dp = [0] * (alloc_l+1)

    '''
        allowed cases of 1 ~ L seat
        [ 1 ] -> 1
        [ 1, 2 ] -> 2
        [ 1, 2, 3 ] -> 123, 213, 132 -> 3
        [1,2,3,4] -> 1234 2134 1324 1243 2143 -> 5
        일반화: [1,2,..k-2,k-1,k]

        k위치 안바뀌는 경우 => dp[k-1]
        k가 k-1과 바뀌는 경우 => dp[k-2]
    '''
    dp[1:2] = [1, 2]
    for k in range(3, max_l+1): # 필요한 만큼만 계산
        dp[k] = dp[k-1] + dp[k-2]

    ans = 1
    for k in L: ans *= dp[k]

    return ans

if __name__ == '__main__':
    print(solve(*get_input()))
