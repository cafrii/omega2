'''
28018번
시간이 겹칠까?, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	1621	689	540	40.299%

문제
얼마 전 부산대학교 커뮤니티에 어느 시간대에 도서관의 열람실 좌석이 널널한지에 관한 질문 글이 올라왔다.
작성자는 지난주 일요일에 언제 도서관의 열람실을 이용했는지 댓글을 달아달라고 부탁하였다.
이에 많은 학생이 본인이 있던 시간을 댓글로 달아주었다.
자랑스러운 부산대학교 학생들은 공부하는 시간에는 도서관에 배정된 자신의 좌석을 비우지 않는다.
각 좌석은 사용이 종료되는 시각에 곧바로 선택될 수 없다.

편의상 시각은 0부터 1,000,000까지 주어지며 정수 단위로 구분된다.
특정한 시각에 선택할 수 없는 좌석이 몇 개였는지 알아보자.

입력
댓글을 달아준 학생 수 N이 주어진다. (1 <= N <= 100,000)
다음 N개 줄에는 각 학생의 좌석 배정 시각 S와 종료 시각 E가 주어진다.
(1 <= S <= E <= 1,000,000)
다음 줄에는 특정한 시각의 개수 Q가 주어진다. (1 <= Q <= 100,000)
다음 줄에는 알고자 하는 특정 시각 Q개가 주어진다.

출력
특정 시각에 선택할 수 없는 좌석 수를 주어진 순서에 따라 줄마다 출력하라.

----

9:06~9:34

검증 완료

'''

import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        s,e = map(int, input().split())
        A.append((s, e))
    _ = int(input().rstrip())
    Q = list(map(int, input().split()))
    return N,A,Q

def solve(N:int, A:list[tuple[int,int]], Q:list[int])->list[str]:
    '''
    Args:
    Returns:
    '''
    MAX_T = 1_000_000
    # differential sum
    D = [0] * (MAX_T + 2)
    max_t = 0

    # s, e 는 zero-based 이다.
    # s는 공부를 시작한 시각, e는 공부를 끝낸 시각+1
    for s,e in A:
        D[s] += 1
        D[e+1] -= 1
        if max_t < e: max_t = e

    for k in range(1, max_t+2): # k: 1 ~ max_t+1
        D[k] = D[k-1] + D[k]
    assert D[max_t+1] == 0

    return [ str(D[q]) for q in Q ]

if __name__ == '__main__':
    print('\n'.join(solve(*get_input())))


'''
예제 입력 1
1
1 3
2
2 4
예제 출력 1
1
0
예제 입력 2
2
1 5
3 6
3
2 3 7
예제 출력 2
1
2
0
----

pr=28018
run=(python3 a$pr.py)

echo '1\n1 3\n2\n2 4' | $run
# 1
# 0

echo '2\n1 5\n3 6\n3\n2 3 7' | $run
# 1
# 2
# 0

'''

