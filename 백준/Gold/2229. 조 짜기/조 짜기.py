import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    assert len(A) == N
    return A,

def solve6(A:list[int])->int:
    '''
    '''
    N = len(A)
    INF = 10_001

    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, N+50))

    dp = [ [-1]*(N) for _ in range(N) ]
    # dp[j][k] 는 Aj 부터 Ak 까지 범위에서 조 구성의 모든 경우 중 최대 점수.
    # dp[][] 값이 <0 이면 아직 계산이 안된 경우.

    mins = [ [INF]*(N) for _ in range(N) ] # min score
    maxs = [ [0]*(N) for _ in range(N) ] # max score

    # min, max 미리 계산.  O(N^2)
    for j in range(0, N):  # 0 ~ N-1
        for k in range(j, N):  # j ~ N-1
            # j 부터 k 까지의 범위 중 단순 최대, 최소 값. (j <= k)
            if j == k:
                mins[j][k] = maxs[j][k] = A[k]
            else:
                mins[j][k] = min(mins[j][k-1], A[k])
                maxs[j][k] = max(maxs[j][k-1], A[k])

    if N == 1: return 0

    def memoize_score(start, end):
        # [start 와 end] 가 단일 조로 구성되었음.
        sc = maxs[start][end] - mins[start][end]
        dp[start][end] = sc
        return sc

    def get_max_score(start:int, end:int)->int:
        '''
            start, end 는 A[] 의 인덱스.
            A[start] 부터 A[end] 범위 (inclusive)에서 조 구성 경우 중 최대 점수를 리턴.
            start <= end
        '''
        if start > end: return 0 # 비정상 호출.

        if dp[start][end] >= 0:  # memoized
            return dp[start][end]

        length = end - start + 1
        if length == 1: # start == end
            dp[start][end] = 0; return 0

        if length == 2:
            return memoize_score(start, end)

        # assert length >= 3
        delta0 = A[start+1] - A[start] # 초기 방향. { 음수, 0, 양수 } 중 한가지.

        # 증감 방향이 바뀌는 부분을 찾는다.
        #  A[i-1] ↑ A[i] ↓ A[i+1] : up -> down
        #  A[i-1] ↓ A[i] ↑ A[i+1] : down -> up

        for i in range(start+1, end): # i: start+1 ~ end-1
            delta = A[i+1] - A[i]
            # 초기 방향이 없었던 경우라면, 지금 초기 방향을 설정
            if delta0 == 0 and delta != 0:
                delta0 = delta
            # 방향이 같으면 계속 탐색.
            if delta0 == 0 or (delta0 < 0 and delta <= 0) or (delta0 > 0 and delta >= 0):
                continue

            # A[i]를 앞 조에 포함시키는 경우.
            sc1 = memoize_score(start, i) + get_max_score(i+1, end)
            # A[i]를 뒷 조에 포함시키는 경우.
            sc2 = memoize_score(start, i-1) + get_max_score(i, end)

            sc = max(sc1, sc2) # 두 가지 경우 중 최대값
            dp[start][end] = sc
            return sc

        # 방향 전환 없이 루프 종료 한 경우
        sc = memoize_score(start, end)
        dp[start][end] = sc
        return sc

    return get_max_score(0, N-1)

if __name__ == '__main__':
    print(solve6(*get_input()))
