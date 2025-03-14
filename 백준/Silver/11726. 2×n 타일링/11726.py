'''
11726
https://www.acmicpc.net/problem/11726

2xn 타일링

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	199969	77802	57794	36.865%

문제
2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2x5 크기의 직사각형을 채운 한 가지 방법의 예이다.


입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

'''


MOD = 10_007

def solve(N:int):
    '''
    맨 오른쪽 끝의 형태에 따라 구분
        case 1. 가로 타일 두 개로 끝나는 경우
            ...HH
            ...HH
        case 2. 세로 타일로 끝나는 경우
            ....V
            ....V

    A[k]는 가로 길이 k인 타일 배치 경우의 수 이며,
        두 가지 case 각각의 경우를 따로 계산 관리함.

        A[k] 는 length 2의 리스트.
        - A[k][0] 은 case 1의 경우의 수
        - A[k][1] 은 case 2의 경우의 수
    '''

    A = [ [0,0] for _ in range(N+1) ]

    A[1][0] = 0
    A[1][1] = 1

    if N == 1:
        return 1

    A[2][0] = 1
    A[2][1] = 1

    for k in range(3, N+1):
        # 가로 배치로 끝내기
        A[k][0] = A[k-2][0] + A[k-2][1]
            # 가로 배치는 다음 한가지 경우 밖에 없음.
            #  ...HH
            #  ...HH
            # 즉, sum(A[k-2]) 와 같음.

        # 세로 배치로 끝내기
        A[k][1] = A[k-1][0] + A[k-1][1]
            # 세로 배치도 한가지 밖에 없다?
            #  ....V
            #  ....V
            # 즉 sum(A[k-1])

    return sum(A[N]) % MOD


def solve2(N:int):
    # 첫 구현과 다르게, 아예 H case, V case 를 합쳐서 기록하자.
    # 또한, 매 기록 마다 mod 연산 적용.
    A = [ 0 for _ in range(N+1) ]

    A[1] = 1  # V
    if N == 1:
        return 1

    A[2] = 2  # HH, VV

    for k in range(3, N+1):
        A[k] = (A[k-2] + A[k-1]) % MOD

    return A[N]


N = int(input().strip()) # N:1~1000
print(solve2(N))

'''
예제 입력 1
2
예제 출력 1
2

예제 입력 2
9
예제 출력 2
55

echo '1000' | time python3 a.py

'''
