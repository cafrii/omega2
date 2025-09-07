
import sys

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    Ns = []
    for _ in range(C):
        Ns.append(int(input().rstrip()))
    return Ns,


def solve(Ns:list[int])->list[str]:
    '''
    Args: Ns: list of N to compose
    Returns: list of answer string
    '''
    max_n = max(Ns)
    alloc_n = max(max_n, 4)

    dp = [ [0,0] for k in range(alloc_n+1) ]

    dp[0][0] = dp[0][1] = 1
    # 0을 만드는 경우의 수: 1

    for k in range(1, max_n+1):
        # 1.
        # dp[k][0]: 1 과 2 만을 이용하여 k 를 만드는 방법의 수:
        # 2로 일부분을 채우고, 나머지는 1로 채울 수 있음.
        dp[k][0] = k//2 + 1
        # 2.
        # dp[k][1]: 1,2,3 을 이용하여 k를 만드는 방법의 수
        dp[k][1] = dp[k][0] + dp[k-3][1]

    ans = []
    for n in Ns:
        ans.append(str(dp[n][1]))
    return ans


if __name__ == '__main__':
    ans = solve(*get_input())
    print('\n'.join(ans))
