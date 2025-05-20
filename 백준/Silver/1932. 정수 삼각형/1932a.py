
'''
별도의 dp array 를 쓰지 않고, 그냥 문제용 array 에 바로 sum 해 가는 방법.
메모리도 적게 쓰고, 좀 더 빠르게 수행 가능함.

https://www.acmicpc.net/source/94364588


'''

import sys
input = sys.stdin.readline

def solution():
  n = int(input())
  trees = [list(map(int, input().split())) for _ in range(n)]

  for i in range(n-2, -1, -1):
    for j in range(0, len(trees[i]), 1):
      trees[i][j] += max(trees[i+1][j], trees[i+1][j+1])

  return trees[0][0]

print(solution())
