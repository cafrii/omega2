
import sys

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    return N,K

def solve(N:int, K:int)->str:
    '''
    finds K-th element (1-based) in lexicographic order
    among the cases to compose N using 1, 2 or 3.
    Args:
        N: target number to compose. 1 ~ 11
        K: order to find. 1 <= K <= N
    Returns:
        answer string or '-1' if no answer
    '''
    alloc_n = max(4, N)
    dp:list[list[str]] = [ [] for j in range(alloc_n+1) ]
    # dp[j]는 정수 j를 만드는 방법에 사용되는 숫자들을 문자열 형태로 붙여 표시한 것.

    dp[1] = ['1']
    dp[2] = ['11', '2']
    dp[3] = ['111', '21', '12', '3']

    for j in range(4, N+1):
        for s in dp[j-1]: dp[j].append(s + '1')
        for s in dp[j-2]: dp[j].append(s + '2')
        for s in dp[j-3]: dp[j].append(s + '3')

    # dp[N]은 N을 만드는 방법의 문자열. 정렬 후 검색.
    a1 = sorted(dp[N])

    # 주의: 문제에서의 K번째는 1부터 시작하는 인덱스임.
    return '+'.join(a1[K-1]) if len(a1)>=K else '-1'

if __name__ == '__main__':
    print(solve(*get_input()))

