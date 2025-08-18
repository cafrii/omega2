'''
27440번
1로 만들기 3 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초 (추가 시간 없음)	1024 MB	1986	545	446	33.358%

문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 1018보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.


----

처음에 방향을 완전 잘못 잡았음.
mod 와 // 연산이 느리다는 것을 너무 의식해서, 1에서부터 x3, x2, +1 로 올라가는 탐색을 시도했음.
결국 올라가는 방식으로는 트리가 너무 커져서 실패!

다시 내려오는 방식으로 성공함.

더 최적의 방법인 27440c.py 를 숙지하고 기억하자!!


-----

97590107 cafrii  27440 맞았습니다!! 36448 KB  72 ms  Python 3  799B
87341275 jun83   27440 맞았습니다!! 32412 KB  36 ms  Python 3  176B   <- 훨씬 더 빠른 방법. 27440c.py 참고.


'''


import sys
from collections import deque

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N

def solve_bfs2(N:int):
    '''
    연산의 종류
        op1: +1
        op2: x2
        op3: x3
    '''
    if N <= 1:
        return 0

    maxqlen = 0
    que = deque()
    visited = {}
    # 10^18 = (10^3)^6 ~= (2^10)^6 = 2^60
    # 64비트 정수로 표현은 가능하긴 하지만..
    # 이 개수 전체를 감당할 수 있는 메모리는 없음. sparse array에 기대보자.

    cnt = 0
    que.append((N, cnt))

    while que:
        maxqlen = max(len(que), maxqlen)
        num,cnt = que.popleft()
        if num == 1:
            break
        if num%3 == 0 and num//3 not in visited:
            que.append((num//3, cnt+1))
            visited[num//3] = cnt+1
        if num%2 == 0 and num//2 not in visited:
            que.append((num//2, cnt+1))
            visited[num//2] = cnt+1
        if num-1 not in visited:
            que.append((num-1, cnt+1))
            visited[num-1] = cnt+1

    log("maxqlen %d, num op %d", maxqlen, cnt)
    return cnt


if __name__ == '__main__':
    print(solve_bfs2(get_input()))


'''
예제 입력 1
2
예제 출력 1
1
예제 입력 2

10
예제 출력 2
3

힌트
10의 경우에 10 → 9 → 3 → 1 로 3번 만에 만들 수 있다.

----

run=(python3 27440.py)

echo '2' | time $run
# -> 1
echo '10' | time $run
# -> 3
echo '1000' | time $run
# -> 9

echo '5000' | time $run
# -> 13

이 방법은 문제가 있음!

echo '10000' | time $run
# -> 14

echo '100000' | time $run
# -> 18

echo '1000000' | time $run
# -> 19

echo '10000000' | time $run
# -> 22

echo '1000000000000000000' | time $run
# -> 58
# $run  0.02s user 0.01s system 88% cpu 0.037 total



'''

