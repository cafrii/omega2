'''
이 문제를 이분 탐색으로 풀이한 것으로 보이는 답변?

https://www.acmicpc.net/source/93476950

제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
93476950	daseeni	 2805	맞았습니다!!	145580	532	Python 3	742	11일 전

결국 greedy search 이긴 한데, 좀 더 빠르게 search 를 하는 것일 뿐이다.

'''

import sys

input = sys.stdin.readline

num_of_tree, target = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))

tree_table = dict()
for tree in trees:
    if tree in tree_table:
        tree_table[tree] += 1
    else:
        tree_table[tree] = 1

# trees.sort()
# 조건 보기 길이 범위 [0,1,000,000,000]
start, end = 0, 1_000_000_000
answer = 0

while start <= end:
    mid = (start+end)//2
    total = 0
    for tree in tree_table.keys():
        if tree > mid:
            total += (tree - mid)*tree_table[tree]
    if total < target:
        end = mid - 1
    else:
        # 이분 탐색이 다 마쳤을 때 최적화된 값만 남음
        answer = mid
        start = mid + 1

print(answer)
