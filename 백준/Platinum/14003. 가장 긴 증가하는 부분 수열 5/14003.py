'''
14003번
가장 긴 증가하는 부분 수열 5 성공스페셜 저지

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
3 초	512 MB	43677	15175	10739	34.253%

문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은
A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (-1,000,000,000 ≤ Ai ≤ 1,000,000,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 정답이 될 수 있는 가장 긴 증가하는 부분 수열을 출력한다.


----

10:16~

'''


import sys
input = sys.stdin.readline
write = sys.stdout.write

import bisect


MIN_A = -1_000_000_000
MIN = MIN_A - 1


def solve(A:list[int])->tuple[int,list]:
    '''
    '''
    N = len(A)

    D = [MIN] * N
    # D[i]: A[:i+1] 까지만 고려했을때, 끝자리 숫자가 A[i]인 LIS의 길이

    # L[k]: 길이가 k인 LIS의 맨 끝자리 숫자 중 최소값.
    L = [MIN] * (N+1)
    lsz = 1   # L의 실제로 유효한 요소의 개수

    # 첫번째 A[0]은 따로 고려해 준다.
    D[0] = 1

    L[lsz] = A[0]
    lsz += 1

    # 두번째 숫자부터는 루프.
    for i in range(1, N):
        #
        # L[:] 중에서 A[i]보다 작은 최대요소를 찾고, 그 LIS길이에 +1을 하면 됨.
        idx = bisect.bisect_left(L, A[i], lo=0, hi=lsz)

        # 발견한 자리의 인덱스 idx가 새 LIS 길이. (즉, +1까지 고려된 길이)
        D[i] = idx

        # L 업데이트.
        L[idx] = A[i] # 길이가 idx인 lis의 끝자리 숫자.
        # 기존에 L2[idx]에 있던 숫자는 A[i]보다 크거나 같음이 보장됨.
        # 즉, A[i]는 현재까지 L2[idx]에 올 수 있는 최소값.

        lsz = max(lsz, idx+1)
        # L2 의 실제로 데이터가 저장된 길이 추적

    # max(D)를 호출하는 것 보다 lsz 계산이 더 빠르다.
    # 현재 L 에는 L[0] 부터 L[lsz-1] 까지 lsz 개의 요소가 있음.
    # L의 인덱스가 LIS 길이 이므로, 최대 LIS 길이는 lsz-1 이다.
    max_d = lsz-1

    # create sample sequence of A[]
    B = [0] * max_d
    d = max_d
    for i in range(len(D)-1, -1, -1):
        if D[i] != d: continue
        B[d-1] = A[i]
        d -= 1
        if d == 0: break # early exit

    return max_d, B


N = int(input().strip())
A = list(map(int, input().split()))
assert len(A) == N
max_d,seq = solve(A)

write(f'{max_d}\n')
write(' '.join(map(str, seq)))
write('\n')



'''
예제 입력 1
6
10 20 10 30 20 50
예제 출력 1
4
10 20 30 50

run=(python3 14003.py)

echo '6\n10 20 10 30 20 50' | $run
->
4
10 20 30 50



A: 1 2 1 3 2 5
D: 1 2 1 3 2 4
L: - 1 2 3 5

A: 3 1 4 1 5 9 2 6 5
D: 1 1 2 1 3 4 2 4 3
L: - 1 2 5 6

echo '9\n3 1 4 1 5 9 2 6 5' | $run
->
4
1 4 5 6

'''
