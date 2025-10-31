'''
5549번
행성 탐사, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	3126	1560	1256	52.225%

문제
상근이는 우주선을 타고 인간이 거주할 수 있는 행성을 찾고 있다.
마침내, 전 세계 최초로 인간이 거주할 수 있는 행성을 찾았다.
이 행성은 정글, 바다, 얼음이 뒤얽힌 행성이다.
상근이는 이 행성에서 거주 할 수 있는 구역의 지도를 만들어 지구로 보냈다.

상근이가 보내온 지도는 가로 Ncm, 세로 Mcm 직사각형 모양이다.
지도는 1cm 크기의 정사각형으로 나누어져 있고, 각 구역의 지형이 알파벳으로 표시되어 있다.
지형은 정글, 바다, 얼음 중 하나이며, 정글은 J, 바다는 O, 얼음은 I로 표시되어 있다.

지구에 있는 정인이는 조사 대상 영역을 K개 만들었다.
이때, 각 영역에 정글, 바다, 얼음이 각각 몇 개씩 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 지도의 크기 M과 N이 주어진다. (1 ≤ M, N ≤ 1000)
둘째 줄에 정인이가 만든 조사 대상 영역의 개수 K가 주어진다. (1 ≤ K ≤ 100000)
셋째 줄부터 M개 줄에는 상근이가 보낸 지도의 내용이 주어진다.
다음 K개 줄에는 조사 대상 영역의 정보가 주어진다.
정보는 네 정수 a b c d로 이루어져 있다.
구역은 직사각형 모양 이며, 왼쪽 위 모서리의 좌표가 (a, b) 오른쪽 아래 모서리의 좌표가 (c, d)이다.

출력
각 조사 대상 영역에 포함되어 있는 정글, 바다, 얼음의 수를 공백으로 구분해 한 줄에 한 정보씩 출력한다.

----

5:19~40

2차원 prefix sum을 세 종류를 구비하게 구현.

'''



import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    M,N = map(int, input().split()) # M(row),N(col)
    K = int(input().rstrip())
    A = []
    for _ in range(M):
        A.append(input().rstrip())
        assert len(A[-1]) == N
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


'''
예제 입력 1
4 7
4
JIOJOIJ
IOJOIJO
JOIJOOI
OOJJIJO
3 5 4 7
2 2 3 6
2 2 2 2
1 1 4 7
예제 출력 1
1 3 2
3 5 2
0 1 0
10 11 7

---
pr=5549
run=(python3 a$pr.py)

echo '4 7\n4\nJIOJOIJ\nIOJOIJO\nJOIJOOI\nOOJJIJO\n3 5 4 7\n2 2 3 6\n2 2 2 2\n1 1 4 7' | $run

# 1 3 2
# 3 5 2
# 0 1 0
# 10 11 7

echo '1 1\n2\nJ\n1 1 1 1\n1 1 1 1' | $run
# 1 0 0
# 1 0 0

echo '2 2\n2\nJO\nIJ\n1 1 2 1\n1 2 2 2' | $run
# 1 0 1
# 1 1 0


'''
