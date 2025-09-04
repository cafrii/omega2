'''

출처 불명

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
open1, open2 = map(int, input().split())
m = int(input())
targets = [int(input()) for _ in range(m)]


dp = [[[ -1 for _ in range(n+1)] for _ in range(n+1)] for _ in range(m+1)]

def dfs(i, o1, o2):
    if i == m:
        return 0
    if dp[i][o1][o2] != -1:
        return dp[i][o1][o2]

    target = targets[i]

    move1 = abs(o1 - target) + dfs(i + 1, target, o2)
    move2 = abs(o2 - target) + dfs(i + 1, o1, target)

    dp[i][o1][o2] = min(move1, move2)
    return dp[i][o1][o2]

print(dfs(0, open1, open2))

