'''
10830번
행렬 제곱 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	48278	17571	13882	34.844%

문제
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오.
수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

입력
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

----

시간제한 생각하지 말고 일단 구현해 본다.
1:18~1:40.

분할 정복 방식으로 리팩토링
2:40~3:??

'''

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
    len_r,len_c,len_m = len(A),len(B[0]),len(B)

    C = [ [ 0 for c in range(len_c) ] for r in range(len_r) ]

    for ra in range(len_r): # row of A
        for cb in range(len_c): # column of B
            # sum = 0
            # for k in range(len(A[0])):
            #     sum += (A[ra][k] * B[k][cb])
            # C[ra][cb] = sum % MOD
            C[ra][cb] = sum( (A[ra][k] * B[k][cb]) for k in range(len_m)) % MOD
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
    log("identity:\n%s", mat_str(I, '  ', '%d'))

    binlist = [ int(k) for k in reversed(bin(B)[2:]) ]
    # B 의 2진 표현 문자열을 뒤집고 int 배열로 변환
    # 2진수 표현시 '0b' prefix가 붙으니 앞 두 글자 제거.
    log("B: %d %s", B, binlist)

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
        log("pwrs[%d]:\n%s", k, mat_str(pwrs[k], '    ', '%4d'))

    # starting with identity matrix (of size N)..
    result = I
    for k,val in enumerate(binlist):
        # val 는 뒤집힌 2진수 표현에서 각 자리(k)의 숫자.
        if val:
            result = mat_mul_mod(result, pwrs[k])
        log("step[%d]: %d\n%s", k, val, result)

    log("result:\n%s", mat_str(result, '  ', '%4d'))
    return result


def solve_slow(A:list[list[int]], B:int):
    # 구식 방법. 그냥 수학 이론 대로 계산.
    #
    N = len(A)
    assert len(A[0]) == N

    # copy of mat A
    res = [ r[:] for r in A ]

    for i in range(B-1):
        res = mat_mul_mod(res, A)

    return res


N,B = map(int, input().split())
assert B >= 1
A = [] # [0]*N for i in range(N) ]
for _ in range(N):
    A.append(list(map(int, input().split())))
    assert len(A[-1]) == N

ans = solve(A,B)
for r in ans:
    print(' '.join([ str(a) for a in r ]))



'''
예제 입력 1
2 5
1 2
3 4
예제 출력 1
69 558
337 406

run=(python3 10830.py)

echo '2 5\n1 2\n3 4' | $run


예제 입력 2
3 3
1 2 3
4 5 6
7 8 9

예제 출력 2
468 576 684
62 305 548
656 34 412


예제 입력 3
5 10
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1

예제 출력 3
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512


5 100000
1 2 3 4 5
6 7 8 9 1
2 3 4 5 6
7 8 9 1 2
3 4 5 6 7
-> 0.92s

5 1000000
1 2 3 4 5
6 7 8 9 1
2 3 4 5 6
7 8 9 1 2
3 4 5 6 7
-> 8.96 s

리팩토링 후

echo '5 1000000\n1 2 3 4 5\n6 7 8 9 1\n2 3 4 5 6\n7 8 9 1 2\n3 4 5 6 7' | time $run
->
922 264 606 608 705
302 9 716 608 342
249 616 983 200 937
984 56 128 137 904
576 968 360 792 169
$run  0.02s user 0.01s system 71% cpu 0.051 total


echo '5 100000000000\n1 2 3 4 5\n6 7 8 9 1\n2 3 4 5 6\n7 8 9 1 2\n3 4 5 6 7' | time $run
->
362 936 510 584 857
774 169 564 400 694
529 632 735 416 745
920 24 128 569 832
696 328 960 248 633
$run  0.02s user 0.01s system 67% cpu 0.053 total


'''


