import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    S = input().rstrip()
    #assert len(S)==N
    return N,S

'''
    기존 solve()를 좀 더 최적화.
    dp의 업데이트 순서를 조정하면 dpx 를 따로 마련할 필요가 없어진다.
'''
def solve2(N:int, S:str)->int:
    '''
    Args:
    Returns:
    '''
    dp = [0]*4

    for s in S:
        if s == 'H':
            dp[3] += dp[2]
        elif s == 'S':
            dp[2] += dp[1]
        elif s == 'K':
            dp[1] += dp[0]
        elif s == 'D':
            dp[0] += 1

    return dp[3]

if __name__ == '__main__':
    print(solve2(*get_input()))
