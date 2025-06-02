import sys
input = sys.stdin.readline

MAX_MN = 40_000

def solve(M,N,x,y):
    max_mn = M*N
    # x,y 가 1 부터 시작하는 값이면 나머지 연산이 불편하므로 1씩 줄여서 생각.
    # z는 y를 찾기 위한 running variable.
    z,k = (x-1)%N,x
    while k <= max_mn:
        if z == y-1:
            return k
        z,k = (z+M)%N, k+M
    return -1

T = int(input().strip())
ans = []
for _ in range(T):
    M,N,x,y = map(int, input().split())
    ans.append(solve(M,N,x,y))
print('\n'.join(map(str, ans)))
