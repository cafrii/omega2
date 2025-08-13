'''
10775번
공항 성공다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	256 MB	27944	10218	7702	36.226%

문제
오늘은 신승원의 생일이다.

박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.

공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.

공항에는 P개의 비행기가 순서대로 도착할 예정이며,
당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다.
비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.

신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다.
승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?

입력
첫 번째 줄에는 게이트의 수 G (1 ≤ G ≤ 105)가 주어진다.
두 번째 줄에는 비행기의 수 P (1 ≤ P ≤ 105)가 주어진다.
이후 P개의 줄에 gi (1 ≤ gi ≤ G) 가 주어진다.

출력
승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력한다.

-------

6:10~6:26

분리 집합 문제라는 것을 이미 알아 버린 후에 문제 풀기 시작.
푸는 방법은 간단하나, timeout 이 나지 않도록 하는 빠른 알고리즘을 찾는 것이 관건.

속도 개선의 여지가 있음.
-> 이런 저런 개선들 적용. 10775a.py 참고.
그래도 최소 시간 달성은 못했음.

'''




import sys
from typing import Iterator

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    G = int(input().rstrip())
    P = int(input().rstrip())
    def gen():
        for i in range(P):
            gi = int(input().rstrip())
            yield i,gi
        return
    return G,P,gen()

def solve(G:int, P:int, it:Iterator)->int:
    '''
    it: iterator which yield (seq,gi) where
        gi is gate index (1-based) for plane will arrive at,
        seq is sequence index of iteration (start from 0)
    '''
    gates = list(range(G+1))
    # gates[k]: k번 gate 의 상태 정보
    #   k: 이 gate가 available 하면 자신 gate 번호.
    #   <k: 이 gate가 occupied 이면, 자신 번호보다 작은 gate 중,
    #       available 한 (available 할 것으로 예상하는) gate 번호
    #   0: 이 gate 포함 이전 gate 모두 full occupied
    # gates[0] is always 0 (fixed!)

    def find_root(a:int)->int:
        log("    finding root (%d):", a)
        if a == gates[a]: return a
        stack = []
        while a != gates[a]:
            stack.append(a)
            a = gates[a]
        log("    stack %s", stack)
        for s in stack: gates[s] = a
        return a

    for i,a in it:
        log("[%d] %d, gates: %s", i, a, gates)
        ra = find_root(a)
        log("    ra %d", ra)
        if ra == 0: return i  # all gates (< a) occupied
        gates[ra] = find_root(ra-1)

    return P


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)


'''
예제 입력 1
4
3
4
1
1
예제 출력 1
2
예제 입력 2
4
6
2
2
3
3
4
4
예제 출력 2
3


run=(python3 10775.py)

echo '4\n3\n4\n1\n1' | $run
# -> 2

echo '4\n6\n2\n2\n3\n3\n4\n4' | $run
# -> 3

echo '5\n7\n3\n3\n4\n4\n5\n2\n1' | $run
# -> 5






(python3 <<EOF
import time
from random import seed,randint
# seed(time.time())
seed(43)
G,P = 100_000,100_000
G,P = 10,10
print(G)
print(P)
for _ in range(P):
    print(G)
EOF
) | time $run

'''


