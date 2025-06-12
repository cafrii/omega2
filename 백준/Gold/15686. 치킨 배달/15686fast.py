'''
다른 풀이
python3 기준으로 소요 시간이 훨씬 작음.

https://www.acmicpc.net/source/94553979

'''


from itertools import combinations

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
chikin = []
house = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chikin.append((i,j))
            continue
        if arr[i][j] == 1:
            house.append((i,j))
# print(chikin)
# print(house)
result = []
dp =[[0] * len(house) for _ in range(len(chikin))]
cur = 0
for i,j in chikin:
    k = 0
    for x,y in house:
        dp[cur][k] = abs(i-x)+abs(j-y)
        k += 1
    cur +=1
# for i in dp:
#     print(*i)
cur = 1e9
for i in combinations(dp,m):
    a = sum(map(min,zip(*i)))
    if  a < cur:
        cur = a
print(cur)


