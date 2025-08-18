import sys
from collections import deque

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N

def solve_bfs2(N:int):
    '''
    '''
    if N <= 1:
        return 0
    que = deque()
    visited = {}
    cnt = 0
    que.append((N, cnt))

    while que:
        num,cnt = que.popleft()
        if num == 1:
            break
        if num%3 == 0 and num//3 not in visited:
            que.append((num//3, cnt+1))
            visited[num//3] = cnt+1
        if num%2 == 0 and num//2 not in visited:
            que.append((num//2, cnt+1))
            visited[num//2] = cnt+1
        if num-1 not in visited:
            que.append((num-1, cnt+1))
            visited[num-1] = cnt+1
    return cnt

if __name__ == '__main__':
    print(solve_bfs2(get_input()))
