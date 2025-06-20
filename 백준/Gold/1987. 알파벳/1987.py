'''
1987번
알파벳 성공다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	145355	45270	27368	28.648%

문제
세로 $R$칸, 가로 $C$칸으로 된 표 모양의 보드가 있다.
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 ($1$행 $1$열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데,
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오.
말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 $R$과 $C$가 빈칸을 사이에 두고 주어진다. ($1 ≤ R,C ≤ 20$)
둘째 줄부터 $R$개의 줄에 걸쳐서 보드에 적혀 있는 $C$개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

----

10:59~11:15 timeout 실패!
그 후 여러번의 시도.

'''


import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

from collections import deque


def solve_timeout(board:list[str])->int:
    R,C = len(board),len(board[0])
    que = deque()
    # element: (r,c,path)
    que.append((0,0,board[0][0]))
    maxpathlen = 1
    deltas = [(1,0),(0,1),(-1,0),(0,-1)]
    loopcnt = 0

    while que:
        loopcnt += 1
        y,x,history = que.popleft()
        # log("(%d) (%d,%d,%s) %d, que %d", loopcnt, y, x, history, maxpathlen, len(que))
        for dy,dx in deltas:
            ny,nx = y+dy,x+dx
            # check boundness
            if not (0<=ny<R and 0<=nx<C):
                continue
            # check if we already passed the alphabet.
            if board[ny][nx] in history:
                continue
            maxpathlen = max(maxpathlen, len(history)+1)
            que.append((ny,nx,history+board[ny][nx]))
        #
    return maxpathlen


def solve_memoverflow(board:list[str])->int:
    R,C = len(board),len(board[0])
    que = deque()
    # element: (r,c,set)
    que.append((0,0,set(board[0][0])))
    maxpathlen = 1
    deltas = [(1,0),(0,1),(-1,0),(0,-1)]
    # loopcnt = 0

    while que:
        # loopcnt += 1
        y,x,history = que.popleft()
        # log("(%d) (%d,%d,%s) %d, que %d", loopcnt, y, x, history, maxpathlen, len(que))
        for dy,dx in deltas:
            ny,nx = y+dy,x+dx
            # check boundness
            if not (0<=ny<R and 0<=nx<C):
                continue
            # check if we already passed the alphabet.
            if board[ny][nx] in history:
                continue
            maxpathlen = max(maxpathlen, len(history)+1)
            que.append((ny, nx, history | set(board[ny][nx])))
        #
    return maxpathlen



'''
    위의 set 을 사용한 경우 메모리 초과 발생.
    최대 알파벳이 26 밖에 안되니, 32비트 정수로 사용 여부를 표현 가능. bitmask 사용하는 것으로 변경.
    단, bitmask 의 1의 개수 세는 것이 번거로우니, que 에 pathlen 까지 저장하였음.

    결과: 여전히 timeout.
'''
def solve_timeout2(board:list[str])->int:
    R,C = len(board),len(board[0])
    que = deque()
    # element: (r,c,historymask,pathlen)

    def gen_mask(s:str)->int:
        return 1 << (ord(s)-ord('A'))
    def check_mask(s:str, mask:int)->bool:
        return (gen_mask(s) & mask) != 0

    que.append((0, 0, gen_mask(board[0][0]), 1))
    maxpathlen = 1
    deltas = [(1,0),(0,1),(-1,0),(0,-1)]
    loopcnt = 0

    while que:
        loopcnt += 1
        y,x,history,pathlen = que.popleft()
        log("(%d) (%d,%d,0x%x) pathlen %d, que %d", loopcnt, y, x, history, maxpathlen, len(que))
        for dy,dx in deltas:
            ny,nx = y+dy,x+dx
            # check boundness
            if not (0<=ny<R and 0<=nx<C):
                continue
            # check if we already passed the alphabet.
            if check_mask(board[ny][nx], history):
                continue
            maxpathlen = max(maxpathlen, pathlen+1)
            que.append((ny, nx, gen_mask(board[ny][nx]) | history, pathlen+1))
        #
    return maxpathlen



'''
    랜덤 보드를 생성하여 돌려보면, loop 반복 개수가 대략 6~7천 회에 이른다.
    이 중 상당 부분은 early exit 가 가능할 수 있을 것도 같은데..
    특정 위치에 다른 경로로 방문을 한 경우,
      A B C
        C D
    저 D 위치로 가는 길이 두 개 존재. 그런데 사실상 경로는 100% 동일.
    이러한 경우를 제거하는 것이 이번 수정의 의도.

    que 에 mask를 저장하지 않고, 각 (y,x) 칸에 저장해 보도록 한다.
    메모리가 허용할 수 있을지 모르겠는데 일단 시도.

'''
def solve(board:list[str])->int:
    R,C = len(board),len(board[0])
    maskmap = [ [{} for c in range(C)] for r in range(R) ]
    # initially empty dict

    que = deque()
    # element: (r,c,pathmask,pathlen)

    def gen_mask(s:str)->int:
        return 1 << (ord(s)-ord('A'))
    # def check_mask(s:str, mask:int)->bool:
    #     return (gen_mask(s) & mask) != 0

    ch = board[0][0]
    mask = gen_mask(ch)
    que.append((0, 0, mask, 1))
    maskmap[0][0][mask] = 1

    maxpathlen = 1
    deltas = [(1,0),(0,1),(-1,0),(0,-1)]
    loopcnt = 0

    while que:
        loopcnt += 1
        y,x,hmask,pathlen = que.popleft()
        # log("(%d) (%d,%d,0x%x) pathlen %d, que #%d %s", loopcnt, y, x, hmask, maxpathlen, len(que), que)
        log("(%d) (%d,%d,0x%x) pathlen %d, que #%d", loopcnt, y, x, hmask, maxpathlen, len(que))
        # log("   maskmap[%d][%d]: %s", y, x, maskmap[y][x])
        log("     maskmap[%d][%d]: #%d", y, x, len(maskmap[y][x].keys()))
        for dy,dx in deltas:
            ny,nx = y+dy,x+dx
            # check boundness
            if not (0<=ny<R and 0<=nx<C):
                continue
            ch = board[ny][nx]
            # check if we already passed the alphabet.
            mask = gen_mask(ch)
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



