'''


'''

import sys
input = sys.stdin.readline

N = int(input().strip())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# print(A)

def solve(oy, ox, sz) -> tuple[int,int]:
    '''
    Global: A: (NxN) 2-d array, with eiter 0 or 1
    Args:
       (oy, ox): origin. ie, left-top location of rect
       sz: size (length) of square rect
    Returns: (num_0_rects, num_1_rects)
    '''
    if sz < 1:
        return (0, 0)
    if sz == 1:
        return (1,0) if A[oy][ox] == 0 else (0,1)

    # print(f'**** sz: {sz}, ({oy},{ox})')
    # calculate sum of elements in this square.

    # 아래 코드는 초기에 작성했던 것인데, 모든 요소를 다 참조하고 계산하므로 비효율적이다.
    # ssum = 0
    # for y in range(oy, oy+sz):
    #     ssum += sum(A[y][ox:ox+sz])

    # if ssum == 0:  # filled with all 0
    #     return (1,0)
    # if ssum == sz*sz: # filled with all 1
    #     return (0,1)

    # 그냥 루프
    e1 = A[oy][ox] # first element
    if all(A[y][x] == e1 for y in range(oy, oy+sz) for x in range(ox, ox+sz)):
        return (1,0) if e1 == 0 else (0,1)

    sz_half = sz // 2
    subans = [
        solve(oy, ox, sz_half),
        solve(oy, ox+sz_half, sz_half),
        solve(oy+sz_half, ox, sz_half),
        solve(oy+sz_half, ox+sz_half, sz_half)
    ]
    ans = tuple(map(sum, zip(*subans)))
    # print(f'{subans} -> {ans}')
    return ans


print(*solve(0, 0, N), sep='\n')


'''
예제 입력 1
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

예제 출력 1
9
7


echo '1\n0' | python3 2630.py
-> 1 0

echo '1\n1' | python3 2630.py
-> 0 1

echo '2\n1 1\n1 1' | python3 2630.py
-> 0 1

echo '2\n1 1\n1 0' | python3 2630.py
-> 1 3

1 0 0 0
0 1 0 0
0 0 1 1
0 0 1 1

echo '4\n1 0 0 0\n0 1 0 0\n0 0 1 1\n0 0 1 1' | python3 2630.py
-> 4 3

'''
