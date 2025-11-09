'''
4095번
최대 정사각형 성공다국어, 골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
5 초	256 MB	2562	1115	821	42.760%

문제
1과 0으로 이루어진 NxM크기의 행렬이 주어졌을 때,
1로만 이루어진 가장 큰 정사각형 부분 행렬 찾는 프로그램을 작성하시오.

입력
입력은 여러 테스트 케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 N과 M이 주어진다. (1 ≤ N,M ≤ 1,000)
다음 N개의 줄에는 공백으로 구분된 M개의 수가 주어진다.
마지막 줄에는 0이 두 개가 주어진다.

출력
각 테스트 케이스에 대해서 가장 큰 정사각형의 너비 또는 높이를 출력한다.
만약 그런 정사각형이 없을 때는 0을 출력한다.


----
5:58~


대부분 10초가 넘는데, 4초 대 이면 선방한 것임.
제출 답안 중 2초 대가 있음.
https://www.acmicpc.net/source/90185638

1. 나는 dp2d 를 사용했으나, 결국 dp[y] 방향으로는 직전 것만 사용하므로
1차원 dp를 두 벌 관리하는 방식으로 했음.
이게 이 정도로 시간 차이를 만들어 내는가?

2. 제일 안쪽 루프에서 매번 max 값을 찾지 않고, row를 하나 끝낸 후 max를 찾게 했음.
이건 좀 이해가 간다.

수정 후 3초대 개선. 그런데 2초 대 까지는 아님.. 그냥 이 정도에서 끝냄.

'''



import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    def gen():
        while True:
            N,M = map(int, input().split())
            if N==0: return
            # A = [ list(map(int, input().split())) for _ in range(N) ]
            A = [ input().rstrip() for _ in range(N) ]
            yield N,M,A
    return gen()

# def solve(N:int, M:int, A:list[list[int]])->str:
def solve(N:int, M:int, A:list[str])->str:
    '''
    Args:
    Returns:
    '''
    dp = [ [0]*(M+1) for _ in range(N+1) ]
    # dp[y][x] 는 (y,x)를 우하단 모서리로 하는 정사각형 중 가장 큰 것의 한변의 길이
    #  y,x 좌표는 1-base.

    max_w = 0
    for y in range(1, N+1):
        for x in range(1, M+1):
            # "1 2 3" -> 숫자가 있는 인덱스는 0 2 4
            if A[y-1][(x-1)*2] == '0':
                continue
            dp[y][x] = min(dp[y-1][x], dp[y-1][x-1], dp[y][x-1]) + 1
            if dp[y][x] > max_w:
                max_w = dp[y][x]

    return str(max_w)


def solve_fast(N:int, M:int, A:list[str])->str:
    '''
    Args:
    Returns:

    2d dp 대신 두벌의 1-d dp로 풀이
    '''
    dp,dp_old = [0]*(M+1),[0]*(M+1)
    max_w = 0
    for y in range(1, N+1):
        for x in range(1, M+1):
            if A[y-1][(x-1)*2] == '0':
                continue
            dp[x] = min(dp_old[x], dp_old[x-1], dp[x-1]) + 1

        max_w = max(max(dp), max_w)
        dp,dp_old = [0]*(M+1),dp

    return str(max_w)


if __name__ == '__main__':
    print('\n'.join(
        [ solve_fast(N,M,A) for N,M,A in get_input() ]
    ))



'''
예제 입력 1
4 5
0 1 0 1 1
1 1 1 1 1
0 1 1 1 0
1 1 1 1 1
3 4
1 1 1 1
1 1 1 1
1 1 1 1
6 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0
예제 출력 1
3
3
0

----
pr=4095
run=(python3 a$pr.py)

echo '4 5\n0 1 0 1 1\n1 1 1 1 1\n0 1 1 1 0\n1 1 1 1 1\n3 4\n1 1 1 1\n1 1 1 1\n1 1 1 1\n6 6\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0' | $run
# 3
# 3
# 0

echo '1 1\n1\n2 2\n0 1\n1 1\n0 0' | $run
# 1
# 1


'''
