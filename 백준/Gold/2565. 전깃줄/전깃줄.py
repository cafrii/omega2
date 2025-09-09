import sys

def get_input():
    input = sys.stdin.readline
    M = int(input().rstrip()) # M: 1 ~ 100
    L = [] # link array
    for _ in range(M):
        a,b = map(int, input().split())
        L.append((a, b))
    return L,

def solve(L:list[tuple[int,int]])->int:
    '''
    '''
    L.sort(key=lambda x:x[0])

    R,S = zip(*L)
    # R is sorted, increasing order
    # problem: S 에서 LIS 의 길이를 찾으면 됨.

    N = len(S)
    dp = [ 0 for _ in range(N) ]
    # dp[k]는 S[k]를 마지막으로 포함하는 sub-sequence 의 LIS 길이

    dp[0] = 1  # 단일 요소는 항상 IS

    for k in range(1, N):
        s = S[k] # s: 현재 검토 중인 seq 의 마지막 숫자
        # s 를 덧붙일 수 있는 IS 들 중 최대 길이 찾기
        mx = 1
        for j in range(k): # j: 0 ~ k-1
            if S[j] >= s: continue
            # 이제 S[j] < s 이므로 S[j] 뒤에 s 를 붙일 수 있음.
            mx = max(mx, dp[j]+1)
        dp[k] = mx

    # LIS 길이는 max(dp). LIS 에 포함 안되는 나머지는 모두 제거 필요.
    return N - max(dp)

if __name__ == '__main__':
    print(solve(*get_input()))
