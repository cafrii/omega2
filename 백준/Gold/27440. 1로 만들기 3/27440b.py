'''

느린 27440a.py 를 개선해 보려고 시도한 버전.


개선 지점
1. visited 최적화
방문한 모든 노드를 다 저장하는 대신, 불필요한 것은 저장하지 않도록 할 수 있는가?
세 연산 중 +1 이 가장 작은 값을 만들어낸다. 이보다 더 작은 값은 유지할 필요가 없다.

que 를 priority que 또는 heapq 를 써서,
같은 distance 에서라면 숫자 값이 작은 것 부터 탐색.
이것보다는 ops 순서를 +1, x2, x3 으로 바꾸면, 항상 작은 숫자 부터 처리하는 셈이 된다.
이렇게 하면 visited 의 최소 경계는 알 수 있게 됨.
그런데, 더 이상 불필요한 visited 의 일부 데이터는 어떻게 없애는가? 이 없애는 작업 자체가 시간을 소모하진 않나?

2. pruning
아래 코드보다 더 강력한 pruning 이 존재하나?
```
if nx_num > N: continue # ignore
```

그런데 잘 모르겠음.

--------

# 일반적인 가지치기 (pruning) 기법

힌트 1: 상한을 먼저 구하라
아주 빠른 규칙(예: 역방향에서 “나눠지면 나누고, 아니면 1 빼기” 같은 탐욕)로 아무 해나 하나 빨리 만들어 그 길이를 상한(best)으로 잡아라.
가지치기는 “현재깊이 + 남은 하한 > best”일 때 자르는 식으로 작동한다.

힌트 2: 남은 최소 필요 횟수의 하한(lower bound)
현재 값이 x일 때 “곱셈만 쓴다고 가정”하면 N에 닿기 위한 최소 곱셈 횟수의 하한은 대략
⌈log3 (N/x)⌉ 이다. (+1은 성장을 못 하므로 하한을 줄이지 못함)
보수적으로는 max(0,⌈log3(N/x)⌉) 정도만으로도 충분히 많은 가지를 자를 수 있다.

힌트 3: 나눠떨어지게 만드는 비용까지 포함한 하한 보정
x가 2나 3으로 나눠떨어지지 않으면, 곱셈을 쓰기 전까지 최소 몇 번의 +1이 필요한지 d를 계산해 하한을
d + ⌈ log3 (N/(x+d)) ⌉ 처럼 보정하면 더 날카롭게 자를 수 있다.
포인트: +1은 “나눌 준비(정렬)” 용도로만 쓰인다고 생각하고, 그 준비 비용을 하한에 미리 반영한다.

힌트 4: 분기 자체를 줄이는 방향
양방향 탐색을 고려하라. 시작(1)과 목표(N)에서 동시에 확장하면, 중간에서 만나기 전에 많은 가지가 자연스럽게 잘린다.
역방향은 “나눠지면 나누기”가 빈번해 레벨 폭이 급격히 줄어드는 편이다.

힌트 5: 지배관계
같은 숫자에 도달하는 경로가 여러 개라면, 더 짧은 깊이만 유지하고 나머지는 버려라(이미 하고 있겠지만, 구조적으로 확실히 enforce).
추가로 같은 깊이에서 “곧바로 곱을 못 쓰는 상태”들 중, 더 적은 +1로 곱을 쓸 수 있는 상태만 남기는 식의 필터링을 고민해보라.

요약: 빠른 상한 확보 → 하한 계산 → branch-and-bound 가지치기, 그리고 양방향/역방향의 자연 가지치기

------
무슨 말인지 참 어렵다.
일단, 포기하고 다른 방식으로 재 고민하기로 함.


'''

import sys
from collections import deque

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N

def solve_bfs(N:int):
    '''
    연산의 종류
        op1: +1
        op2: x2
        op3: x3
    '''
    if N == 1:
        return 0

    maxqlen = 0
    answer = -1

    que = deque()
    visited = {}
    # visited = 0
    # 10^18 = (10^3)^6 ~= (2^10)^6 = 2^60
    # 64비트 정수로 표현은 가능하긴 하지만..
    # 이 개수 전체를 감당할 수 있는 메모리는 없음. sparse array에 기대보자.

    que.append((1, ''))

    while que:
        maxqlen = max(len(que), maxqlen)
        num,hist = que.popleft()
        if num == N:
            return len(hist)
        if num > N: return -1 # 실패!

        # ops = [ (num*3, '3'), (num*2, '2'), (num+1, '1') ]
        ops = [ (num+1, '1'), (num*2, '2'), (num*3, '3') ]
        for nx_num,nx_op in ops:
            if nx_num > N:
                continue # ignore
            nx_hist = hist + nx_op
            if nx_num == N:
                log("goal! %d, hist: %s", N, nx_hist)
                answer = len(nx_hist)
                break
            if nx_num in visited:
                continue
            que.append((nx_num, nx_hist))
            visited[nx_num] = 1
        else:
            if answer > 0: break

    log("maxqlen %d, num op %d", maxqlen, answer)
    return answer


if __name__ == '__main__':
    print(solve_bfs(get_input()))


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

echo '1000' | time $run
-> 0.033 sec

echo '5000' | time $run
-> 8.187 sec

이 방법은 문제가 있음!

echo '10000' | time $run
# -> 14
# goal! 10000, hist: 33122133131331

echo '100000' | time $run
goal! 100000, hist: 332122133131312222
18
$run  0.06s user 0.01s system 97% cpu 0.069 total

echo '1000000' | time $run
goal! 1000000, hist: 3332221332221222222
19
$run  0.16s user 0.01s system 98% cpu 0.175 total

echo '10000000' | time $run
22
goal! 10000000, hist: 3213321333313321321331
maxqlen 1720212, num op 22
$run  1.84s user 0.13s system 99% cpu 1.982 total

큐 크기도 너무 크다!


'''

