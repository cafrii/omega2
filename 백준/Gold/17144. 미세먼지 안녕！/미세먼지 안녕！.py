
import sys
input = sys.stdin.readline

# def log(fmt, *args): print(fmt % args, file=sys.stderr)

def mapstr(A:list[list[int]], indent='', fmt='%2d ')->str:
    lines = []
    for line in A:
        lines.append(indent + ''.join(
            [ (fmt % e) for e in line ]
        ))
    return '\n'.join(lines)

def solve(A:list[list[int]], aircon:list[int], T:int):
    '''
    '''
    R,C = len(A),len(A[0])

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    aircon_loc = [(aircon[0],0),(aircon[1],0)]

    def diffuse():
        # this function will replace object A
        nonlocal A
        B = [[0]*C for r in range(R)]

        # for all dust in A..
        for r in range(R):
            for c in range(C):
                dust = A[r][c]
                if dust==0: continue # empty
                if dust<0: continue # aircon
                part = dust // 5
                if part == 0:
                    B[r][c] += dust # no diffuse
                    continue
                for dr,dc in neighbors: # delta r/c
                    nr,nc = r+dr,c+dc   # next r/c
                    if not (0<=nr<R and 0<=nc<C): # exceed bound
                        continue
                    if (nr,nc) in aircon_loc: # aircon
                        continue
                    B[nr][nc] += part
                    dust -= part
                B[r][c] += dust
        A = B  # keep B as A
        pass

    def circulate():
        # aircon 위치를 기준으로 두 개의 flow 적용.
        # 1. top flow
        ac = aircon[0]
        # 1-1. downward
        for r in range(ac-2, -1, -1):  # AC-2 ~ 0
            A[r+1][0] = A[r][0]
        # 1-2. left
        for c in range(1, C):  # 1 ~ C-1
            A[0][c-1] = A[0][c]
        # 1-3. upward
        for r in range(1, ac+1): # 1 ~ AC
            A[r-1][C-1] = A[r][C-1]
        # 1-4. right
        for c in range(C-2, 0, -1): # C-2 ~ 1
            A[ac][c+1] = A[ac][c]
        A[ac][1] = 0

        # 2. bottom flow
        ac = aircon[1]
        # 2-1. upward
        for r in range(ac+2, R): # AC+2 ~ R-1
            A[r-1][0] = A[r][0]
        # 2-2. left
        for c in range(1, C):  # 1 ~ C-1
            A[R-1][c-1] = A[R-1][c]
        # 2-3. downward
        for r in range(R-2, ac-1, -1): # R-2 ~ AC
            A[r+1][C-1] = A[r][C-1]
        # 2-4. right
        for c in range(C-2, 0, -1): # C-2 ~ 1
            A[ac][c+1] = A[ac][c]
        A[ac][1] = 0
        pass

    for t in range(1,T+1):
        # log("******** t: %d", t)
        diffuse()
        # log(" after diffuse\n%s", mapstr(A, '  '))
        circulate()
        # log(" after circulate\n%s", mapstr(A, '  '))

    return sum([ sum(k) for k in A ])


R,C,T = map(int, input().split())

aircon = [-1,-1] # row index of air conditioner, [top,bottom]
A = []
for i in range(R):
    A.append(list(map(int, input().split())))
    assert len(A[-1]) == C
    if A[-1][0] == -1:
        if aircon[0]<0: aircon[0] = i
        else: aircon[1] = i

assert aircon[0]>=2 and aircon[1]>=2
# log("input\n%s", mapstr(A, '  '))

print(solve(A,aircon,T))
