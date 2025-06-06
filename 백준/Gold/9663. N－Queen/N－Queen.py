
import sys
input = sys.stdin.readline

def solve(N)->int:
    ans = 0

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
