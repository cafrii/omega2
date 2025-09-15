'''
2229번
조 짜기, 골드5


중간에 시도 했던 코드들.


'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    assert len(A) == N
    return A,



def solve1_dp(A:list[int])->int:
    '''
    순수하게 dp로 계산.
    O(N^3) 이라서 매우 느림.
    '''
    N = len(A)

    dp = [ [0]*(N) for _ in range(N) ]

    def score(B:list[int])->int:
        mn,mx = min(B),max(B)
        return mx - mn

    # dp[j][k] 를 구하는데, 대각선에서부터 우상향으로..

    '''
    dp[j][k] 는 학생 j 부터 k 까지 만 대상으로 검토할 경우의 최대 점수.
    최종 목표는 dp[0][N-1] (모든 학생을 대상) 를 구하는 것.

        0 1 2 3 4
      . - - - - -
    0 | a b c d e
    1 |   a b c d
    2 |     a b c
    3 |       a b
    4 |         a
    '''

    for j in range(N): # j: 0 ~ N-1
        for k in range(0, N-j):
            if j == 0:   # 단독 그룹
                dp[k][k+j] = 0 # 단독 그룹은 점수 0
            elif j == 1:  # 2인 그룹
                dp[k][k+j] = score(A[k:k+2])  # abs(A[k]-A[k+1])
            elif j == 2:  # 3인 그룹
                # 예: dp[0][2] 는 A0 A1 A2 의 경우임.
                # Ak Ak+1 Ak+2
                dp[k][k+j] = max(
                    dp[k][k+j-1] + dp[k+j][k+j], # (Ak Ak+1) (Ak+2)
                    dp[k][k] + dp[k+1][k+j],     # (Ak) (Ak+1 Ak+2)
                    score(A[k:k+j+1]),           # all in one group
                    0)
            else: # j > 2, # 일반 적인 경우
                # 더 작은 규모의 두 문제로 분할하는 경우는 총 j 가지가 있음.
                # 예: j==3 이라면
                #    Ak   Ak+1   Ak+2   Ak+3
                #       ^      ^      ^    <- 분할 가능한 지점들
                #   h=  1      2      3
                #
                max_score = score(A[k:k+j+1])  # 전체 한 조
                for h in range(1,j+1):
                    # h 개 한 조, 그리고 나머지 한 조
                    s = dp[k][k+h-1] + dp[k+h][k+j]
                    max_score = max(max_score, s)
                dp[k][k+j] = max_score

    return dp[0][N-1]


'''
bottom-up 보다는 top-down 이 더 간편해 보임.
'''
def solve2_recursive(A:list[int])->int:
    '''
    '''
    N = len(A)

    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, N+50))

    dp = [ [-1]*(N) for _ in range(N) ]

    def get_score(i:int, j:int)->int:
        sub = A[i:j+1]
        mn,mx = min(sub),max(sub)
        return mx - mn

    def get_max_score(s:int, e:int)->int:
        # A[s] 부터 A[j] 까지를 대상으로 최대 점수.
        if s >= e: return 0
        if dp[s][e] >= 0:
            return dp[s][e]

        # log("fn(%d, %d)", s, e)
        if s+1 == e:
            dp[s][e] = abs(A[s] - A[e])
            return dp[s][e]
        # s  k  e
        max_sc = get_score(s, e)
        for k in range(s, e): # k: s ~ e-1
            max_sc = max(max_sc,
                get_max_score(s, k) + get_max_score(k+1, e))
        dp[s][e] = max_sc
        return max_sc

    return get_max_score(0, N-1)





def solve3_minmax(A:list[int])->int:
    '''
    min, max 의 모든 조합을 미리 계산해 두는 방법.
    solve1_dp 에 비해 약간 빨라지긴 하지만, 여전히 O(N^3)으로, 근본적인 해결책은 안됨.
    '''
    N = len(A)
    INF = 10_001

    dp = [ [0]*(N) for _ in range(N) ]

    mns = [ [INF]*(N) for _ in range(N) ] # min score
    mxs = [ [0]*(N) for _ in range(N) ] # max score

    # min, max 미리 계산.  O(N^2)
    for j in range(0, N):  # 0 ~ N-1
        for k in range(j, N):  # j ~ N-1
            # j 부터 k 까지의 범위 중 단순 최대, 최소 값. (j <= k)
            if j == k:
                mns[j][k] = mxs[j][k] = A[k]
            else:
                mns[j][k] = min(mns[j][k-1], A[k])
                mxs[j][k] = max(mxs[j][k-1], A[k])

    # 구성된 조의 점수
    def score(start, end)->int:
        return mxs[start][end] - mns[start][end]

    # dp[j][k] 를 구하는데, 대각선에서부터 우상향으로..

    '''
    dp[j][k] 는 학생 j 부터 k 까지 만 대상으로 검토할 경우의 최대 점수.
    최종 목표는 dp[0][N-1] (모든 학생을 대상) 를 구하는 것.

        0 1 2 3 4
      . - - - - -
    0 | a b c d e
    1 |   a b c d
    2 |     a b c
    3 |       a b
    4 |         a
    '''

    for j in range(N): # j: 0 ~ N-1
        for k in range(0, N-j):
            if j == 0:   # 단독 그룹
                dp[k][k] = 0 # 단독 그룹은 점수 0
            elif j == 1:  # 2인 그룹
                dp[k][k+1] = score(k, k+1)  # abs(A[k]-A[k+1])
            elif j == 2:  # 3인 그룹
                # 예: dp[0][2] 는 A0 A1 A2 의 경우임.
                # Ak Ak+1 Ak+2
                dp[k][k+2] = max(
                    dp[k][k+1] + dp[k+2][k+2], # (Ak Ak+1) (Ak+2)
                    dp[k][k] + dp[k+1][k+2],   # (Ak) (Ak+1 Ak+2)
                    score(k, k+2),             # all in one group
                    0)
            else: # j > 2, # 일반 적인 경우
                # 더 작은 규모의 두 문제로 분할하는 경우는 총 j 가지가 있음.
                # 예: j==3 이라면
                #    Ak   Ak+1   Ak+2   Ak+3
                #       ^      ^      ^    <- 분할 가능한 지점들
                #   h=  1      2      3
                #
                max_score = score(k, k+j)  # 전체 한 조
                for h in range(1,j+1): # 1 ~ j
                    # h 개 한 조, 그리고 나머지 한 조
                    s = dp[k][k+h-1] + dp[k+h][k+j]
                    max_score = max(max_score, s)
                dp[k][k+j] = max_score

    return dp[0][N-1]


def solve4_greedy(A:list[int])->int:
    '''
    아이디어는 참신했지만, 결국 greedy 방식인데, 이게 최적의 해를 보장하지 못함.
    '''
    N = len(A)
    INF = 10_001

    # dp = [ [0]*(N) for _ in range(N) ]

    mns = [ [INF]*(N) for _ in range(N) ] # min score
    mxs = [ [0]*(N) for _ in range(N) ] # max score

    # min, max 미리 계산.  O(N^2)
    for j in range(0, N):  # 0 ~ N-1
        for k in range(j, N):  # j ~ N-1
            # j 부터 k 까지의 범위 중 단순 최대, 최소 값. (j <= k)
            if j == k:
                mns[j][k] = mxs[j][k] = A[k]
            else:
                mns[j][k] = min(mns[j][k-1], A[k])
                mxs[j][k] = max(mxs[j][k-1], A[k])

    # 구성된 조의 점수
    def score(start, end)->int:
        return mxs[start][end] - mns[start][end]

    '''
        1. 증가 구간, 감소 구간으로 나눈다.
        전환점은 두 번 포함이 되는데..
            예: [8, 6, 1, 4, 7, 5, 3, 2]
            -> (8 6 1) (1 4 7) (7 5 3 2)
        전환점을 어느 그룹에 소속 시킬지에 따라, 각 그룹은 1씩 더 작을 수도 있다.
            (8 6) (1 4 ..)
            (8 6 1) (4 ..)
            # 1을 왼쪽 조에 포함시키면 +5를 얻고, 오른쪽 조에 포함시키면 +3을 얻으니, 당연히 왼쪽 조가 더 유리하다.
                .. 4) (7 5 3 2)
                .. 4 7) (5 3 2)
            # 7을 왼쪽 조에 포함시키면 +3, 오른쪽 조는 +2 이므로 왼쪽 조가 더 유리.
            정답: (8 6 1) (4 7) (7 5 3 2)

        2. 짧은 구간
            예: [ 2 5 3 6 ]
                (2 5) (3 ..)  +3
                (2) (5 3 ..)  +2
            앞의 규칙에 의해 전환점 5는 앞에 붙여야 한다.
            그런데, 그렇게 하고 나면 3은 감소가 아니라 다시 증가의 시작이 됨.


        2. 평지 구간
            예: [ 2 4 4 5 ]
            (2 4 4 5) -> 3
            (2 4) (4 5) -> 2+1 = 3

            어쨌든 중간에 '나눔'으로 인해 더 이익이 증가하진 않으니 나누지 않아도 상관 없음.

        3. 전환점이 여럿
            예: [ 3 5 8 8 2 1 ]
            (3 5 8 8) (2 1) -> 5+1=6
            (3 5 8) (8 2 1) -> 5+7=12
            (3 5) (8 8 2 1) -> 2+7=9

    '''
    if N == 1: return 0

    start, end = 0, N-1

    inc = [ A[k-1]<=A[k] for k in range(1,N) ]
    # inc[0] 는 A[0]->A[1] 이 increase 라는 의미

    # def deltaplusone(i:int)->int:
    #     d = A[i] - A[i-1]
    #     if d > 0: d += 1
    #     elif d < 0: d -= 1
    #     return d
    # delta1 = [ deltaplusone(k) for k in range(1,N) ]

    total_score = 0

    def add_score(start, end, desc=''):
        nonlocal total_score
        sc = score(start, end)
        log("%s [%d~%d] (%d .. %d), %+d -> %d", desc, start, end, A[start], A[end], sc, total_score)
        total_score += sc

    def chunk():
        nonlocal start, end, total_score

        log("*** chunk(%d, %d)", start, end)

        # assert start <= end:
        length = end - start + 1
        if length == 1:
            # total score not change
            start = end+1
            return
        if length == 2:
            add_score(start, end)
            # log("[%d~%d] (%d .. %d), %+d -> %d", start, end, A[start], A[end], sc, total_score)
            # total_score += score(start, end)
            start = end+1
            return

        is_inc = (A[start] <= A[start+1])

        # for i in range(start+1, end): # start+1 ~ end-1
        #     if A[i-1] <= A[i] <= A[i+1]:
        #         continue  # keep increasing
        #     if A[i-1] >= A[i] >= A[i+1]:
        #         continue  # keep decreasing

        for i in range(start+1, end+1): # start+1 ~ end

            if is_inc:
                if A[i-1] <= A[i]: continue # keep increasing
                # A[i-1] > A[i]  # A[i] is pivot point.
                # A[i]를 앞 조에 포함시킬 것인지, 아니면 뒤 조에 포함시킬지는 바로 판단.
                benefit1 = A[i-1] - A[i-2]
                benefit2 = A[i-1] - A[i]
                if benefit1 >= benefit2:
                    #          A[i-1]
                    #        /       A[i]
                    #  A[i-2]
                    # 앞 조에 포함시킨다.
                    # sc = score(start, i-1)
                    # total_score += sc
                    # log("inc [%d~%d] (%d .. %d), %+d -> %d", start, i-1, A[start], A[i-1], sc, total_score)
                    add_score(start, i-1, 'inc')
                    start = i
                else:
                    #        A[i-1]
                    #  A[i-2]      \
                    #               A[i]
                    # 뒷 조에 포함. A[i-2] 에서 끊기.
                    # sc = score(start, i-2)
                    # total_score += sc
                    # log("inc [%d~%d] (%d .. %d), %+d -> %d", start, i-2, A[start], A[i-2], sc, total_score)
                    add_score(start, i-2, 'inc')
                    start = i-1
                is_inc = False
                return

            else: # not inc
                if A[i-1] >= A[i]: continue # keep decreasing
                    #   A[i-2]         A[i]
                    #          A[i-1]
                if A[i-2] - A[i-1] >= A[i] - A[i-1]: # 앞 쪽에 포함
                    # sc = score(start, i-1)
                    # total_score += sc
                    # log("dec [%d~%d] (%d .. %d), %+d -> %d", start, i-1, A[start], A[i-1], sc, total_score)
                    add_score(start, i-1, 'dec')
                    start = i
                else:                   # 뒤 쪽에 포함
                    # sc = score(start, i-2)
                    # total_score += sc
                    # log("dec [%d~%d] (%d .. %d), %+d -> %d", start, i-2, A[start], A[i-2], sc, total_score)
                    add_score(start, i-2, 'dec')
                    start = i-1
                is_inc = True
                return

        # sc = score(start, end)
        # total_score += sc
        # log("[%d~%d] (%d .. %d), %+d -> %d", start, end, A[start], A[end], sc, total_score)
        add_score(start, end, '--')
        start = end+1
        return

    log("A: %s", A)
    while start <= end:
        chunk()

    return total_score


def solve5(A:list[int])->int:
    '''
    solve4 의 방식을 쓰되 모든 경우의 전환점 경우를 다 고려.
    전환점의 개수는 최대 N-2 개 이므로 경우의 수가 2^(N-2) 가지로 보이지만
    memoization을 적용하면 그 보다는 적어지지 않을까?
    '''
    N = len(A)
    INF = 10_001

    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, N+50))

    dp = [ [-1]*(N) for _ in range(N) ]
    # dp[j][k] 는 Aj 부터 Ak 까지 범위에서 조 구성의 모든 경우 중 최대 점수.
    # 우리가 최종적으로 구하고자 하는 값은 dp[0][N-1]
    # dp[][] 값이 <0 이면 아직 계산이 안된 경우.
    # 주의: 우리는 모든 dp 값을 다 구하려고 시도하지 않는다.

    mins = [ [INF]*(N) for _ in range(N) ] # min score
    maxs = [ [0]*(N) for _ in range(N) ] # max score

    # min, max 미리 계산.  O(N^2)
    # 이 계산만 수행하는 데 대략 90ms 정도 소요됨. (내 macbook 기준)
    for j in range(0, N):  # 0 ~ N-1
        for k in range(j, N):  # j ~ N-1
            # j 부터 k 까지의 범위 중 단순 최대, 최소 값. (j <= k)
            if j == k:
                mins[j][k] = maxs[j][k] = A[k]
            else:
                mins[j][k] = min(mins[j][k-1], A[k])
                maxs[j][k] = max(maxs[j][k-1], A[k])

    if N == 1: return 0

    def add_score(start, end, desc=''):
        # [start 와 end] 가 단일 조로 구성되었음.
        sc = maxs[start][end] - mins[start][end]
        # log("%s [%d: %d] [%d, .. %d], ret %d", desc, start, end, A[start], A[end], sc)
        dp[start][end] = sc
        return sc

    def get_max_score(start:int, end:int)->int:
        '''
            start, end 는 A[] 의 인덱스.
            A[start] 부터 A[end] 범위 (inclusive)에서 조 구성 경우 중 최대 점수를 리턴.
            start <= end
        '''
        if start > end: return 0 # 비정상 호출.

        # log("*** chunk(%d, %d)", start, end)

        if dp[start][end] >= 0:  # memoized
            return dp[start][end]

        length = end - start + 1
        if length == 1: # start == end
            dp[start][end] = 0; return 0

        if length == 2:
            return add_score(start, end, '-')

        # assert length >= 3
        delta0 = A[start+1] - A[start] # 초기 방향

        # 증감 방향이 바뀌는 부분을 찾는다.
        for i in range(start+1, end+1): # start+1 ~ end
            delta = A[i] - A[i-1]
            # 초기 방향이 없는 경우, 방향 늦은 초기화
            if delta0 == 0 and delta != 0:
                delta0 = delta
            # 방향이 같으면 계속 탐색.
            if delta0 == 0 or (delta0 < 0 and delta <= 0) or (delta0 > 0 and delta >= 0):
                continue
            # 방향이 바뀌었음. 아래는 예시. (증 -> 감)
            #        A[i-1]
            #  A[i-2]       A[i]
            dir = 'inc' if delta0 > 0 else 'dec'

            # A[i]를 앞 조에 포함시키는 경우. A[i-1] 에서 끊기
            sc1 = add_score(start, i-1, dir) + get_max_score(i, end)

            # 뒷 조에 포함시키는 경우. A[i-2] 에서 끊기. 참고: i>=2 가 보장됨.
            sc2 = add_score(start, i-2, dir) + get_max_score(i-1, end)

            sc = max(sc1, sc2)
            dp[start][end] = sc
            return sc

        # 방향 전환 없이 루프 종료
        sc = add_score(start, end, '--')
        dp[start][end] = sc
        return sc

    # log("A: %s", A)
    return get_max_score(0, N-1)




if __name__ == '__main__':
    # print(solve1_dp(*get_input()))
    # print(solve2_recursive(*get_input()))
    r = get_input()
    print(solve3_minmax(*r))
    print(solve4_greedy(*r))



