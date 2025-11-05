'''
1451번
직사각형으로 나누기, 골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	4769	1970	1516	41.855%

문제
세준이는 N*M크기로 직사각형에 수를 N*M개 써놓았다.

세준이는 이 직사각형을 겹치지 않는 3개의 작은 직사각형으로 나누려고 한다.
각각의 칸은 단 하나의 작은 직사각형에 포함되어야 하고,
각각의 작은 직사각형은 적어도 하나의 숫자를 포함해야 한다.

어떤 작은 직사각형의 합은 그 속에 있는 수의 합이다.
입력으로 주어진 직사각형을 3개의 작은 직사각형으로 나누었을 때,
각각의 작은 직사각형의 합의 곱을 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 직사각형의 세로 크기 N과 가로 크기 M이 주어진다.
둘째 줄부터 직사각형에 들어가는 수가 가장 윗 줄부터 한 줄에 하나씩 M개의 수가 주어진다.
N과 M은 50보다 작거나 같은 자연수이고, 직사각형엔 적어도 3개의 수가 있다.
또, 직사각형에 들어가는 수는 한 자리의 숫자이다.

출력
세 개의 작은 직사각형의 합의 곱의 최댓값을 출력한다.

----

9:59~11:00

bruteforce 밖에 없음. 사각형 내합 계산에서 누적합 사용.
제출, 검증 완료


'''



import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().rstrip())))
    return N,M,A


def solve(N:int, M:int, A:list[list[int]])->int:
    '''
    Args:
    Returns:
    '''

    # 누적합 (accumulated sum)
    asum = [ [0]*(M+1) for _ in range(N+1) ]
    # asum 에 대해서만큼은 좌상단 좌표를 (1,1)로 간주하는 것이 편하다.
    # 즉, asum[y][x] 는 (1,1) 부터 (y,x) 까지의 partial sum
    for y in range(1, N+1):
        asum_x = [0]*(M+1)
        for x in range(1, M+1):
            asum_x[x] = asum_x[x-1] + A[y-1][x-1]
            asum[y][x] = asum[y-1][x] + asum_x[x]

    maxval = -1

    # case 1: 세로 분할, 가로 배치 ||.  조건: M>=3
    for i in range(1, M-1):  # i: 첫번째 사각형의 가로길이. 1 ~ M-2
        for k in range(i+1, M): # k: 첫번째와 두번째 사각형의 길이. i+1 ~ M-1
            #   |   k   |
            #   +-i-+---+---+
            #   | 1 | 2 | 3 |
            #   +---+---+---+
            #
            # 각 사각형 내부합
            s1 = asum[N][i] - asum[0][i] - asum[N][0] + asum[0][0]
            s2 = asum[N][k] - asum[0][k] - asum[N][i] + asum[0][i]
            s3 = asum[N][M] - asum[0][M] - asum[N][k] + asum[0][k]
            v = s1*s2*s3
            if v > maxval: maxval = v

    # case 2: 가로 분할. N>=3
    for i in range(1, N-1):  # i: 첫번째 사각형의 세로길이. 1 ~ N-2
        for k in range(i+1, N): # k: 첫번째와 두번째 사각형의 길이. i+1 ~ N-1
            #   +-------+---
            #   |   1   |i
            #   +-------+- k
            #   |   2   |
            #   +-------+---
            #   |   3   |
            #   +-------+
            #
            s1 = asum[i][M] - asum[0][M] - asum[i][0] + asum[0][0]
            s2 = asum[k][M] - asum[i][M] - asum[k][0] + asum[i][0]
            s3 = asum[N][M] - asum[k][M] - asum[N][0] + asum[k][0]
            v = s1*s2*s3
            if v > maxval: maxval = v

    # case 3: T 분할.  N>=2, M>=2
    for i in range(1, N): # i: 위 사각형의 세로 길이. 1 ~ N-1
        for k in range(1, M): # k: 좌하단 사각형의 가로 길이. 1 ~ M-1
            #   +-------+
            #   |   1   |i
            #   +-k-+---+
            #   | 2 | 3 |
            #   +---+---+
            #
            s1 = asum[i][M] - asum[0][M] - asum[i][0] + asum[0][0]
            s2 = asum[N][k] - asum[i][k] - asum[N][0] + asum[i][0]
            s3 = asum[N][M] - asum[i][M] - asum[N][k] + asum[i][k]
            v = s1*s2*s3
            if v > maxval: maxval = v

    # case 4: ㅗ 분할.  N>=2, M>=2
    for i in range(1, N): # i: 위 사각형의 세로 길이. 1 ~ N-1
        for k in range(1, M): # k: 좌상단 사각형의 가로 길이. 1 ~ M-1
            #   +---+---+
            #   | 1 | 2 |i
            #   +-k-+---+
            #   |   3   |
            #   +-------+
            #
            s1 = asum[i][k] - asum[0][k] - asum[i][0] + asum[0][0]
            s2 = asum[i][M] - asum[0][M] - asum[i][k] + asum[0][k]
            s3 = asum[N][M] - asum[i][M] - asum[N][0] + asum[i][0]
            v = s1*s2*s3
            if v > maxval: maxval = v

    # case 5: ㅏ 분할.  N>=2, M>=2
    for i in range(1, N): # i: 우상단 사각형의 세로 길이. 1 ~ N-1
        for k in range(1, M): # k: 좌측 사각형의 가로 길이. 1 ~ M-1
            #   +-k-+---+
            #   |   | 2 |i
            #   | 1 +---+
            #   |   | 3 |
            #   +---+---+
            #
            s1 = asum[N][k] - asum[0][k] - asum[N][0] + asum[0][0]
            s2 = asum[i][M] - asum[0][M] - asum[i][k] + asum[0][k]
            s3 = asum[N][M] - asum[i][M] - asum[N][k] + asum[i][k]
            v = s1*s2*s3
            if v > maxval: maxval = v

    # case 6: ㅓ 분할.  N>=2, M>=2
    for i in range(1, N): # i: 우상단 사각형의 세로 길이. 1 ~ N-1
        for k in range(1, M): # k: 좌측 사각형의 가로 길이. 1 ~ M-1
            #   +-k-+---+
            #   | 1 |   |i
            #   +---+ 3 +-
            #   | 2 |   |
            #   +---+---+
            #
            s1 = asum[i][k] - asum[0][k] - asum[i][0] + asum[0][0]
            s2 = asum[N][k] - asum[i][k] - asum[N][0] + asum[i][0]
            s3 = asum[N][M] - asum[0][M] - asum[N][k] + asum[0][k]
            v = s1*s2*s3
            if v > maxval: maxval = v

    return maxval

if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
1 8
11911103
예제 출력 1
108
예제 입력 2
3 3
123
456
789
예제 출력 2
3264
예제 입력 3
3 1
7
9
3
예제 출력 3
189

----
pr=1451
run=(python3 a$pr.py)

echo '1 8\n11911103' | $run
# 108
echo '3 3\n123\n456\n789' | $run
# 3264
echo '3 1\n7\n9\n3' | $run
# 189


'''

