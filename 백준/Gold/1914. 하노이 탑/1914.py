'''
1914번

하노이 탑 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
6 초	128 MB	45814	9923	7607	23.241%

문제
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다.
이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

아래 그림은 원판이 5개인 경우의 예시이다.

입력
첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄에 옮긴 횟수 K를 출력한다.

N이 20 이하인 입력에 대해서는 두 번째 줄부터 수행 과정을 출력한다.
두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데,
이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.
N이 20보다 큰 경우에는 과정은 출력할 필요가 없다.

----

10:54~11:07

'''


import sys

def solve(N):
    move_history = []
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
# print(f'total {cnt} moves.', file=sys.stderr)



'''
예제 입력 1
3
예제 출력 1
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3

run=(python3 1914.py)

echo 25 | time $run
33554431

'''
