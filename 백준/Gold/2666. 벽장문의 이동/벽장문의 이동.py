
import sys
from heapq import heappush,heappop

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip()) # number of door, 4~20
    #assert 3<N<=20, "wrong N"
    a,b = map(int, input().split()) # door id which is initially open
    #assert 1<=a<=N and 1<=b<=N, "wrong a,b"
    M = int(input().rstrip())
    #assert 0<=M<=20, "wrong M"
    K = []
    for _ in range(M):
        K.append(int(input().rstrip()))
        #assert 1<=K[-1]<=N, "wrong K"
    return N,a,b,K


def solve_bfs(N:int, a:int,b:int, K:list[int])->int:
    '''
    변형된 bfs. 우선순위 큐 사용
    Returns:
        minumum move count
    '''

    que = [ (0,0,a,b) ]
    # element: ( move_count, step, open_door_1, open_door_2 )
    cnt = 0

    while que:
        cnt,step,a,b = heappop(que)
        a,b = min(a,b),max(a,b)

        if step >= len(K):
            break

        k = K[step] # target of this step

        if k == a or k == b:
            heappush(que, (cnt, step+1, a, b))
        elif k < a: #  k  a  b
            heappush(que, (cnt+(a-k), step+1, k, b))
        elif b < k: # a b k
            heappush(que, (cnt+(k-b), step+1, a, k))
        else: #if a < k < b:
            # 지금 어느 쪽 문을 사용하는 것이 더 유리한지는 알 수 없음. 두 가지 경우를 다 계산.
            heappush(que, (cnt+(k-a), step+1, k, b))
            heappush(que, (cnt+(b-k), step+1, a, k))

    return cnt


if __name__ == '__main__':
    print(solve_bfs(*get_input()))
