'''
15724번
주지수, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	4387	2124	1745	46.909%

문제
네모 왕국의 왕인 진경대왕은 왕국의 영토를 편하게 통치하기 위해서
1X1의 단위 구역을 여러 개 묶어서 하나의 거대 행정구역인 주지수(州地數, 마을의 땅을 셈)를 만들 예정이다.
진경대왕은 주지수를 만들기 위해서 일정한 직사각형 범위 내에 살고 있는 사람 수를 참고 자료로 쓰고 싶어한다.


진경대왕은 굉장히 근엄한 왕이기 때문에 당신에게 4개의 숫자로 직사각형 범위를 알려줄 것이다.

예를 들어, 위와 같이 사람이 살고 있다고 가정할 때
<그림 1>의 직사각형 범위의 사람 수를 알고 싶다면 진경대왕은 네 개의 정수 1 1 3 2를 부를 것이다.
마찬가지로 <그림 2>는 1 1 1 4, <그림 3>은 1 1 4 4가 될 것이다.

진경대왕을 위하여 이 참고 자료를 만들어내는 프로그램을 작성해보자.

입력
첫째 줄에 영토의 크기 N, M(1 ≤ N, M ≤ 1,024)이 주어진다.

다음 N개의 줄에는 M개의 정수로 단위 구역 내에 살고 있는 사람 수가 주어진다.
각 단위 구역 내에 살고 있는 사람 수는 100명 이하이며, 각 단위 구역 별 최소 1명의 사람은 살고 있다.

그 다음 줄에는 진경대왕이 인구 수를 궁금해하는 직사각형 범위의 개수 K(1 ≤ K ≤ 100,000)가 주어진다.

다음 K개의 줄에는 네 개의 정수로 직사각형 범위 x1, y1, x2, y2가 주어진다(x1 ≤ x2, y1 ≤ y2).

출력
K개의 줄에 순서대로 주어진 직사각형 범위 내에 살고 있는 사람 수의 합을 출력한다.

----

9/15, 11:21~11:42

부분합 문제.

'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
        assert len(A[-1]) == M
    K = int(input().rstrip())
    B = []
    for _ in range(K):
        B.append(list(map(int, input().split())))
        assert len(B[-1]) == 4
    return N,M,A,K,B

def solve(N:int, M:int, A:list[list[int]], K:int, B:list[list[int]])->list[int]:
    '''
    Args:
        N,M: 땅의 크기. N (row) x M (column)
        A: NxM 크기의 2차원 배열. 해당 구역에 거주하는 사람 수.
        K: 아래 B 요소 개수.
        B: 알고자 하는 영역의 좌상단, 우하단 좌표 (sy,sx), (ey,ex). 1-based 좌표.
    주의:
        A 배열의 index는 zero-based. B는 1-based.
        B 요소의 좌표는 우리 기준으로는 y1,x1,y2,x2 이다.
    Returns:
        K개의 영역 내의 거주 사람 수. 길이 K의 배열.
    알고리즘:
        누적 sum 을 이용하여 부분합 계산
    '''

    # 누적 sum 계산
    S = [ [0]*(M+1) for _ in range(N+1) ]
    # S[y][x] 는 A[0][0] 부터 A[y-1][x-1] 범위 내의 사람 수

    for y in range(1, N+1):
        sum1 = 0  # sum of line segment
        for x in range(1, M+1):
            sum1 += A[y-1][x-1]
            S[y][x] = S[y-1][x] + sum1

    # ans = []
    # for y1,x1,y2,x2 in B:
    #     a = S[y2][x2] - S[y1-1][x2] - S[y2][x1-1] + S[y1-1][x1-1]
    #     ans.append(a)
    # return ans

    return [
        S[y2][x2] - S[y1-1][x2] - S[y2][x1-1] + S[y1-1][x1-1]
        for y1,x1,y2,x2 in B
    ]

if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))



'''
예제 입력 1
4 4
9 14 29 7
1 31 6 13
21 26 40 16
8 38 11 23
3
1 1 3 2
1 1 1 4
1 1 4 4
예제 출력 1
102
59
293

----
run=(python3 a15724.py)

echo '4 4\n9 14 29 7\n1 31 6 13\n21 26 40 16\n8 38 11 23\n3\n1 1 3 2\n1 1 1 4\n1 1 4 4' | $run
# 102
# 59
# 293







'''

