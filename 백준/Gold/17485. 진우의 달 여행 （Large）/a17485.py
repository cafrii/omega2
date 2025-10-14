'''
17485번
진우의 달 여행 (Large), 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	3792	1952	1512	51.657%

문제
우주비행이 꿈이였던 진우는 음식점 '매일매일싱싱'에서 열심히 일한 결과 달 여행에 필요한 자금을 모두 마련하였다!
지구와 우주사이는 N X M 행렬로 나타낼 수 있으며 각 원소의 값은 우주선이 그 공간을 지날 때 소모되는 연료의 양이다.

[예시]

진우는 여행경비를 아끼기 위해 조금 특이한 우주선을 선택하였다. 진우가 선택한 우주선의 특징은 아래와 같다.

1. 지구 -> 달로 가는 경우 우주선이 움직일 수 있는 방향은 아래와 같다.
..
2. 우주선은 전에 움직인 방향으로 움직일 수 없다. 즉, 같은 방향으로 두번 연속으로 움직일 수 없다.

진우의 목표는 연료를 최대한 아끼며 지구의 어느위치에서든 출발하여 달의 어느위치든 착륙하는 것이다.

최대한 돈을 아끼고 살아서 달에 도착하고 싶은 진우를 위해 달에 도달하기 위해 필요한 연료의 최소값을 계산해 주자.

입력
첫줄에 지구와 달 사이 공간을 나타내는 행렬의 크기를 나타내는 N, M (2 ≤ N, M ≤ 1000)이 주어진다.

다음 N줄 동안 각 행렬의 원소 값이 주어진다. 각 행렬의 원소값은 100 이하의 자연수이다.

출력
달 여행에 필요한 최소 연료의 값을 출력한다.

----

7:36~7:58

직전 이동 방향에 따라 계산이 달라지므로 dp state 에 직전 이동 방향까지 포함시키도록 한다.
즉, 3차원 dp table 이어야 함.
그 외엔 특이 사항 없음.

제출 후 검증 완료.

'''

import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    import sys
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
        A: fuel loss matrix, NxM
    Returns:
        minimum fuel loss consumed
    '''

    INF = 1000*1000*100 + 1

    dp = [ [ [INF]*3 for m in range(M+2) ] for n in range(N) ]
    # dp[n][m][dir]
    # dir 은 마지막 우주선의 움직임. 0:/↙️ 1:|⬇️ 2:\\↘️
    # m 은 좌우 1칸 씩 여백을 두었음. if 검사가 귀찮으니..

    # dp[0] 초기화
    for m in range(1, M+1):
        dp[0][m][:] = [ A[0][m-1] ]*3 # 처음엔 방향 제약 없으니 모두 동일하게.

    for n in range(1, N):  # n: 1 ~ N-1

        for m in range(1, M+1):
            c = A[n][m-1] # fuel loss in current loc.
            dp[n][m][0] = c + min(dp[n-1][m+1][1], dp[n-1][m+1][2])
            dp[n][m][1] = c + min(dp[n-1][m  ][0], dp[n-1][m  ][2])
            dp[n][m][2] = c + min(dp[n-1][m-1][0], dp[n-1][m-1][1])

    return min( min(dp[N-1][m]) for m in range(1,M+1) )



if __name__ == '__main__':
    #inp = get_input()
    #print(solve(*inp))
    #r = solve(*inp)
    #r = solve(*get_input())
    #print(r)
    print(solve(*get_input()))


'''
예제 입력 1
6 4
5 8 5 1
3 5 8 4
9 77 65 5
2 1 5 2
5 98 1 5
4 95 67 58
예제 출력 1
29

----
run=(python3 a17485.py)

echo '6 4\n5 8 5 1\n3 5 8 4\n9 77 65 5\n2 1 5 2\n5 98 1 5\n4 95 67 58' | $run
# 29


'''
