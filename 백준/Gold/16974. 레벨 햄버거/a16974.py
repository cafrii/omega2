'''
16974번
레벨 햄버거 성공, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	512 MB	3287	1608	1274	51.873%

문제
상근날드에서 오랜만에 새로운 햄버거를 출시했다. 바로 레벨-L 버거이다. 레벨-L 버거는 다음과 같이 만든다.

레벨-0 버거는 패티만으로 이루어져 있다.
레벨-L 버거는 햄버거번, 레벨-(L-1) 버거, 패티, 레벨-(L-1)버거, 햄버거번으로 이루어져 있다. (L ≥ 1)

예를 들어, 레벨-1 버거는 'BPPPB', 레벨-2 버거는 'BBPPPBPBPPPBB'와 같이 생겼다. (B는 햄버거번, P는 패티)

상도가 상근날드에 방문해서 레벨-N 버거를 시켰다.
상도가 햄버거의 아래 X장을 먹었을 때, 먹은 패티는 몇 장일까? 한 장은 햄버거번 또는 패티 한 장이다.

입력
첫째 줄에 N과 X가 주어진다.

출력
첫째 줄에 상도가 먹은 패티의 수를 출력한다.

제한
1 ≤ N ≤ 50
1 ≤ X ≤ 레벨-N 버거에 있는 레이어의 수

----
10/13, 6:09~6:30

dp 로 저장해야 할 것들..

- 이 레벨의 버거 크기 = 직전 레벨 버거 크기 x 2 + 3
- 이 레벨 버거에 포함된 패티 개수

일단 1 ~ N 레벨까지의 위 정보를 dp table 에 채운 후
X 층에 포함된 패티 수는 재귀적으로 호출

검증 완료

'''

# log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
#     if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    import sys
    input = sys.stdin.readline
    N,X = map(int, input().split())
    return N,X

def solve(N:int, X:int)->int:
    '''
    Args: N: level
    Returns: number of patties of lower X layers of level-N burger
    '''
    # 최대 recursive depth 는 50을 넘지 않음.

    dp = [ [0,0] for _ in range(N+1) ]
    # dp[k][0]: size of this level burger
    # dp[k][1]: number of patties of this level burger

    dp[0] = [1, 1] # P
    dp[1] = [5, 3] # BPPPB
    # dp[2] = [13, 7]

    for k in range(2, N+1):
        dp[k][0] = dp[k-1][0]*2 + 3
        dp[k][1] = dp[k-1][1]*2 + 1

    def count_patty(n:int, x:int)->int:
        # 레벨 n 버거의 아래 x 장에 포함된 패티 수를 리턴
        if n <= 1:
            if n < 0: return 0
            if n == 0: return 1 if x >= 1 else 0
            # n == 1
            return 0 if x<=1 else x-1 if x<=4 else 3

        # 먼저 레벨 n 버거의 구성 파악
        prev_sz = dp[n-1][0]
        #  B (n-1 burger, prev_sz) P (prev_sz) B
        if x <= 1+prev_sz:
            return count_patty(n-1, x-1)
        if x < 1+prev_sz+1+prev_sz:
            return count_patty(n-1, x-1-prev_sz-1) + dp[n-1][1] + 1
        else:
            return dp[n][1]

    return count_patty(N, X)


if __name__ == '__main__':
    print(solve(*get_input()))



'''
예제 입력 1
2 7
예제 출력 1
4
예제 입력 2
1 1
예제 출력 2
0
예제 입력 3
50 4321098765432109
예제 출력 3
2160549382716056

----
run=(python3 a16974.py)

echo '2 7' | $run
# 4
echo '1 1' | $run
# 0
echo '50 4321098765432109' | $run
# 2160549382716056

echo '2 8' | $run
# 4   # 사실 8은 유효한 입력은 아님.
echo '2 0' | $run
# 0


'''

