
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

    return max(score[N-1])


T = int(input())

for _ in range(T):
    n = int(input()) # 1 ≤ n ≤ 100,000
    A = [ list(map(int, input().split())), list(map(int, input().split())) ]

    print(solve1(A))
