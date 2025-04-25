'''
스도쿠 성공다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	29509	14234	10207	45.683%
문제
스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열,
그리고 9개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다.
예를 들어 다음을 보자.

위 그림은 참 잘도 스도쿠 퍼즐을 푼 경우이다.
각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고,
각 3×3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.

하다 만 스도쿠 퍼즐이 주어졌을 때, 마저 끝내는 프로그램을 작성하시오.

입력
9개의 줄에 9개의 숫자로 보드가 입력된다. 아직 숫자가 채워지지 않은 칸에는 0이 주어진다.

출력
9개의 줄에 9개의 숫자로 답을 출력한다. 답이 여러 개 있다면 그 중 사전식으로 앞서는 것을 출력한다.
즉, 81자리의 수가 제일 작은 경우를 출력한다.

'''

import sys
input = sys.stdin.readline

board:list[list[int]] = []
for _ in range(9):
    board.append([ int(x) for x in input().strip() ])
    assert len(board[-1]) == 9

zeros = []
for y in range(9):
    for x in range(9):
        if board[y][x] == 0:
            zeros.append((y, x))
# print(len(zeros))

def print_board(to=sys.stdout):
    for y in range(9):
        print(*board[y], sep='', file=to)

def is_allowed(r, c, num) -> bool:
    if num in board[r]:
        return False
    for y in range(9):
        if board[y][c] == num: return False
    ya,xa = r//3*3, c//3*3
    for y in range(ya, ya+3):
        for x in range(xa, xa+3):
            if board[y][x] == num: return False
    return True


def step(index:int):
    # solve zero in zeros[index] location
    if index >= len(zeros): # all zeros are filled
        return True

    r,c = zeros[index] # target location (row, col)

    for i in range(1, 10): # candidates
        if not is_allowed(r, c, i): continue
        board[r][c] = i
        if step(index+1):
            return True
        board[r][c] = 0 # recover and try next i

if step(0):
    print_board()


'''
예제 입력 1
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107

예제 출력 1
143628579
572139468
986754231
391542786
468917352
725863914
237481695
619275843
854396127

'''
