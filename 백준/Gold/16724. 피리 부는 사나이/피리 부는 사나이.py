
import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(input().rstrip())
        assert len(board[-1]) == M
    return board


def solve_bf(board:list[str])->int:
    '''
    '''
    N,M = len(board),len(board[0])

    # region map
    rmap = [ [-1]*M for k in range(N) ]
    rid = 0
    valid_rid_count = 0

    str2dir = {'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0) }

    def mark_region(y:int, x:int, rid:int):
        if rid < 0:
            return -1
        while (0<=y<N and 0<=x<M):
            if rmap[y][x] >= 0:
                if rmap[y][x] == rid: # meet self
                    return rid
                else: # meet previous region
                    return rmap[y][x]
            rmap[y][x] = rid
            dy,dx = str2dir[board[y][x]]
            y,x = y+dy,x+dx
        return -1 # it should not happen

    for y in range(N):
        for x in range(M):
            if rmap[y][x] < 0:
                new_rid = mark_region(y, x, rid)
                if new_rid >= 0:
                    if new_rid == rid:
                        valid_rid_count += 1
                    rid += 1

    return valid_rid_count


if __name__ == '__main__':
    inp = get_input()
    print(solve_bf(inp))
