
import sys
input = sys.stdin.readline

#def log(fmt, *args):
#    print(fmt % args, file=sys.stderr)

MAX_LEN_N = 2000

# answer matrix
# A[j][k]: Ns[j:k+1] 이 팰린드롬이면 1
#
A = [ [0]*MAX_LEN_N for k in range(MAX_LEN_N) ]

def solve(N:list[int]):
    len_n = len(N)
    for k in range(len_n):
        A[k][k] = 1
        # k가 center 인 홀수 길이의 팰린드롬 모두 검사
        for j in range(1, min(k, len_n-1-k)+1):
            if N[k-j] != N[k+j]:
                break
            A[k-j][k+j] = 1
            # log('odd  (%d ~ %d), %s', k-j, k+j, N[k-j:k+j+1])
        # N[k:k+2] 부터 커져가는 짝수 길이의 팰린드롬 검사
        for j in range(0, len_n):
            if k-j < 0 or len_n <= k+1+j:
                break
            if N[k-j] != N[k+1+j]:
                break
            A[k-j][k+1+j] = 1
            # log('even (%d ~ %d), %s', k-j, k+1+j, N[k-j:k+1+j])
    return A

_ = int(input().strip())
Ns = list(map(int, input().split()))

ans = solve(Ns)

M = int(input().strip())
for _ in range(M):
    s,e = map(int, input().split())
    print(ans[s-1][e-1])
