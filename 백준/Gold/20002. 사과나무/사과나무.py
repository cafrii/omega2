import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    return N,A

def solve(N:int, A:list[list[int]])->int:
    '''
    최적화
    함수 호출 대신 inlining. 반복되는 +1 연산을 쓰지 않도록 좌표 기준 변경.
    Args:
    Returns:
    '''
    INF = int(1e8) # 1000 * (300*300) + 1 # ~== 90_000_000

    # 누적합 (accumulated sum)
    asum = [ [0]*(N+1) for _ in range(N+1) ]
    # asum 에 대해서만큼은 좌상단 좌표를 (1,1)로 간주하는 것이 편하다.
    # 즉, asum[y][x] 는 (1,1) 부터 (y,x) 까지의 partial sum
    for y in range(1, N+1):
        asum_x = [0]*(N+1)
        for x in range(1, N+1):
            asum_x[x] = asum_x[x-1] + A[y-1][x-1]
            asum[y][x] = asum[y-1][x] + asum_x[x]

    maxval = -INF
    # K은 내부 정사각형 영역의 한변의 길이
    for k in range(2, N+1): # k: 2 ~ N
        # (y2, x2)는 정사각 영역의 우하단 좌표 + 1
        for y2 in range(k, N+1): # y: k ~ N
            for x2 in range(k, N+1):
                y1,x1 = y2-k,x2-k
                v = asum[y2][x2] - asum[y1][x2] - asum[y2][x1] + asum[y1][x1]
                if maxval < v: maxval = v
    # 크기 1짜리 고려
    maxval = max(maxval, max(max(al) for al in A))
    return maxval

if __name__ == '__main__':
    print(solve(*get_input()))
