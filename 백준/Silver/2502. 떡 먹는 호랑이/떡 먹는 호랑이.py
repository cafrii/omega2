
import sys
input = sys.stdin.readline

D,K = map(int, input().split())
# D번째 날에 K개의 떡을 줬음. D는 1부터 시작.

def solve(D,K):
    # d-번째 날에 떡의 개수를 N[d] 라고 하자.
    # N[1] = A, N[2] = B 라고 가정
    # N[3] = N[1]+N[2] = A+B
    # N[4] = N[2]+N[3] = A+2B
    # ...
    # N[x] 를 aA+bB 라고 표현할 수 있고, 이 계수 목록을 C[d]로 표현.
    # 즉, C[d] = [a,b]

    C = [None]*(D+1) # coefficients
    C[1] = [1,0]  # A = 1A+0B
    C[2] = [0,1]  # B = 0A+1B
    for j in range(3,D+1):
        C[j] = [ C[j-2][0]+C[j-1][0], C[j-2][1]+C[j-1][1] ]

    # D번째 날의 A,B의 계수 ca,cb
    ca,cb = C[D]
    # ca*A + cb*B = K 를 만족하는 A,B를 찾아라.
    # 예: D=6, K=41 인 경우라면, 3A+5B=41, A=2, B=7

    # 여기서부터는 greedy로..
    ans = []
    for A in range(1,K+1):
        if A*ca >= K: break
        # ca*A + cb*B = K
        # cb*B = K - ca*A
        # B = (K - ca*A)/cb
        if (K - A*ca) % cb: continue
        B = (K - A*ca) // cb
        return (A,B)
    return (0,0) # 해가 없는 경우

print('\n'.join(map(str,solve(D,K))))
