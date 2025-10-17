'''
1749번
점수따먹기, 골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	4971	1889	1379	36.118%

문제
동주는 항상 혼자 노느라 심심하다.
하지만 혼자 놀기의 고수가 된 동주는 매일매일 게임을 개발하여 혼자놀기의 진수를 우리에게 보여준다.
어느 날 동주는 새로운 게임을 개발하였다. 바로 점수 따먹기라는 게임인데 그다지 재밌어 보이지는 않는다.

동주가 개발한 게임은 이렇다.
일단 N*M 행렬을 그린 다음, 각 칸에 -10,000 이상 10,000 이하의 정수를 하나씩 쓴다.
그런 다음 그 행렬의 부분행렬을 그려 그 안에 적힌 정수의 합을 구하는 게임이다.

동주가 혼자 재밌게 놀던 중 지나가는 당신을 보고 당신을 붙잡고 게임을 하자고 한다.
귀찮은 당신은 정수의 합이 최대가 되는 부분행렬을 구하여 빨리 동주에게서 벗어나고 싶다.

입력
첫째 줄에 N (1 < N < 200), M (1 < M < 200)이 주어진다.
그 다음 N개의 줄에 M개씩 행렬의 원소가 주어진다.

출력
첫째 줄에 최대의 합을 출력하라.

----

7:07~

dp 로는 아무리 생각해 봐도 점화식 조건을 찾을 수 없다.
200x200 정도이고, 특정 부분행렬의 partial sum은 O(1)에 구할 수 있으니
brute force로 진행해도 가능한가?

좌상단 좌표의 가짓수 200x200, 우하단 좌표 가짓수 ~= 200x200
1,600,000,000
brute force 방법은 쓰지 못함...

----
어떻게 어떻게 풀긴 했으나.. 너무 복잡하다.
그리고 더 빠르게 수행되는 다른 답안들도 보임.

일단 다른 누적합, 부분합 문제들을 더 연습한 후 다시 복습이 필요해 보임.


'''

import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)


def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
        assert len(A[-1]) == M
    return N,M,A


def solve(N:int, M:int, A:list[list[int]])->int:
    '''
    Args: A: NxM 2차원 행렬
    Returns: 최대 부분합
    '''
    INF = int(1e9) # 10_000 * (200*200) + 1 # ~== 400 000 000

    # 누적합 (accumulated sum)
    asum = [ [0]*(M+1) for _ in range(N+1) ]
    # asum 에 대해서만큼은 좌상단 좌표를 (1,1)로 간주하는 것이 편하다.
    # 즉, asum[y][x] 는 (1,1) 부터 (y,x) 까지의 partial sum
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

        log("   colsum %s", colsum)
        # N x 1 컬럼 벡터 -> 길이 N 의 1차원 배열이 됨.
        # 이제 y 방향으로 최대 부분합 구하기 -> 1차원 부분합 문제임.
        return kadane(colsum)

    mxsum = -INF
    for x1 in range(M):
        for x2 in range(x1, M):
            log("**** x[%d ~ %d]", x1, x2)
            k = get_max_sum(x1, x2)
            mxsum = max(mxsum, k)
            log("**** x[%d ~ %d] -> k %d, max %d", x1, x2, k, mxsum)

    return mxsum



if __name__ == '__main__':
    print(solve(*get_input()))



'''
예제 입력 1
3 5
2 3 -21 -22 -23
5 6 -22 -23 -25
-22 -23 4 10 2
예제 출력 1
16

----
run=(python3 a1749.py)

echo '3 5\n2 3 -21 -22 -23\n5 6 -22 -23 -25\n-22 -23 4 10 2' | $run
# 16




'''


