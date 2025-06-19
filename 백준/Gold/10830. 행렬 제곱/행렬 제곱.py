import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

MAX_B = 100_000_000_000
MOD = 1000

def mat_str(A:list[list[int]], indent:str='', format:str='%d')->str:
    # string representation of matrix A
    lines = []
    for r in A:
        lines.append(indent + ' '.join([(format % c) for c in r]))
    return '\n'.join(lines)

def mat_mul_mod(A:list[list[int]], B:list[list[int]]):
    '''
    matrix multiply with mod
    '''
    assert len(A[0]) == len(B)
    C = [ [ 0 for c in range(len(B[0])) ] for r in range(len(A)) ]

    for ra in range(len(A)): # row of A
        for cb in range(len(B[0])): # column of B
            sum = 0
            for k in range(len(A[0])):
                sum += (A[ra][k] * B[k][cb])
            C[ra][cb] = sum % MOD
    return C

def solve(A:list[list[int]], B:int):
    '''
        A is NxN matrix.
        return A^B (A**B)

        B를 2의 제곱수의 곱으로 분리해야 하는데, 이건 곧 2진수 표현으로 쉽게 얻을 수 있다.
        예: B=100 이면 0x64 = 0110 0110b
            = 2^1 + 2^2 + 2^5 + 2^6
        A^100
            = A^64 * A^32 * A^2 * A^1
        최대 A^2 부터 A^64 까지를 미리 구해 두고, 필요한 항만 따로 다시 곱하면 됨.
    '''
    N = len(A)
    I = [ [ (1 if c==r else 0) for c in range(N) ] for r in range(N) ]
    #log("identity:\n%s", mat_str(I, '  ', '%d'))

    binlist = [ int(k) for k in reversed(bin(B)[2:]) ]
    # B 의 2진 표현 문자열을 뒤집고 int 배열로 변환
    # 2진수 표현시 '0b' prefix가 붙으니 앞 두 글자 제거.
    #log("B: %d %s", B, binlist)

    # power of powers of A matrix
    pwrs:list = [None] * len(binlist)
        # pwrs[k] is A^(2^k))
        # pwrs[0] = A^1 = A
        # pwrs[1] = A^2 = pwrs[0]^2
        # pwrs[2] = A^4 = (A^2)^2 = pwrs[1]^2
        # pwrs[3] = A^8 = (A^4)^2 = pwrs[2]^2
        # ...
    for k in range(len(binlist)):
        if k == 0:
            pwrs[0] = A
        else:
            pwrs[k] = mat_mul_mod(pwrs[k-1], pwrs[k-1])
        #log("pwrs[%d]:\n%s", k, mat_str(pwrs[k], '    ', '%4d'))

    # starting with identity matrix (of size N)..
    result = I
    for k,val in enumerate(binlist):
        # val 는 뒤집힌 2진수 표현에서 각 자리(k)의 숫자.
        if val:
            result = mat_mul_mod(result, pwrs[k])
        #log("step[%d]: %d\n%s", k, val, result)

    #log("result:\n%s", mat_str(result, '  ', '%4d'))
    return result


N,B = map(int, input().split())
assert B >= 1
A = [] # [0]*N for i in range(N) ]
for _ in range(N):
    A.append(list(map(int, input().split())))
    assert len(A[-1]) == N

ans = solve(A,B)
for r in ans:
    print(' '.join([ str(a) for a in r ]))
