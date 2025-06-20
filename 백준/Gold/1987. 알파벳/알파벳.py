import sys
input = sys.stdin.readline

from collections import deque
'''
    랜덤 보드를 생성하여 돌려보면, loop 반복 개수가 대략 6~7천 회에 이른다.
    이 중 상당 부분은 early exit 가 가능할 수 있을 것도 같은데..
    특정 위치에 다른 경로로 방문을 한 경우,
      A B C
        C D
    A 에서 D 위치로 가는 길이 두 개 존재. 그런데 사실상 경로는 100% 동일.
    이러한 경우를 제거하는 것이 이번 수정의 의도.

    que 에 mask를 저장하지 않고, 각 (y,x) 칸에 저장해 보도록 한다.
    메모리가 허용할 수 있을지 모르겠는데.. 일단 시도.
    -> que 에도 같이 저장. 별로 메모리 크지 않으니..
'''
def solve(board:list[str])->int:
    #
    R,C = len(board),len(board[0])
    maskmap = [ [{} for c in range(C)] for r in range(R) ]
    # initially empty dict
    que = deque()
    # element: (r,c,pathmask,pathlen)

    def gen_mask(s:str)->int:
        return 1 << (ord(s)-ord('A'))

    mask = gen_mask(board[0][0])
    que.append((0, 0, mask, 1))
    maskmap[0][0][mask] = 1
    maxpathlen = 1
    deltas = [(1,0),(0,1),(-1,0),(0,-1)]

    while que:
        y,x,hmask,pathlen = que.popleft()
        for dy,dx in deltas:
            ny,nx = y+dy,x+dx
            # check boundness
            if not (0<=ny<R and 0<=nx<C):
                continue
            # check if we already passed the alphabet.
            mask = gen_mask(board[ny][nx])
            if mask & hmask:
                continue
            newmask = hmask | mask
            # check mask history of this cell
            if newmask in maskmap[ny][nx]:
                continue
            que.append((ny, nx, newmask, pathlen+1))
            maskmap[ny][nx][newmask] = 1
            maxpathlen = max(maxpathlen, pathlen+1)
        #
    return maxpathlen

R,C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input().strip())
    assert len(board[-1]) == C
print(solve(board))
