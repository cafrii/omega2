import sys

def get_input():
    input = sys.stdin.readline
    T,W = map(int, input().split())
    A = []
    for _ in range(T):
        A.append(int(input().rstrip()))
    return T,W,A

def solve(T:int, W:int, A:list[int])->int:
    '''
    Args:
        T: 수행 단계.  1 ~ 1000
        W: 가능한 최대 움직임 수. 1 ~ 30
    Returns:
        받을 수 있는 자두의 최대 개수
    '''
    dp = [ [0]*(W+1) for _ in range(T+1) ]
    # dp[][]: 해당 상태에서 받은 자두 누적 개수

    for t in range(1, T+1):
        # t=1 일때: w= 0,1
        # t=2      w= 0,1,2
        # t=3      w= 0,1,2,3
        # ...      w= 0,.....W (max)
        for w in range(0, min(t, W)+1):
            k = (1 if A[t-1] == w%2 + 1 else 0) # 이번 단계에서 획득한 자두
            # 이동하지 않은 경우.
            v1 = dp[t-1][w] + (1 if A[t-1] == w%2 + 1 else 0)
            # 이동하는 경우. w >= 1 에서만 가능
            if w > 0:
                v2 = dp[t-1][w-1] + (1 if A[t-1] == w%2 + 1 else 0)
            else:
                v2 = 0
            dp[t][w] = max(dp[t][w], v1, v2)

    return max(dp[T])

if __name__ == '__main__':
    print(solve(*get_input()))

