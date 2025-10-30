import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
        #assert len(A[-1]) == N
    return N,A

def solve(N:int, A:list[list[int]])->int:
    '''
    Args: A: NxN 크기의 행렬.
    Returns: 가능한 모든 최단 경로의 LIS 값 중 최대 값
    '''
    dp = [ [0]*(N) for _ in range(N) ]
    # dp[y][x]는 (0,0)에서 (y,x)까지의 경로의 LIS 중에서
    # (y,x)에서 종료되는 것의 최장 길이

    dp[0][0] = 1

    for y in range(0, N):  # y: 1~N-1
        for x in range(0, N):  # x: 1~N-1
            if y==0 and x==0: continue

            # (0,0)에서 (y,x)까지 다시 순회하면서
            # A[y][x]보다 작은 최대 LIS 값을 검색하고
            # 거기에 A[y][x]를 덧붙여서 (+1 해서) LIS를 갱신한다.
            cur = A[y][x]

            dp[y][x] = max(
                (dp[y2][x2]
                for y2 in range(0, y+1)
                for x2 in range(0, x+1)
                if A[y2][x2] < cur),
                default=0
            ) + 1

    # dp[][] 전체 중에서 제일 큰 값 선택
    return max(max(j) for j in dp)

if __name__ == '__main__':
    print(solve(*get_input()))
