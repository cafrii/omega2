import sys

def get_input():
    input = sys.stdin.readline
    M,N = map(int, input().split()) # M(row),N(col)
    K = int(input().rstrip())
    A = []
    for _ in range(M):
        A.append(input().rstrip())
        #assert len(A[-1]) == N
    Ks = []
    for _ in range(K):
        r1,c1,r2,c2 = map(int, input().split())
        Ks.append([r1-1, c1-1, r2, c2])
        # 미리 1뺀 값으로 추가함
    return A,Ks

def solve(A:list[str], Ks:list[list[int]])->list[str]:
    '''
    Args:
    Returns:
    '''
    M,N,K = len(A),len(A[0]),len(Ks)

    asumj = [ [0]*(N+1) for _ in range(M+1) ]  # accumulated sum of jungle
    asumo = [ [0]*(N+1) for _ in range(M+1) ]  # .. for ocean
    asumi = [ [0]*(N+1) for _ in range(M+1) ]  # .. for ice
    # axum?[y][x]는 (1,1) 부터 (y,x) 까지의 범위에 있는 해당 셀(j,i,o)의 개수.

    # calculate prefix sum
    for y in range(1, M+1): # y: 1 ~ M
        for x in range(1, N+1):
            asumj[y][x] = asumj[y-1][x] + asumj[y][x-1] - asumj[y-1][x-1] + (1 if A[y-1][x-1]=='J' else 0)
            asumo[y][x] = asumo[y-1][x] + asumo[y][x-1] - asumo[y-1][x-1] + (1 if A[y-1][x-1]=='O' else 0)
            asumi[y][x] = asumi[y-1][x] + asumi[y][x-1] - asumi[y-1][x-1] + (1 if A[y-1][x-1]=='I' else 0)
            # asumi[y][x] = (y-1)*(x-1) - asumj[y][x] - asumo[y][x]

    ans = []
    for y1,x1,y2,x2 in Ks:
        nj = asumj[y2][x2] - asumj[y1][x2] - asumj[y2][x1] + asumj[y1][x1]
        no = asumo[y2][x2] - asumo[y1][x2] - asumo[y2][x1] + asumo[y1][x1]
        ni = asumi[y2][x2] - asumi[y1][x2] - asumi[y2][x1] + asumi[y1][x1]
        ans.append(f'{nj} {no} {ni}')

    return ans

if __name__ == '__main__':
    print('\n'.join(solve(*get_input())))
