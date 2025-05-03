
import sys
input = sys.stdin.readline

N = int(input().strip())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# print(A)

def solve(orgy, orgx, sz) -> tuple[int,int]:
    '''
    Global: A: (NxN) 2-d array, with eiter 0 or 1
    Args:
       (orgy, orgx): left-top location of rect
       sz: size (length) of square rect
    Returns: (num_0_rects, num_1_rects)
    '''
    if sz < 1:
        return (0, 0)
    if sz == 1:
        return (1,0) if A[orgy][orgx] == 0 else (0,1)

    # print(f'**** sz: {sz}, ({orgy},{orgx})')
    # calculate sum of elements in this square.
    ssum = 0
    for y in range(orgy, orgy+sz):
        ssum += sum(A[y][orgx:orgx+sz])

    if ssum == 0:  # filled with all 0
        return (1,0)
    if ssum == sz*sz: # filled with all 1
        return (0,1)

    sz_half = sz // 2
    subans = [
        solve(orgy, orgx, sz_half),
        solve(orgy, orgx+sz_half, sz_half),
        solve(orgy+sz_half, orgx, sz_half),
        solve(orgy+sz_half, orgx+sz_half, sz_half)
    ]
    ans = tuple(map(sum, zip(*subans)))
    # print(f'{subans} -> {ans}')
    return ans

print(*solve(0, 0, N), sep='\n')
