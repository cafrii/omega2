
import sys

def get_input():
    input = sys.stdin.readline
    A = []
    for i in range(1000):
        n = int(input().rstrip())
        if n == 0: break
        A.append(n)
    return A,

def solve(N:int)->int:
    '''
    Logic:
        N개의 W와 N개의 H를 나열하는 방법의 수에서, 출력된 H개수가 W개수를 넘을 수 없는 조건이 있음.
        총 2N개의 자리를 채우는 경우
        맨 앞은 항상 W. -> 2N-1개를 채우는 경우의 수가 됨. W N-1개, H N개

        dp[w][h] =  # h >= w
            dp[w-1][h] if w == h else
            dp[w-1][h] + dp[w][h-1]
    '''

    dp = [ [0]*(N+1) for _ in range(N+1) ]
    # dp[w][h]는 병 안에 W 와 H 가 각각 w, h 개가 있을 때 꺼내는 방법의 수

    # H만 병 안에 있으면 경우의 수는 1가지 뿐.
    for h in range(1, N+1):
        dp[0][h] = 1

    for w in range(1, N+1):
        for h in range(w, N+1):

            dp[w][h] = ( # h >= w
                dp[w-1][h] if w == h else
                dp[w-1][h] + dp[w][h-1]
            )

    return dp[N][N]

if __name__ == '__main__':
    A, = get_input()
    for n in A:
        print(solve(n))
