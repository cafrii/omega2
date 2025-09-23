'''

https://www.acmicpc.net/source/97897762

2025/9/18
아직 완전히 코드를 이해하진 못했음.

'''


import sys

sys.setrecursionlimit(10**3)
arr = []
s = 0
N = int(input())
if N == 1 :
    print(1)
    sys.exit()
sets= set()
for i in range(1, 130) :
    tmp = ((i*(i+1))//2)
    s += tmp
    if N < s :
        idx = i -1
        break
    sets.add(s)
    arr.append(s)

def backtrack(total, curr, depth) :
    global answer
    if total == N :
        answer = min(answer, depth)

    if depth >= answer-1 :
        return

    for i in range(curr, idx) :
        if total + arr[i] > N :
            return
        backtrack(total + arr[i],i,  depth + 1)

visited = set()
answer = sys.maxsize
for ix in range(idx-1, -1, -1) :
    backtrack(arr[ix],ix, 1)
print(answer)

