from collections import deque

def solve(A,B)->int:
    que = deque()
    que.append((A,1))

    while que:
        n,cnt = que.popleft()
        for n2 in [ n*10+1, 2*n ]:
            if n2 == B:
                return cnt+1
            if n2 > B:
                continue
            que.append((n2, cnt+1))

    return -1


A,B = map(int, input().split())
print(solve(A,B))