def solve_optimum(board:list[str])->int:
    '''
        문제는 pass 했으니 더 최적화.
        BFS, DSF 방식 무관하다. 결국 모든 경로를 다 계산하니.
        DFS 로 하고, 재귀까지 사용하면 stack 관리 안해도 된다.

        그리고 naming convention을 관례에 따라 maskmap을 visited 로 변경.
        역할은 앞과 동일.
    '''
    R,C = len(board),len(board[0])
    visited = [ [{} for c in range(C)] for r in range(R) ]
    # initially empty dict

    def gen_mask(s:str)->int:
        return 1 << (ord(s)-ord('A'))

    maxpathlen = 0
    deltas = [(1,0),(0,1),(-1,0),(0,-1)]

    def dfs(y, x, histmask, pathlen):
        # y, x should be in valid range.
        nonlocal maxpathlen

        # check mask history of this cell
        if histmask in visited[y][x]: return
        visited[y][x][histmask] = 1
        maxpathlen = max(maxpathlen, pathlen)

        for dy,dx in deltas:
            ny,nx = y+dy,x+dx
            # check boundness
            if not (0<=ny<R and 0<=nx<C): continue

            # check if we already passed the alphabet.
            mask = gen_mask(board[ny][nx])
            if mask & histmask: continue

            dfs(ny, nx, histmask | mask, pathlen+1)
        #
    dfs(0, 0, gen_mask(board[0][0]), 1)

    return maxpathlen



R,C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input().strip())
    assert len(board[-1]) == C
print(solve_optimum(board))



'''
예제 입력 1
2 4
CAAB
ADCB
예제 출력 1
3

run=(python3 1987.py)

echo '2 4\nCAAB\nADCB' | time $run
echo '3 6\nHFDFFB\nAJHGDH\nDGAGEH' | time $run
echo '5 5\nIEFCJ\nFHFKC\nFFALF\nHFGCF\nHMCHH' | time $run
-> 3 6 10


예제 입력 2
3 6
HFDFFB
AJHGDH
DGAGEH
예제 출력 2
6

예제 입력 3
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
예제 출력 3
10

1 1
A
-> 1

2 2
AA
AB
-> 1

1 10
ABAAAAAAAA
-> 2

echo '4 4\nABCD\nBCDA\nCDAB\nDABC' | time $run
-> 4

echo $worstcase | time $run
-> 26

worstcase=`cat <<EOF
26 26
ABCDEFGHIJKLMNOPQRSTUVWXYZ
BCDEFGHIJKLMNOPQRSTUVWXYZA
CDEFGHIJKLMNOPQRSTUVWXYZAB
DEFGHIJKLMNOPQRSTUVWXYZABC
EFGHIJKLMNOPQRSTUVWXYZABCD
FGHIJKLMNOPQRSTUVWXYZABCDE
GHIJKLMNOPQRSTUVWXYZABCDEF
HIJKLMNOPQRSTUVWXYZABCDEFG
IJKLMNOPQRSTUVWXYZABCDEFGH
JKLMNOPQRSTUVWXYZABCDEFGHI
KLMNOPQRSTUVWXYZABCDEFGHIJ
LMNOPQRSTUVWXYZABCDEFGHIJK
MNOPQRSTUVWXYZABCDEFGHIJKL
NOPQRSTUVWXYZABCDEFGHIJKLM
OPQRSTUVWXYZABCDEFGHIJKLMN
PQRSTUVWXYZABCDEFGHIJKLMNO
QRSTUVWXYZABCDEFGHIJKLMNOP
RSTUVWXYZABCDEFGHIJKLMNOPQ
STUVWXYZABCDEFGHIJKLMNOPQR
TUVWXYZABCDEFGHIJKLMNOPQRS
UVWXYZABCDEFGHIJKLMNOPQRST
VWXYZABCDEFGHIJKLMNOPQRSTU
WXYZABCDEFGHIJKLMNOPQRSTUV
XYZABCDEFGHIJKLMNOPQRSTUVW
YZABCDEFGHIJKLMNOPQRSTUVWX
ZABCDEFGHIJKLMNOPQRSTUVWXY
EOF
`



----

export _N=5

(python3 <<EOF
import time,os
from random import seed,randint
#seed(time.time())
seed(43)
N = int(os.getenv('_N','5'))
R,C = N,N
print(R,C)
for r in range(R):
    print(''.join([ chr(ord('A')+randint(0,25)) for c in range(C) ]))
EOF
) | time $run

->
$run  0.04s user 0.01s system 67% cpu 0.071 total

'''

