

def solve(A:list[list]):
    '''
    우 하단 부분 채워 나감.
    채워가는 순서:
        3x3 이라면 다음 순서로.
            8  7  6
            5  4  3
            2  1  0
    '''
    N = len(A)
    C = [ [0 for x in range(N)] for y in range(N) ]

    C[N-1][N-1] = 1

    for y in range(N-1, -1, -1):
        for x in range(N-1, -1, -1):
            if A[y][x] == 0: # cannot move
                continue
            dist = A[y][x]

            count = 0
            # 아래방향 점프
            if y+dist < N:
                count += C[y+dist][x]
            # 오른쪽 방향 점프
            if x+dist < N:
                count += C[y][x+dist]

            C[y][x] = count

    return C[0][0]


N = int(input().strip())
A = []
for _ in range(N):
    A.append(list(map(int, input().strip().split())))

print(solve(A))
