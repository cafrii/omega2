
import sys
input = sys.stdin.readline


def solve_bs(A:list[int], N:int)->int:
    '''
    Args:
        A: array of length of cables
        N: number of cables needed
    Returns:
        max length of cable
    '''
    A.sort(reverse=True)

    def allowed_len(clen:int)->bool:
        return sum( k//clen for k in A ) >= N

    cl_mx,cl_mn = A[0],1

    if allowed_len(cl_mx):
        return cl_mx
    # assert allowed_len(cl_mn)

    while cl_mx > cl_mn:
        # cl_mn 길이로는 항상 성공 (allowed)
        # cl_mx 길이로는 항상 실패 (not allowed)
        cl_mid = (cl_mx + cl_mn)//2
        if allowed_len(cl_mid):
            cl_mn = cl_mid
        else:
            cl_mx = cl_mid
        if cl_mx == cl_mn+1:
            return cl_mn
    return cl_mn


K,N = map(int, input().split())
A = []
for _ in range(K):
    A.append(int(input().strip()))
print(solve_bs(A, N))

