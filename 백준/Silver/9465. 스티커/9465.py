
'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	83534	39760	28444	47.101%
문제
상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다.
스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다. 상냥이는 스티커를 이용해 책상을 꾸미려고 한다.

상냥이가 구매한 스티커의 품질은 매우 좋지 않다. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다.
즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.

 50  10 100  20  40
 30  50  70  10  60

모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다.
먼저, 그림 (b)와 같이 각 스티커에 점수를 매겼다. 상냥이가 뗄 수 있는 스티커의 점수의 최댓값을 구하는 프로그램을 작성하시오.
즉, 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.

위의 그림의 경우에 점수가 50, 50, 100, 60인 스티커를 고르면, 점수는 260이 되고 이 것이 최대 점수이다.
가장 높은 점수를 가지는 두 스티커 (100과 70)은 변을 공유하기 때문에, 동시에 뗄 수 없다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 n (1 ≤ n ≤ 100,000)이 주어진다.
다음 두 줄에는 n개의 정수가 주어지며, 각 정수는 그 위치에 해당하는 스티커의 점수이다.
연속하는 두 정수 사이에는 빈 칸이 하나 있다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.
'''


def solve1(A: list) -> int:
    # A[row][col]. row = 0 or 1, col = 0 ~ N-1

    N = len(A[0])

    # for column 'col', there 3 cases
    # case 0: neither A[0][col] nor A[1][col] used.
    # case 1: pick A[0][col].
    # case 2: pick A[1][col].
    # for each case, calculate the maximum score and save it to score[col][case]

    score = [[0] * 3 for _ in range(N)]
        # [ [0, 0, 0], [0, 0, 0], ... ]

    for col in range(N):
        if col == 0:
            score[col][0] = 0
            score[col][1] = A[0][0]
            score[col][2] = A[1][0]
            continue

        # for col > 0
        # case 0. no pick. only score[col-1][*] is considerred.
        score[col][0] = max(score[col-1][0], score[col-1][1], score[col-1][2])

        # case 1. pick A[0]. it is possible only when previous case is 0 or 2.
        score[col][1] = A[0][col] + max(score[col-1][0], score[col-1][2])

        # case 2. pick A[1]. it is possible only when previous case is 0 or 1.
        score[col][2] = A[1][col] + max(score[col-1][0], score[col-1][1])

    # print(score)
    # print(score[N-1])
    return max(score[N-1])


T = int(input())

for _ in range(T):
    n = int(input()) # 1 ≤ n ≤ 100,000
    A = [ list(map(int, input().split())), list(map(int, input().split())) ]

    print(solve1(A))







'''
1
5
50 10 100 20 40
30 50 70 10 60


예제 입력 1
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80

예제 출력 1
260
290
'''