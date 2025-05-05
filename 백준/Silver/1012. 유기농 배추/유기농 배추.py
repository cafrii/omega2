
import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve():
    T = int(input().strip())
    ans = [0]*T
    for t in range(T):
        M,N,K = map(int, input().split())
        # create N by M 2-d array
        A = [ [0 for x in range(M)] for y in range(N) ]
        for _ in range(K):
            x,y = map(int, input().split())
            A[y][x] = 1
        ans[t] = solve_tc(A)
    print(*ans, sep='\n')


def solve_tc(A:list[list]) -> int:
    '''
    Solve one test case.
    Args: A - 2d map
    Returns: number of segment
    '''
    N,M = len(A),len(A[0])

    idmap = [[0 for x in range(M)] for y in range(N)]
    # idmap[][] == 0 means that it is not visited yet.

    deltas = [(1,0), (-1,0), (0,1), (0,-1)]

    def mark(y0, x0, id):
        # starting from (y0, x0), mark area (1-segment) with id
        # id should be > 0
        stack = [ (y0, x0) ]
        idmap[y0][x0] = id
        extent = 1

        while stack:
            # log('    stack %s', stack)
            y,x = stack.pop()
            for dy,dx in deltas:
                ny,nx = y+dy,x+dx
                if not (0<=ny<N and 0<=nx<M): # out of map
                    continue
                if A[ny][nx] == 0: # cannot be area
                    continue
                if idmap[ny][nx] > 0: # already visited
                    continue

                stack.append((ny,nx))
                idmap[ny][nx] = id
                extent += 1

        return extent # just for debugging

    num_region = 0
    for y in range(N):
        for x in range(M):
            if A[y][x] == 1 and idmap[y][x] == 0:
                num_region += 1
                extent = mark(y, x, num_region)
                # log('(%d,%d) mark as id %d, area extent %d', y, x, num_region, extent)
    return num_region

solve()
