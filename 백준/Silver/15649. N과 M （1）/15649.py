'''
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

import sys
def log(fmt, *arg):
    print(fmt % arg, file=sys.stderr)

# greedy
def solve(N, M):
    # construct length M array [1, 2, 3, .., M]
    A = [i for i in range(1, M+1)]

    def incr(L) -> bool:
        # 길이 L 의 숫자 배열 A (즉, A[0:L]) 를 하나 증가.
        # 더 이상 증가를 못하면 False 리턴
        if L <= 0:
            return False
        if A[0] > N:
            log("finish: %s", A[:L])
            return False

        # 맨 끝 자리 하나 증가
        A[L-1] = A[L-1] + 1
        # 허용 가능 수: 1~N
        if A[L-1] > N: # 마지막 자리가 넘침. carry 처리.
            log("carry up.. %s", A[:L])
            if not incr(L-1):
                return False
            A[L-1] = 1
            # 1 또한 중복 체크 해야 하니 계속 진행

        if A[L-1] in A[:L-1]: # 중복 체크
            log("redundant: %s", A[:L])
            return incr(L)
        else:
            log("increased: %s", A[:L])
            return True # ok

    while True:
        print(*A)
        if incr(M) == False:
            break



N,M = map(int, input().split())
solve(N, M)



'''
echo '3 1' | python3 15649.py
echo '4 2' | python3 15649.py



'''
