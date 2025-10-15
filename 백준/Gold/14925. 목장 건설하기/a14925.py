'''
14925번
목장 건설하기 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	3519	1435	1108	39.899%

문제
랜드 씨는 퇴직금으로 땅을 사서 목장을 지으려 한다.
그가 사려고 소개받은 땅은 직사각형이고 대부분 들판이지만, 여기저기에 베기 어려운 나무와 치울 수 없는 바위가 있다.

그는 목장을 하나의 정사각형으로 최대한 크게 지으려 하는데, 그 안에 나무나 바위는 없어야 한다.

땅의 세로 길이가 M미터, 가로 길이가 N미터일 때, 1미터 간격의 격자로 된 땅의 지도를 M x N행렬로 표현하자.

이때, 행렬의 원소 0은 들판, 1은 나무 그리고 2는 돌을 의미한다.
랜드씨의 땅에서 지을 수 있는 가장 큰 정사각형 목장의 한 변의 크기 L을 출력하시오.

입력
M N  // M x N 행렬
1 <= M <= 1000
1 <= N <= 1000

출력
L

----

10.15, 8:05~

2차원 dp로 한번의 스캔으로 풀이 가능.

개선: dp 테이블에서 가장 큰 길이의 L을 찾기 위해, 마지막에 한번 더 검사하는 대신
dp 만드는 과정에서 추적하도록 함.

검증 완료.

'''


def get_input():
    import sys
    input = sys.stdin.readline
    M,N = map(int, input().split())
    A = []
    for _ in range(M):
        A.append(list(input().split()))
        assert len(A[-1]) == N
    return M,N,A

def solve(M:int, N:int, A:list[list[str]])->int:
    '''
    Args: A: ground map, MxN matrix
            M: 세로길이, num of rows
            N: 가로길이, num of columns
    '''

    dp = [ [0]*(N+1) for _ in range(M+1) ]
    max_l = 0
    for y in range(1, M+1):
        for x in range(1, N+1):
            if A[y-1][x-1] != '0': continue # 나무 또는 돌
            dp[y][x] = min(dp[y][x-1], dp[y-1][x], dp[y-1][x-1]) + 1
        max_l = max(max_l, max(dp[y]))

    return max_l


if __name__ == '__main__':
    print(solve(*get_input()))



'''
예제 입력 1
6 6
0 0 0 1 0 0
0 0 0 2 1 0
0 0 2 0 0 0
0 1 0 0 0 0
2 0 0 0 0 0
0 0 0 0 0 0
예제 출력 1
3

----
run=(python3 a14925.py)

echo '6 6\n0 0 0 1 0 0\n0 0 0 2 1 0\n0 0 2 0 0 0\n0 1 0 0 0 0\n2 0 0 0 0 0\n0 0 0 0 0 0' | $run
# 3


echo '1 1\n0' | $run
# 1
echo '1 1\n2' | $run
# 0

echo '1 4\n0 0 1 0' | $run
# 1
echo '2 2\n0 0\n0 0' | $run
# 2

# 주의: L 값이 우하단 끝에 걸리지 않은 경우.
echo '2 2\n0 0\n0 1' | $run
# 1



'''
