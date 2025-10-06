import sys

def get_input():
    input = sys.stdin.readline
    TC = int(input().rstrip())
    A = []
    for _ in range(TC):
        N = int(input().rstrip())
        Ns = list(map(int, input().split()))
        #assert len(Ns) == N
        M = int(input().rstrip())
        A.append((Ns, M))
    return A

def solve(Ns:list[int], M:int)->int:
    '''
    Args:
        Ns: 사용할 수 있는 동전의 종류 목록
        M: 만들어야 하는 목표 금액.
    Returns:
        Ns 동전들로 M원을 만드는 방법의 수
    '''
    dp = [0] * (M+1)
    # dp[k]는 k원을 만드는 방법의 수
    dp[0] = 1

    for p in Ns:
        # p는 현재 동전의 가치 (price). p는 1~10000
        # p원의 가치를 추가하는 경우를 고려함.
        for k in range(p, M+1):
            if dp[k-p] > 0:
                dp[k] += dp[k - p]
    return dp[M]

if __name__ == '__main__':
    print('\n'.join(map(str, (solve(ns,m) for ns,m in get_input()))))

