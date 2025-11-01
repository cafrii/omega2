'''
27210번
신을 모시는 사당, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	2132	958	723	44.274%

문제
신을 모시는 사당에는 신을 조각한 돌상 N개가 일렬로 놓여 있다.
각 돌상은 왼쪽 또는 오른쪽을 바라보고 서있다.
창영이는 연속한 몇 개의 돌상에 금칠을 하여 궁극의 깨달음을 얻고자 한다.

궁극의 깨달음을 얻기 위해서는 가능한 한 많은 금색 돌상들이 같은 방향을 바라보아야 한다.
방향이 다른 돌상은 깨달음에 치명적이다.
깨달음의 양은 아래와 같이 정의된다.

| (왼쪽을 바라보는 금색 돌상의 개수) - (오른쪽을 바라보는 금색 돌상의 개수) |

창영이는 궁극의 깨달음을 얻을 수 있을까?

입력
첫째 줄에 돌상의 개수 N이 주어진다.
둘째 줄에 돌상이 나열된 순서대로, 각 돌상이 바라보고 있는 방향이 주어진다.
입력의 편의상 왼쪽은 1, 오른쪽은 2라고 하자.

출력
최대한 많은 깨달음을 얻기 위해 금을 칠하였을 때, 얻을 수 있는 깨달음의 양을 출력한다.

제한
1 ≤ N ≤ 100,000

--------

9:41~

dp로 풀때 dp[] 에 저장할 값을 뭐로 할 것인지.
단순히 깨달음양 만으로는 안되고 1우세인지 2우세인지도 저장해야..

문제를 두개 푼다고 봐야 함.

'''



import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    assert len(A) == N
    return N,A

def solve(N:int, A:list[int])->int:
    '''
    Args:
    Returns:
    '''

    # INF = 100_001

    # dp = [ [-INF,-INF] for _ in range(N) ]
    dp = [ [0,0] for _ in range(N) ]
    # dp[k][0] 는 A[k]를 끝자리로 하는 부분수열 중 1의 초과 개수 (1개수-2개수)
    # dp[k][1] 는 ... 2의 초과 개수 (2 개수 - 1 개수)

    dp[0][0] = (1 if A[0]==1 else 0)
    dp[0][1] = (1 if A[0]==2 else 0)

    maxval = abs(dp[0][0] - dp[0][1])

    for k in range(1, N):
        # 끝자리가 1로 끝나는 것. 다시 1이 오면 하나 증가됨.
        dp[k][0] = ((dp[k-1][0] + 1) if A[k]==1 else \
                    max(dp[k-1][0] - 1, 0))
        # 끝자리가 2로 끝나는 것.
        dp[k][1] = ((dp[k-1][1] + 1) if A[k]==2 else \
                    max(dp[k-1][1] - 1, 0))
        maxval = max(maxval, abs(dp[k][0] - dp[k][1]))

    return maxval



def solve2(N:int, A:list[int])->int:
    '''
    https://www.acmicpc.net/source/96474283

    좀 더 빠른 해 인데... 얼른 읽히진 않음.

    '''
    # 2를 -1로 대체
    b = [0] + [ (-1 if a==2 else a) for a in A ]

    for i in range(1, N+1):
        b[i] += b[i - 1]

    # 왜 이렇게만 해도 답이 되는지는 잘 모르겠음.
    return max(b) - min(b)


if __name__ == '__main__':
    print(solve(*get_input()))

    # print(solve2(*get_input()))



'''
예제 입력 1
5
1 1 2 1 2
예제 출력 1
2
예제 입력 2
1
1
예제 출력 2
1
예제 입력 3
2
1 2
예제 출력 3
1

----
pr=27210
run=(python3 a$pr.py)

echo '5\n1 1 2 1 2' | $run
# 2
echo '1\n1' | $run
# 1
echo '2\n1 2' | $run
# 1



echo '6\n2 2 1 1 2 2' | $run
# 2
echo '8\n2 2 2 1 1 2 2 2' | $run
# 4




'''
