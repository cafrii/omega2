
import sys
input = sys.stdin.readline


def solve(A):
    ''' calculate partial sum matrix
        which is the sum of (0,0)~(y,x) elements for each (y,x).
        return the partial matrix.
    '''
    H,W = len(A),len(A[0])
    psum = [[0 for x in range(W)] for y in range(H)]
    # for y == 0
    psum[0][0] = A[0][0]
    for x in range(1,W):
        psum[0][x] = psum[0][x-1] + A[0][x]

    for y in range(1,H):
        psum[y][0] = psum[y-1][0] + A[y][0]
        for x in range(1,W):
            psum[y][x] = psum[y-1][x] + (psum[y][x-1] - psum[y-1][x-1]) + A[y][x]

    return psum


N,M = map(int, input().split())

# A[0][] and A[][0] is zero-filled.
A = [ [0]*(N+1) ]
for y in range(N):
    A.append([0] + list(map(int, input().split())))


psum = solve(A)

for m in range(M):
    # y가 행, x가 열로 naming.
    y1,x1,y2,x2 = map(int, input().split())
    answer = psum[y2][x2] - psum[y1-1][x2] - psum[y2][x1-1]+ psum[y1-1][x1-1]
    print(answer)
