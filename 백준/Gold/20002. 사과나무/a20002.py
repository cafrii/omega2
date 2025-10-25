'''
20002번
사과나무 성공, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	2134	1161	957	56.998%

문제
N x N 크기의 정사각형 모양 과수원이 있고,
N x N 개의 사과나무가 1 x 1 크기의 간격으로 모든 칸에 심어져있다.

농부 형곤이가 가을을 맞아 사과를 수확하려는데, 땅주인 신영이가
"너는 과수원 내에 사과나무를 K x K 의 크기의 정사각형 모양으로만 수확해 가져갈 수 있어,
이때 K는 1보다 크거나 같고 N보다 작거나 같은 정수라구!
나머지는 내가 먹을께! 하하!" 라고 통보했다.

하나의 사과나무를 수확할 때, 사과를 통해 얻을 수 있는 이익과
노동비로 빠져나가는 손해가 동시에 이루어진다.

그래서 형곤이는 나무의 위치를 좌표로 하여,
사과를 통해 얻은 이익과 노동비를 더한 총이익을 2차원 배열의 형태로 정리했다.

악독한 땅주인 신영이로부터 고통받는 귀여운 형곤이에게
최대 총이익을 안겨주고 싶은 당신, 형곤이를 도와주자!

입력
첫 번째 줄에는 과수원의 크기 N이 주어진다. (1 ≤ N ≤ 300)
두 번째 줄부터 N + 1번째 줄까지, 해당 나무를 수확했을 때 얻을 수 있는 총이익을 표시한다.
총이익은 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫 번째 줄에 최댓값을 출력한다.

--------
8:47~

dp를 사용할 수 있을 것 같은데 잘 안됨.
알고리즘 종류를 보니 dp가 없고, bf 와 asum 뿐이다.
그냥 단순 무식하게 다 계산하자!

빠른 해법은 없는 듯?

'''

import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    return N,A


def solve_0(N:int, A:list[list[int]])->int:
    '''
    첫번째 구현
    Args:
    Returns:
    '''
    INF = int(1e8) # 1000 * (300*300) + 1 # ~== 90_000_000

    # 누적합 (accumulated sum)
    asum = [ [0]*(N+1) for _ in range(N+1) ]
    # asum 에 대해서만큼은 좌상단 좌표를 (1,1)로 간주하는 것이 편하다.
    # 즉, asum[y][x] 는 (1,1) 부터 (y,x) 까지의 partial sum
    for y in range(1, N+1):
        asum_x = [0]*(N+1)
        for x in range(1, N+1):
            asum_x[x] = asum_x[x-1] + A[y-1][x-1]
            asum[y][x] = asum[y-1][x] + asum_x[x]

    # 이후부터는 모두 zero-based index.
    def partial_sum2(k:int,y2:int,x2:int)->int:
        # 한변의 길이 k, 우하단 좌표 (y2,x2)
        y1,x1 = y2-k+1,x2-k+1
        return asum[y2+1][x2+1] - asum[y1][x2+1] - asum[y2+1][x1] + asum[y1][x1]

    maxval = -INF

    # K은 내부 정사각형 영역의 한변의 길이
    for k in range(2, N+1): # k: 2 ~ N
        # (y, x)는 정사각 영역의 우하단 좌표
        for y in range(k-1, N): # y: k-1 ~ N-1
            for x in range(k-1, N):
                # maxval = max(partial_sum2(k, y, x), maxval)
                v = partial_sum2(k, y, x)
                if maxval < v: maxval = v

    # 크기 1짜리 고려
    maxval = max(maxval, max(max(al) for al in A))
    return maxval


def solve(N:int, A:list[list[int]])->int:
    '''
    최적화 버전
    함수 호출 대신 inlining. 반복되는 +1 연산을 쓰지 않도록 좌표 기준 변경.

    Args:
    Returns:
    '''

    INF = int(1e8) # 1000 * (300*300) + 1 # ~== 90_000_000

    # 누적합 (accumulated sum)
    asum = [ [0]*(N+1) for _ in range(N+1) ]
    # asum 에 대해서만큼은 좌상단 좌표를 (1,1)로 간주하는 것이 편하다.
    # 즉, asum[y][x] 는 (1,1) 부터 (y,x) 까지의 partial sum
    for y in range(1, N+1):
        asum_x = [0]*(N+1)
        for x in range(1, N+1):
            asum_x[x] = asum_x[x-1] + A[y-1][x-1]
            asum[y][x] = asum[y-1][x] + asum_x[x]

    maxval = -INF

    # K은 내부 정사각형 영역의 한변의 길이
    for k in range(2, N+1): # k: 2 ~ N
        # (y2, x2)는 정사각 영역의 우하단 좌표 + 1
        for y2 in range(k, N+1): # y: k ~ N
            for x2 in range(k, N+1):
                y1,x1 = y2-k,x2-k
                v = asum[y2][x2] - asum[y1][x2] - asum[y2][x1] + asum[y1][x1]
                if maxval < v: maxval = v

    # 크기 1짜리 고려
    maxval = max(maxval, max(max(al) for al in A))
    return maxval


if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
4
-1 -2 -3 -4
5 6 7 8
9 10 11 12
-13 -14 -15 -16
예제 출력 1
45
예제 입력 2
3
-1 -1 -1
-1 -1 -1
-1 -1 -1
예제 출력 2
-1

----
pr=20002
run=(python3 a$pr.py)

echo '4\n-1 -2 -3 -4\n5 6 7 8\n9 10 11 12\n-13 -14 -15 -16' | $run
# 45
echo '3\n-1 -1 -1\n-1 -1 -1\n-1 -1 -1' | $run
# -1

echo  '1\n3' | $run


'''


import time,os
from random import seed,randint,shuffle

def gen_worstcase_input():
    # seed(time.time())
    seed(43)
    N = int(os.getenv('_N', '10'))
    A = [ [ randint(-10,10) for x in range(N) ] for y in range(N) ]
    return N,A

def test():
    N,A = gen_worstcase_input()
    print(N)
    print('\n'.join( ' '.join(map(str, ln)) for ln in A ))

'''
# worst case simulation
_N=300 python3 -c "from a$pr import test; test()" | time $run

# 1.35s user 0.01s system 97% cpu 1.394 total
# 0.86s user 0.01s system 96% cpu 0.903 total  # 개선 후

'''
