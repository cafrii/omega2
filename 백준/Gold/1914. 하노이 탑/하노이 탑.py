
import sys

def solve(N):
    move_history = []
    track = True if N<=20 else False
    counts = [0]*(N+1)

    def track_moves(num, frm, via, to)->int:
        # num 개의 원판을 frm 에서 to 로 이동. via 를 중간 보관용으로 활용.
        if num == 1:
            move_history.append((frm, to))
            return 1
        if num == 2:
            move_history.append((frm, via))
            move_history.append((frm, to))
            move_history.append((via, to))
            return 3

        cnt = track_moves(num-1, frm, to, via)
        cnt = cnt + track_moves(1, frm, 0, to)
        cnt = cnt + track_moves(num-1, via, frm, to)
        return cnt


    def count_moves(num)->int:
        # just count moves without tracking.
        if counts[num]:
            return counts[num]
        counts[num] = count_moves(num-1)*2 + 1
        return counts[num]

    if N > 20: # count only
        counts[1] = 1
        counts[2] = 3
        total_cnt = count_moves(N)
    else:
        total_cnt = track_moves(N, 1, 2, 3) # 1에서 2를 거쳐 3으로.

    return total_cnt, move_history

N = int(input().strip())
cnt,history = solve(N)
print(cnt)
for h in history:
    print(*h)
