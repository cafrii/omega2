'''
24392번
영재의 징검다리, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	512 MB	1468	573	435	37.500%

문제
푸앙이 게임에 참가한 영재는 유리 징검다리 게임을 통과해야 한다.

유리 징검다리 게임의 규칙은 간단하다.
총 N번의 걸음을 통해 건널 수 있고, 각 걸음마다 M개의 칸이 있다.
영재는 시작점(N - 1 번째 줄)의 한 칸에서 건너기 시작해 이후 앞의 인접한 최대 3개의 유리 중 하나를 선택해 건너갈 수 있다.
밟은 칸이 강화유리라면 안전하게 건널 수 있지만, 일반 유리는 밟을 수 없다.

다음은 N = 3, M = 5인 어느 순간에 영재가 가능한 이동을 나타낸 그림이다.
..
다리의 정보가 주어지면, 영재가 다리를 무사히 건널 수 있는 경우의 수를 알아내보자.

입력
첫 줄에 N과 M(1 ≤ N, M ≤ 1,000)이 공백으로 구분되어 주어지고, 그 뒤에는 N줄에 걸쳐 다리의 정보가 주어진다.
강화유리의 경우 1, 일반 유리의 경우 0으로 주어진다.

출력
영재가 무사히 다리를 건널 수 있는 경우의 수를 1,000,000,007로 나눈 나머지를 출력한다.

----

9:52~10:07

----
2차원 dp로 간단하게 구현.
따로 worst-case 검사하지 않음.
제출 후 검증 완료

'''


#def log(fmt, *args): print(fmt % args, file=sys.stderr)
log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)


def get_input():
    import sys
    input = sys.stdin.readline
    N,M = map(int, input().split()) # N행, M열
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
        assert len(A[-1]) == M
    return N,M,A


def solve(N:int, M:int, A:list[list[int]])->int:
    '''
    Args:
        A: N by M matrix with 0 or 1 element. 1 is safe.
    Returns:
        possible safe paths mode mod MOD
    '''
    MOD = 1_000_000_007

    # 아래에서 위, 또는 위에서 아래 상관 없음. 나는 위에서 아래로..
    # x축 (행)의 양 끝 계산의 편의를 위해 양쪽에 빈 공간을 둔다. 폭이 M+2 라고 가정.

    dp = [ [0]*(M+2) for _ in range(N) ]
    # 하나의 행 dp[y][..]는 [0]부터 [M+1]까지 총 M+2 의 폭을 가진다.
    # 이 중에서 양 끝 [0]과 [M+1]은 항상 0의 값을 가진다.

    # 첫번째 행은 강화유리 여부가 경로 수와 같음.
    # dp[0][:] = [0] + A[0] + [0]
    dp[0][1:M+1] = A[0]
    log("y:%d, dp %s", 0, dp[0])

    for y in range(1, N):  # y: 1 ~ N-1
        for x in range(1, M+1):  # x: 1 ~ M
            if A[y][x-1] == 0: continue # 강화 유리 아님
            dp[y][x] = (dp[y-1][x-1] + dp[y-1][x] + dp[y-1][x+1]) % MOD

        log("y:%d, dp %s", y, dp[y])

    return sum(dp[N-1]) % MOD


if __name__ == '__main__':
    print(solve(*get_input()))



'''
예제 입력 1
3 2
0 1
1 0
0 1
예제 출력 1
1
예제 입력 2
5 5
1 0 1 0 1
0 0 1 1 1
1 0 1 0 0
0 1 1 0 1
1 0 1 0 1
예제 출력 2
9
예제 입력 3
4 4
1 1 1 1
1 0 0 1
1 0 0 1
1 1 1 1
예제 출력 3
8

----
run=(python3 a24392.py)

echo '3 2\n0 1\n1 0\n0 1' | $run
# 1
echo '5 5\n1 0 1 0 1\n0 0 1 1 1\n1 0 1 0 0\n0 1 1 0 1\n1 0 1 0 1' | $run
# 9
echo '4 4\n1 1 1 1\n1 0 0 1\n1 0 0 1\n1 1 1 1' | $run
# 8

echo '1 1\n1' | $run
# 1
echo '1 1\n0' | $run
# 0

echo '1 5\n1 1 1 1 1' | $run
# 5
echo '2 5\n1 1 0 1 1\n1 1 0 1 1' | $run
# 8


'''
