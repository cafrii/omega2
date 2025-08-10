'''
https://www.acmicpc.net/source/95101756

95101756 ksh990409 16562 맞았습니다!! 33432KB 48ms Python 3 679B


'''

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
parent = [i for i in range(n+1)]
visited = [0] * (n + 1)
pay = list(map(int, input().split()))
pay.insert(0, 0)

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if pay[a] < pay[b]:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)


sum = 0
for i in range(1, n+1):
    a = find(i)
    if visited[a] == 1:
        continue

    sum += pay[a]
    visited[a] = 1

    if k < sum:
        print('Oh no')
        exit()

print(sum)
