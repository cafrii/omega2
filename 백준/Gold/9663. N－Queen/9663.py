'''
9663번

N-Queen 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
10 초	128 MB	138554	67375	43244	46.943%

문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.


------

10:19~20
11:40~
~12:13 코딩

하지만 timeout 이 발생하게 되고, 개선 방향을 찾지 못하여 잠시 중단.
c++ 로 동일 로직 구현 후 pass
'채점 현황'에서 같은 cpp 코드가 배 이상 빠른 경우를 발견하고, 알고리즘 개선 방향을 잡음.

'''

import sys
input = sys.stdin.readline


def solve_timeout(N)->int:
    #
    ans = 0
    A = [-1] * N

    # N 개의 row 로 구성된 board A 에 N 개의 queen 을 배치해야 하므로
    # 최소한 row 1개에 하나의 queen 을 배치해야 한다.
    def allowed(row, col) -> bool:
        # board 의 (row,col) 위치에 새 queen 을 배치하기 전, 허용 가능 여부 검사
        for r in range(row-1, -1, -1):
            # off = row - r  # 1,2,3,4..
            if A[r] == col or abs(A[r]-col) == row - r:
                return False
        return True

    def backtrack(index):
        # A[index] 번째의 row 에서 queen 의 위치 결정
        nonlocal ans
        if index >= N:
            ans += 1
            return

        for k in range(N):
            # A[index][k] 에 queen 배치가 가능한지 체크하고, 가능하다면 후속 호출.
            if not allowed(index, k):
                continue
            A[index] = k
            backtrack(index+1)

    backtrack(0) # 0번 row 부터 배치.
    return ans



def solve(N)->int:
    ans = 0
    # A = [-1] * N

    blocked_col = [0] * N
    blocked_slash = [0] * (2*N-1)
    blocked_bslash = [0] * (2*N-1)

    '''
    N=5 인 경우의 예시
    blocked_col[k]
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
        k=  0 1 2 3 4

    (r,c) -> blocked_col[c]
    range: [0, N-1]

    blocked_slash[k]
             0 1 2 3 4 5 6 7 8
            / / / / / . . . .
          0 / / / / / . . .
          1 / / / / / . .
          2 / / / / / .
          3 / / / / /
           4 5 6 7 8

    (r,c) -> blocked_slash[r+c]
    range: [0, 2*N-2]

    blocked_bslash[k]
     0 1 2 3 4 5 6 7 8
      . . . . \ \ \ \ \  #
        . . . \ \ \ \ \ .
          . . \ \ \ \ \ . .
            . \ \ \ \ \ . . .
              \ \ \ \ \ . . . .
               0 1 2 3 4 5 6 7 8

    (r,c) -> blocked_bslash[c-r+(N-1)]
    range: [0, 2N-2]
    '''

    def set_blocked(r,c, val):
        blocked_col[c] = val
        blocked_slash[r+c] = val
        blocked_bslash[c-r+(N-1)] = val

    def is_blocked(r,c) -> bool:
        return (blocked_col[c] or
                blocked_slash[r+c] or
                blocked_bslash[c-r+(N-1)])

    def backtrack(index):
        nonlocal ans
        if index >= N:
            ans += 1
            return
        for k in range(N):
            if is_blocked(index, k):
                continue

            set_blocked(index, k, 1)
            backtrack(index+1)
            set_blocked(index, k, 0)

    backtrack(0) # 0번 row 부터 배치.
    return ans


N = int(input().strip())
print(solve(N))
# print(solve_timeout(N))


'''
echo '12' | time python3 9663.py
14200
python3 9663.py  3.13s user 0.02s system 99% cpu 3.150 total

'''
