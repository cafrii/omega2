'''
1915번

가장 큰 정사각형 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	49837	15505	11258	30.196%

문제
n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.

0	1	0	0
0	1	1	1
1	1	1	0
0	0	1	0

위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다.

입력
첫째 줄에 n, m(1 ≤ n, m ≤ 1,000)이 주어진다. 다음 n개의 줄에는 m개의 숫자로 배열이 주어진다.

출력
첫째 줄에 가장 큰 정사각형의 넓이를 출력한다.

'''

import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve(arr:list[str]):
    N,M = len(arr),len(arr[0])
    dp = [ [ 0 for x in range(M+1) ] for y in range(N+1) ]
    # dp[y][x] 는 (y,x) 위치를 우하단으로 하는 최대 정사각형의 한변의 길이
    max_area = 0
    for y in range(1, N+1):
        for x in range(1, M+1):
            if arr[y-1][x-1] == '1':
                dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1
            max_area = max(max_area, dp[y][x]**2)
        # log('[%d] %s, max %d', y, dp[y], max_area)
    return max_area



N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input().strip())
    assert len(arr[-1]) == M

print(solve(arr))


'''
예제 입력 1
4 4
0100
0111
1110
0010

echo '4 4\n0100\n0111\n1110\n0010' | python3 1915.py
-> 4


4 4
0001
0111
0111
1111
-> 9

4 5
01110
11111
01111
10001
-> 9

1 1
0
-> 0

1 1
1
-> 1


'''
