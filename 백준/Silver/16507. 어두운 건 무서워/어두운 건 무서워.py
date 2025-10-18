import sys

def get_input():
    input = sys.stdin.readline
    R,C,Q = map(int, input().split())
    A = []
    for _ in range(R):
        A.append(list(map(int, input().split())))
        #assert len(A[-1]) == C
    B = []
    for _ in range(Q):
        B.append(list(map(int, input().split())))
        #assert len(B[-1]) == 4
    return A,B

def solve(A:list[list[int]], B:list[list[int]])->list[int]:
    '''
    Args:
    Returns:
    '''
    R,C = len(A),len(A[0])

    # partial sum
    psum = [ [0]*(C+1) for _ in range(R+1) ]

    for r in range(1,R+1):
        rsum = 0
        for c in range(1,C+1):
            rsum += A[r-1][c-1]
            psum[r][c] = psum[r-1][c] + rsum

    ans = []
    for r1,c1,r2,c2 in B:
        tsum = psum[r2][c2] - psum[r1-1][c2] - psum[r2][c1-1] + psum[r1-1][c1-1]
        area = (r2-r1+1)*(c2-c1+1)
        ans.append(tsum // area)

    return ans

if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))
