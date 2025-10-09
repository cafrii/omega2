def get_input():
    import sys
    input = sys.stdin.readline
    T = int(input().rstrip())
    A = []
    for _ in range(T):
        A.append(int(input().rstrip()))
    return A,

def solve(A:list[int])->list[int]:
    '''
    Args:
        A: list of N, to be solved against. 1<=N<=1000
    Returns:
        answer list.
        answer: number of recursive palindromes on number N
    '''
    # recursion depth:
    # max N is 1000 -> log_2(1000) = log 1000/log 2 ~= 10

    max_n = max(A)
    dp = [0] * (max_n+1)
    # dp[k]는 숫자 k의 재귀적인 팰린드롬 파티션의 개수

    # 미리 계산된 몇 개의 답
    dp[1] = 1  # 1
    dp[2] = 2  # 1+1, 2
    # dp[3] = 2  # 1+1+1, 3
    # dp[4] = 4  # 1+1+1+1, 2+2, 1+2+1, 4

    def dfs(N:int)->int:
        if N <= 0: return 0
        if dp[N] > 0: return dp[N]
        # <side> [<center>] <side> 형태
        # center 는 side 값에 따라서 없을 수도 있음.
        # side 가 0 인 경우는 N 단독인 경우와 같음.
        # side 값을 1부터 키워가며 찾음.
        num = 1   # N 단독.
        for side in range(1, N//2 + 1): # side: 1 ~ N//2
            num += dfs(side)
        dp[N] = num
        return num

    ans = []
    for n in A:
        ans.append(dfs(n))
    return ans

if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))
