'''
16724번
피리 부는 사나이 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	12989	5944	4453	42.719%

문제
피리 부는 사나이 성우는 오늘도 피리를 분다.

성우가 피리를 불 때면 영과일 회원들은 자기도 모르게 성우가 정해놓은 방향대로 움직이기 시작한다.
성우가 정해놓은 방향은 총 4가지로 U, D, L, R이고 각각 위, 아래, 왼쪽, 오른쪽으로 이동하게 한다.

이를 지켜보던 재훈이는 더 이상 움직이기 힘들어하는 영과일 회원들을 지키기 위해
특정 지점에 ‘SAFE ZONE’ 이라는 최첨단 방음 시설을 만들어 회원들이 성우의 피리 소리를 듣지 못하게 하려고 한다.
하지만 예산이 넉넉하지 않은 재훈이는 성우가 설정해 놓은 방향을 분석해서 최소 개수의 ‘SAFE ZONE’을 만들려 한다.

성우가 설정한 방향 지도가 주어졌을 때 재훈이를 도와서 영과일 회원들이 지도 어느 구역에 있더라도
성우가 피리를 불 때 ‘SAFE ZONE’에 들어갈 수 있게 하는 ‘SAFE ZONE’의 최소 개수를 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에 지도의 행의 수를 나타내는 N(1 ≤ N ≤ 1,000)과 지도의 열의 수를 나타내는 M(1 ≤ M ≤ 1,000)이 주어진다.
두 번째 줄부터 N개의 줄에 지도의 정보를 나타내는 길이가 M인 문자열이 주어진다.
지도 밖으로 나가는 방향의 입력은 주어지지 않는다.

출력
첫 번째 줄에 ‘SAFE ZONE’의 최소 개수를 출력한다.

----

8:39~9:03

'''


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
    # valid_rids = []
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
                # id,sy,sx = mark_region(y, x, len(rid))
                new_rid = mark_region(y, x, rid)
                if new_rid >= 0:
                    if new_rid == rid:
                        # valid_rids.append(rid)
                        valid_rid_count += 1
                    rid += 1

    # return len(valid_rids)
    return valid_rid_count


if __name__ == '__main__':
    inp = get_input()
    print(solve_bf(inp))


'''
예제 입력 1
3 4
DLLL
DRLU
RRRU
예제 출력 1
2

2 20
RLRLRLRLRLRLRLRLRLRL
RLRLRLRLRLRLRLRLRRRL
-> 19

2 20
RLRLRLRLRLRLRLRLRLRL
RURURURURURURURURRRU
-> 10


run=(python3 16724.py)

echo '3 4\nDLLL\nDRLU\nRRRU' | $run


'''

