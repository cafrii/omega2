import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = input().rstrip()
    #assert len(A) == N
    return N,A

def solve(N:int, A:str)->int:
    '''
    '''
    dp = [-1] * N
    label = 'BOJ'
    dp[0] = 0

    def find_next(sub:str, cur:int):
        j = A.find(sub, cur+1, N) # j cannot be 0 if found
        return j if j>0 else 0  # 0 means 'not-found'

    def update_dp(k:int, j:int): # jump from k to j (k < j)
        new = dp[k] + (j-k)*(j-k)
        if dp[j] < 0: dp[j] = new
        else: dp[j] = min(dp[j], new)

    for k in range(N):
        if dp[k] < 0: continue
        cur = A[k]
        nxt = label[(label.index(cur) + 1) % 3]
        j = k
        while j := find_next(nxt, j):
            update_dp(k, j)
            
    return dp[N-1]

if __name__ == '__main__':
    print(solve(*get_input()))
