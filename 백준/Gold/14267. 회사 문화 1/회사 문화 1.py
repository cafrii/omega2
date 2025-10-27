import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = list(map(int, input().split())) # 상사-부하 관련 정보
    #assert len(A) == N
    B = []
    for _ in range(M):
        n,w = map(int, input().split()) # 직원 n이 상사로부터 w만큼 칭찬을 받음.
        B.append((n, w))
    return N,M,A,B

def solve(N:int, M, A:list[int], B:list[tuple[int,int]])->list[int]:
    '''
        N: 직원 수
        A[k]: 직원 서열. A[k]는 직원 k+1 의 직속 상사의 번호
            A[0]: 직원 1(사장)의 상사는 없음. -1
            A[1]: 직원 2의 상사.
            A[2]: 직원 3의 상사.
            ...
        B: [(n, w), ...],  len(B)=M
            직원 n이 상사로부터 받은 칭찬이 w
    '''
    pr = [0] * (N+1)  # praise map, 칭찬 매핑 표
    for n,w in B:
        pr[n] += w
        # pr[k]: 직원 k가 받은 칭찬

    dp = [0] * (N+1)

    for j in range(2, N+1):  # j: 2 ~ N. 사장은 제외.
        jboss = A[j-1]  # 직원 j 의 상사
        dp[j] = dp[jboss] + pr[j]

    return dp[1:]

if __name__ == '__main__':
    a = solve(*get_input())
    print(' '.join(map(str, a)))

