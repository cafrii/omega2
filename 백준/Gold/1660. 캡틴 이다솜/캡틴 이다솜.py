import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N,

def solve(N:int)->int:
    '''
    Args: N: number of balls
    Returns: minimum number of tri-pyramid to compose

    만들 수 있는 사면체의 최소 수는 가능한 한 큰 사면체를 만들려고 시도하는 것이 쉽다.

    greedy 대신 dp를 바로 적용하자.
    bottom up, forward, layered.
    '''
    MAX_N = 300_000
    # max_height = sqrt(MAX_N*2)

    dp = list(range(N+1))  # [0, 1, 2, .., N]
    # dp[k] 는 볼 개수 k로 사면체를 만들 수 있는 사면체의 최소 개수
    # 처음에는 1층 짜리 (볼 1개짜리 사면체) 로만 만드는 경우로 초기화

    j = 0
    for h in range(1, MAX_N):  # 몇 층 까지 할 수 있을지 알 수 없으니 충분히 큰 수로..
        # h: 사면체의 높이. 1, 2, 3...

        b = (h+1)*h//2
        # b: 높이 h 사면체의 바닥층의 볼 수:  (h+1) x h / 2
        #  1, 3, 6, 10, 15, 21, ..

        j += b
        # j: 높이 h의 사면체의 전체 볼 수. 직전 h-1 높이 사면체 볼 수 (j) 에 바닥층 볼 수 (b) 추가
        #  1, 4, 10, 20, 35, 56, ..

        if j > N: break
        # 어느 h 이상이 되면, 보유한 볼 수로는 만들 수 없게 됨.

        for k in range(j, N+1):
            dp[k] = min(dp[k], dp[k-j]+1)

    return dp[N]


if __name__ == '__main__':
    print(solve(*get_input()))
