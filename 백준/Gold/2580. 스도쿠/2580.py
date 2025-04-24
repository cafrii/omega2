
'''
스도쿠 스페셜 저지

문제

스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다. 이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.

나머지 빈 칸을 채우는 방식은 다음과 같다.

각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
위의 예의 경우, 첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로 첫째 줄 빈칸에는 1이 들어가야 한다.

또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이 이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.

이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.

게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

입력
아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다. 스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

출력
모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.

스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.

'''

import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

# input
board = []
for y in range(9):
    a = list(map(int, input().split()))
    assert len(a) == 9
    board.append(a)

def print_board(to = sys.stdout):
    [ print(*a, file=to) for a in board ]

# print_board(sys.stderr)




# 0 의 위치 정보 수집.
# zeros[] 는 (y, x, level) 의 튜플.
#   (y,x) 는 0 이 위치한 좌표
#   level 은 난이도. 난이도는 가로, 세로, 구역 내에 포함된 0 의 개수.
zeros = []

def prepare():
    for y in range(9):
        for x in range(9):
            if board[y][x]: continue

            # 가로 줄 에서의 0 의 개수 (자신 제외)
            lv1 = board[y].count(0) - 1
            # 세로 줄 ..
            lv2 = (sum(1 for k in range(9) if board[k][x] == 0) - 1)
            # 구역 내
            y2,x2 = y//3*3, x//3*3
            lv3 = sum(1 for j in range(x2, x2+3)
                      for k in range(y2, y2+3) if board[k][j] == 0) - 1

            # log("(%d,%d): %d, %d, %d", y, x, lv1, lv2, lv3)
            zeros.append((y, x, lv1 + lv2 + lv3))

    # log("zeros #%d, %s", len(zeros), zeros)
    # level 을 기준으로 오름차순 정렬. 쉬운 문제 부터 푸는 것이 유리할 것 같아서.
    # 비교해 보니 별 차이는 없는 듯 함..

    zeros.sort(key = lambda e: e[2])
    log("sorted zeros #%d, %s", len(zeros), zeros)


def prepare2():
    for y in range(9):
        for x in range(9):
            if board[y][x]: continue
            zeros.append((y, x, 0))


fullset = set(range(1,10))



def get_avail(y_, x_):
    # (y_,x_) 기준으로 사용 가능한 숫자 목록 추출

    # 가로축 검토. 0 이 아닌 숫자만 추출
    availset = fullset - set(board[y_])
    # 세로축
    availset -= set(board[y][x_] for y in range(9))
    # 구역
    ya, xa = y_//3*3, x_//3*3 # aligned y, x
    availset -= set(board[y][x] for x in range(xa, xa+3) for y in range(ya, ya+3))

    return sorted(list(availset))


def is_allowed(y_, x_, num):
    if num in board[y_]: # 가로 체크
        return False
    for y in range(9): # 세로 체크
        if board[y][x_] == num:
            return False
    ya, xa = y_//3*3, x_//3*3   # aligned y, x
    for y in range(ya, ya + 3): # 구역 체크
        for x in range(xa, xa + 3):
            if board[y][x] == num:
                return False
    return True


'''
이 함수로는 시간 초과가 발생...
'''
def solve_step(n_solved:int) -> bool:
    # Args:
    #   zeros[] 를 순서대로 solve 하는데
    #   현재까지 solve 된 개수가 n_solved 이다.
    # Returns:
    #   finished:bool
    #
    if n_solved >= len(zeros): # 다 푼 경우임.
        # log("~~ finished ~~")
        return True

    # use y, x as running variable.
    y_,x_,lvl = zeros[n_solved] # target y, x and level
    # log("step %d: (%d,%d) level %d", n_solved, y_, x_, lvl)

    avail = get_avail(y_, x_)
    if not avail:
        # log("!! step %d: no available digits", n_solved)
        return False
    # log("step %d: (%d,%d) lv %d, avail %s", n_solved, y_, x_, lvl, avail)

    # 차례대로 하나씩 검토
    for e in avail:
        # log("step %d:     (%d,%d) <= %d", n_solved, y_, x_, e)
        board[y_][x_] = e
        success = solve_step(n_solved + 1)
        # 문제 조건에서, 하나라도 만족하는 해가 찾아지면 종료
        if success:
            return True
        board[y_][x_] = 0 # rollback

    # log("step %d: no success on %s", n_solved, avail)
    return False


# set 를 사용하지 않는 버전으로 개선.
def solve_step2(n_solved:int) -> bool:
    if n_solved >= len(zeros):
        # log("~~ finished ~~")
        return True

    y_,x_,lvl = zeros[n_solved] # target y, x and level
    # log("step %d: (%d,%d) level %d", n_solved, y_, x_, lvl)

    # 모든 숫자를 순서대로 체크
    for num in range(1, 10):
        if not is_allowed(y_, x_, num): continue
        # log("step %d:     (%d,%d) <= %d", n_solved, y_, x_, e)
        board[y_][x_] = num
        success = solve_step2(n_solved + 1)
        if success:
            return True
        board[y_][x_] = 0 # rollback

    return False



prepare2()

if solve_step2(0):
    print_board()




'''
python3 2580.py << EOF
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
EOF


echo '0 3 5 4 6 9 2 7 8\n7 8 2 1 0 5 6 0 9\n0 6 0 2 7 8 1 3 5\n3 2 1 0 4 6 8 9 7\n8 0 4 9 1 3 5 0 6\n5 9 6 8 2 0 4 1 3\n9 1 7 6 5 2 0 8 0\n6 0 3 7 0 1 9 5 2\n2 5 8 3 9 4 7 6 0' \
    | python3 2580.py



--
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

0 2 0 9 0 5 0 0 0
5 9 0 0 3 0 2 0 0
7 0 0 6 0 2 0 0 5
0 0 9 3 5 0 4 6 0
0 5 4 0 0 0 7 8 0
0 8 3 0 2 7 5 0 0
8 0 0 2 0 9 0 0 4
0 0 5 0 4 0 0 2 6
0 0 0 5 0 3 0 7 9

0 0 0 0 4 3 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 5 0 0 0 0
0 8 0 7 0 0 0 2 0
0 6 0 0 0 0 0 0 3
0 0 0 0 0 0 0 4 0
0 0 5 8 0 0 6 0 0
4 0 0 1 0 0 0 0 0
3 0 0 0 0 0 5 0 0

'''
