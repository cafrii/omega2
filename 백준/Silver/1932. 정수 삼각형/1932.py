'''
1932번

정수 삼각형 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	108929	64643	48966	60.064%

문제

        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5

위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

----

9:58~10:12



'''

import sys
input = sys.stdin.readline


def solve(A:list[list]) -> int:
    N = len(A)
    # N: size of triagle (height or bottom size)

    dp = [ [0 for x in range(N+2)] for y in range(N+2) ]
    # dp[y][x]: 위에서부터의 레벨 y, 왼쪽에서부터 x 번째의 칸 까지의 경로 합.
    #           y: 1~N.  dp[0] 은 모두 0 으로 미사용.
    #           x: 1~y.  dp[y][0] 은 미사용.

    for k in range(1, N+1): # k: 1 ~ N
        for j in range(1, k+1): # j: 1 ~ k
            dp[k][j] = max(dp[k-1][j-1], dp[k-1][j]) + A[k-1][j-1]

    return max(dp[N])


N = int(input().strip())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
    assert len(A[-1]) == i+1

print(solve(A))


'''
예제 입력 1
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
예제 출력 1
30

echo '5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5' | python3 1932.py
-> 30

'''