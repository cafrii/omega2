import sys

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
    Args: A: NxM 2차원 행렬
    Returns: 최대 부분합
    '''
    INF = int(1e9) # 10_000 * (200*200) + 1 # ~== 400 000 000

    # 누적합 (accumulated sum)    
    # asum 에 대해서만큼은 좌상단 좌표를 (1,1)로 간주하는 것이 편하다.
    # 즉, asum[y][x] 는 (1,1) 부터 (y,x) 까지의 partial sum
    asum = [ [0]*(M+1) for _ in range(N+1) ]

    for y in range(1, N+1):
        asum_x = [0]*(M+1)
        for x in range(1, M+1):
            asum_x[x] = asum_x[x-1] + A[y-1][x-1]
            asum[y][x] = asum[y-1][x] + asum_x[x]

    # 이후부터는 모두 zero-based index.

    def get_partial_sum(y1:int,x1:int, y2:int,x2:int)->int:
        '''
            누적합을 이용해 부분합을 O(1)시간안에 구한다.
            asum의 단위가 +1 offset 이 있으므로 주의.
        '''
        return asum[y2+1][x2+1] - asum[y1][x2+1] - asum[y2+1][x1] + asum[y1][x1]

    def kadane(lst:list[int])->int:
        '''
            주어진 배열에서의 최대 부분합을 구한다.
        '''
        max_sum = -INF
        cur_sum = 0
        for a in lst:
            cur_sum = max(a, cur_sum + a)
            max_sum = max(max_sum, cur_sum)
        return max_sum

    def get_max_sum(x1:int, x2:int)->int:
        '''
            x 방향으로 일부만 선택한 영역 내에서 최대 부분합을 구한다.
            예: 3x5 행렬에서, x1=2, x2=3 부분 영역 내에서 구하기
                아래 A 의 범위에서만 최대 부분합을 구한다.
                0 1 2 3 4 5
            0   . . A A . .
            1   . . A A . .
            2   . . A A . .
        '''
        # 먼저 x 방향으로 모두 sum을 구함. 이때 앞서 구해 놓은 누적합을 활용.
        colsum = [ get_partial_sum(y, x1, y, x2) for y in range(N) ]

        # N x 1 컬럼 벡터 -> 길이 N 의 1차원 배열이 됨.
        # 이제 y 방향으로 최대 부분합 구하기 -> 1차원 부분합 문제임.
        return kadane(colsum)

    mxsum = -INF
    for x1 in range(M):
        for x2 in range(x1, M):
            k = get_max_sum(x1, x2)
            mxsum = max(mxsum, k)

    return mxsum

if __name__ == '__main__':
    print(solve(*get_input()))

