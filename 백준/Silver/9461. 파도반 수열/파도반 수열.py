
import sys
input = sys.stdin.readline

def solve(Ns:list[int])->list[int]:
    max_n = max(max(Ns), 10)
    dp = [0]*(max_n+1)
    dp[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for n in range(6, max_n+1):
        dp[n] = dp[n-1] + dp[n-5]
    # print(dp)
    return [ dp[n] for n in Ns ]


T = int(input().strip())
Ns = []
for _ in range(T):
    Ns.append(int(input().strip()))
print('\n'.join(map(str, solve(Ns))))
