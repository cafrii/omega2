'''
25708번
만남의 광장, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	381	210	178	55.108%

문제
인하대학교의 마스코트인 인덕이가 사는 인경호는 인하대학교 학생이 아니여도
주변에 거주하는 사람들이 산책로로 이용할 수 있다.
인하대학교는 인경호에서 산책하는 사람들이 많은 것을 알고
이들을 위해 인경호 근처에 적당한 녹지를 골라 만남의 광장을 만들기로 하였다.

만남의 광장은 위 그림과 같이 N × M 크기의 녹지에 각각 다른 행을 골라
가로 방향으로 2개, 각각 다른 열을 골라 세로 방향으로 2개의 직선으로 뻗은 4개의 길을 놓아 만든다.
녹지의 i행 j열의 칸에는 가치 dij가 정해져있다.

인하대학교는 녹지에 만남의 광장을 만들 때 광장의 아름다움을 최대화하려고 한다.
이때, 광장의 아름다움이란 4개의 길에 둘러싸인 직사각형 꼴 영역에 포함된 녹지인 칸의 개수에
길이 깔린 모든 칸의 가치를 더한 값이다. 광장의 아름다움은 0보다 작을 수 있다.

만남의 광장을 만들기 위해 고른 녹지의 크기와 모든 칸 각각의 가치가 주어질 때,
만남의 광장의 아름다움을 최대화했을 때의 아름다움을 출력하여라.

입력
첫 번째 줄에 만남의 광장을 만들 녹지의 크기 N과 M이 공백으로 구분되어 주어진다.

두 번째 줄부터 N개의 줄에 걸쳐 녹지의 각 칸에 길을 놓을 때
광장의 아름다움에 영향을 끼치는 정도 dij가 M개씩 공백으로 구분되어 주어진다.

출력
주어진 녹지에 만남의 광장을 만들 때 광장의 아름다움의 최댓값을 출력한다.

제한
2 ≤ N ≤ 100
2 ≤ M ≤ 100
-1,000 ≤ dij ≤ 1,000

--------

주의: PyPy3 로 제출해야 함!


11:40~

100x100 정도의 크기이므로 brute-force 로 먼저 시도해 본다.
모든 행, 열의 합을 미리 계산해 놓는 것이 좋겠음.

일단 pass는 했는데 시간이 다른 제출자 평균 보다 더 걸림.
O(N^4)가 아니라 O(N^3)로 하는 방법이 있는 듯.
맨 안쪽 루프를 x1, x2 다 탐색하지 않고 x2만 탐색.
이 안쪽 루프에서 누적합 기법을 쓰는 것인가?

참고: https://www.acmicpc.net/source/97804471

같은 코드로 보이는데 왜 3배나 더 많은 시간이 걸릴 수도 있음.

100241051  cafrii        25708  맞았습니다!!  110968   360 ms  PyPy3 1210
100083935  gcn8099       25708  맞았습니다!!  111380  1056 ms  PyPy3  904
99797719   tmdals77177   25708  맞았습니다!!  111600   408 ms  PyPy3  665

x combi 를 루프 밖으로 빼서 시간 단축 시킴. 그러면 400 ms 수준이 될 것으로 예상.
ok.

'''


import sys, itertools

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
    Args:
    Returns:
    '''
    INF = int(1e6) # 1000*100*4
    maxval = -INF

    rsum = [ sum(A[y]) for y in range(N) ]
    # rsum[y] 는 row y 의 합. sum(A[y])

    csum = [ sum( A[y][x] for y in range(N) ) for x in range(M) ]
    # csum[x] 는 column x 의 합. sum(A[?][x]])

    log("rsum %s", rsum)
    log("csum %s", csum)

    # 매 y1,y2 에 대해서 x1, x2 컴비네이션을 구하는 것이 문제다!
    # x combination 을 y1,y2 루프 밖에서 미리 만들어 놓는다.
    x_combi = list(itertools.combinations(range(M), 2))

    for y1,y2 in itertools.combinations(range(N), 2):
        # log("%d %d", y1, y2)
        rowval = rsum[y1] + rsum[y2]

        for x1,x2 in x_combi:
            beauty = rowval + csum[x1] + csum[x2] - \
                (A[y1][x1]+A[y1][x2]+A[y2][x1]+A[y2][x2]) + \
                (y2 - y1 - 1) * (x2 - x1 - 1)

            if beauty > maxval: maxval = beauty

    return maxval

if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
4 4
8 2 1 4
2 3 7 4
4 1 2 3
5 6 9 1
예제 출력 1
58

예제 입력 2
3 6
-9 -1 -3 13 -8 -14
-6 -20 -15 0 14 4
-6 7 18 13 14 4
예제 출력 2
46

예제 입력 3
10 10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
예제 출력 3
100

-------
pr=25708
run=(python3 a$pr.py)

echo '4 4\n8 2 1 4\n2 3 7 4\n4 1 2 3\n5 6 9 1' | $run
# 58
echo '3 6\n-9 -1 -3 13 -8 -14\n-6 -20 -15 0 14 4\n-6 7 18 13 14 4' | $run
# 46
echo '10 10\n1 1 1 1 1 1 1 1 1 1\n1 1 1 1 1 1 1 1 1 1\n1 1 1 1 1 1 1 1 1 1\n1 1 1 1 1 1 1 1 1 1\n1 1 1 1 1 1 1 1 1 1\n1 1 1 1 1 1 1 1 1 1\n1 1 1 1 1 1 1 1 1 1\n1 1 1 1 1 1 1 1 1 1\n1 1 1 1 1 1 1 1 1 1\n1 1 1 1 1 1 1 1 1 1' | $run
# 100


'''

