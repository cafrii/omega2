import sys, itertools

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
        #assert len(A[-1]) == M
    return N,M,A

def solve(N:int, M:int, A:list[list[int]])->int:
    '''
    Args:
    Returns:
    '''
    INF = int(1e6) # 1000*100*4
    maxval = -INF

    rsum = [ sum(A[y]) for y in range(N) ]
    # rsum[y] 는 row y 의 합. sum(A[y])

    csum = [ sum( A[y][x] for y in range(N) ) for x in range(M) ]
    # csum[x] 는 column x 의 합. sum(A[?][x]])

    # 매 y1,y2 에 대해서 x1, x2 컴비네이션을 구하는 것이 문제다!
    # x combination 을 y1,y2 루프 밖에서 미리 만들어 놓는다.
    x_combi = list(itertools.combinations(range(M), 2))

    for y1,y2 in itertools.combinations(range(N), 2):
        rowval = rsum[y1] + rsum[y2]

        for x1,x2 in x_combi:
            beauty = rowval + csum[x1] + csum[x2] - \
                (A[y1][x1]+A[y1][x2]+A[y2][x1]+A[y2][x2]) + \
                (y2 - y1 - 1) * (x2 - x1 - 1)
            if beauty > maxval: maxval = beauty

    return maxval

if __name__ == '__main__':
    print(solve(*get_input()))
