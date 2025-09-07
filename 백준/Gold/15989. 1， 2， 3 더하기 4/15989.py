'''
15989번
1, 2, 3 더하기 4 성공  골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	14898	9514	7591	64.048%

문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다.
합을 나타낼 때는 수를 1개 이상 사용해야 한다. 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.

1+1+1+1
2+1+1 (1+1+2, 1+2+1)
2+2
1+3 (3+1)

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.
n은 양수이며 10,000보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

------
2:31~2:55

1. set 로 구현 -> 시간 초과 예상
2. 그 다음 dictionary로 hashing 완화 -> 여전히 시간 초과 예상
-> 15989_slow.py

각 k 단계에서 3을 포함하는 경우와 아닌 경우로 나누어 계산 하니 풀림.
채점 확인.

'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    Ns = []
    for _ in range(C):
        Ns.append(int(input().rstrip()))
    return Ns,

def solve(Ns:list[int])->list[str]:
    '''
    Args: Ns: list of N to compose
    Returns: list of answer string
    '''

    max_n = max(Ns)
    alloc_n = max(max_n, 4)

    '''
    slow 버전 코드에서 추출한 로그. n=10 일 때, 각 조합의 경우.
    총 14 가지 인데, 일정한 패턴이 발견됨.
    이 패턴의 특징을 이용하여 빠른 계산 가능.

    [1, 0, 3],

    [4, 0, 2],
    [2, 1, 2],
    [0, 2, 2],

    [7, 0, 1],
    [5, 1, 1],
    [3, 2, 1],
    [1, 3, 1],

    [10, 0, 0],
    [8, 1, 0],
    [6, 2, 0],
    [4, 3, 0],
    [2, 4, 0],
    [0, 5, 0],

    dp[k][0] # 1 과 2 만을 이용하여 k 를 만드는 방법의 수
    dp[k][1] # 1, 2, 3 을 이용하여 k 를 만드는 방법의 수
    '''

    dp = [ [0,0] for k in range(alloc_n+1) ]

    dp[0][0] = dp[0][1] = 1
    # 0을 만드는 경우의 수: 1

    for k in range(1, max_n+1):
        # 1.
        # dp[k][0]: 1 과 2 만을 이용하여 k 를 만드는 방법의 수:
        # 2로 일부분을 채우고, 나머지는 1로 채울 수 있음.
        #   2를 k//2, k//2-1, ..., 0 개 사용까지.
        # 총 경우의 수: (k//2) + 1
        # ...
        dp[k][0] = k//2 + 1

        # 2.
        # dp[k][1]: 1,2,3 을 이용하여 k를 만드는 방법의 수
        # 3을 사용하는 경우는 k//3, k//3-1, k//3-2, .., 0 가지가 존재함.
        # for j in range(k//3, -1, -1):
        #     # 3을 j개 사용할 때, 각각의 경우서 1,2로 나머지를 채우는 경우의 수를 합산
        #     dp[k][1] += dp[k - j*3][0]
        # => 위 코드로 해도 worst case 1초 정도로 풀리긴 함.
        #  그런데 제출하면 시간 초과 뜬다. TC 개수가 있기 때문일듯.

        # 더 빠른 방법. dp[][1] 의 결과 까지도 재활용한다.
        dp[k][1] = dp[k][0] + dp[k-3][1]

        # log("[%d]: %s", k, dp[k])

    ans = []
    for n in Ns:
        ans.append(str(dp[n][1]))
    return ans


if __name__ == '__main__':
    ans = solve(*get_input())
    print('\n'.join(ans))


'''
예제 입력 1
3
4
7
10
예제 출력 1
4
8
14
----

run=(python3 15989.py)

echo '3\n4\n7\n10' | $run
# 4 8 14

echo '1\n3' | $run
# 3

echo '1\n10' | $run
# 14

echo '1\n100' | $run
# 884

echo '1\n300' | time $run
# 7651
# -- solve1
# $run  1.33s user 0.13s system 53% cpu 2.709 total
# -- solve2
# $run  1.06s user 0.03s system 98% cpu 1.111 total

echo '1\n500' | time $run
# 21084

echo '1\n700' | time $run
# 41184

echo '1\n10000' | time $run
# 8338334
# $run  1.08s user 0.01s system 99% cpu 1.095 total


'''


