import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    #assert len(A) == N
    return N,A

def solve3(N:int, A:list[int])->int:
    '''
    using recursive call with memoization
    '''
    # dimension up
    if N < 3: A = A + [0]*(3-N)

    MAX_HP = 60
    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, MAX_HP + 10))

    dp = [[ [-1]*(MAX_HP+1) for j in range(MAX_HP+1) ] for k in range(MAX_HP+1) ]
    dp[0][0][0] = 0

    def count(a, b, c):
        dpv = dp[a][b][c]
        if dpv >= 0: return dpv

        ans = min(
                count(max(a-9, 0), max(b-3, 0), max(c-1, 0)),
                count(max(a-9, 0), max(b-1, 0), max(c-3, 0)),
                count(max(a-3, 0), max(b-9, 0), max(c-1, 0)),
                count(max(a-3, 0), max(b-1, 0), max(c-9, 0)),
                count(max(a-1, 0), max(b-3, 0), max(c-9, 0)),
                count(max(a-1, 0), max(b-9, 0), max(c-3, 0)),
            ) + 1
        dp[a][b][c] = ans
        return ans

    return count(*A)

if __name__ == '__main__':
    print(solve3(*get_input()))  # solve3 is fastest
