'''

재귀 호출 버전.
recursion depth 측정 등..

제출 현황. 최소 168ms.
97418592 cafrii  10775 맞았습니다!! 40428KB 168ms Python 3 1321B
97418505 cafrii  10775 맞았습니다!! 40428KB 176ms Python 3 1339B
97417797 cafrii  10775 맞았습니다!! 40428KB 172ms Python 3 1366B
97401569 cafrii  10775 맞았습니다!! 40428KB 172ms Python 3 1355B

더 빠른 제출도 있긴 함. 하지만 알고리즘은 거의 동일.
97239271 dnmslyyd 10775 맞았습니다!! 37048KB 100ms Python 3 402B

'''




import sys
from typing import Iterator

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    G = int(input())
    P = int(input())
    def gen():
        for i in range(P):
            gi = int(input())
            yield i,gi
        return
    return G,P,gen()

def solve(G:int, P:int, it:Iterator)->int:
    '''
    it: iterator which yield (seq,gi) where
        gi is gate index (1-based) for plane will arrive at,
        seq is sequence index of iteration (start from 0)
    '''
    log("G %d, P %d", G, P)

    lm = sys.getrecursionlimit()
    log("recursion limit: %d", lm)
    sys.setrecursionlimit(max(lm, P+50))

    gates = list(range(G+1))
    # gates[k]: k번 gate 의 상태 정보
    #   k: 이 gate가 available 하면 자신 gate 번호.
    #   <k: 이 gate가 occupied 이면, 자신 번호보다 작은 gate 중,
    #       available 한 (available 할 것으로 예상하는) gate 번호
    #   0: 이 gate 포함 이전 gate 모두 full occupied
    # gates[0] is always 0 (fixed!)

    def find_root(a:int)->int:
        if a == gates[a]: return a
        gates[a] = ra = find_root(gates[a]) # 경로 압축
        return ra

    for i,a in it:
        ra = find_root(a)
        if ra == 0: return i  # all gates (< a) occupied
        gates[ra] = gates[a] = find_root(ra-1)

    return P


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)


'''


run=(python3 10775.py)

echo '4\n3\n4\n1\n1' | $run
# -> 2

echo '4\n6\n2\n2\n3\n3\n4\n4' | $run
# -> 3

echo '5\n7\n3\n3\n4\n4\n5\n2\n1' | $run
# -> 5


# deep recursion simulation

echo '10\n10\n9\n9\n8\n7\n6\n5\n4\n3\n2\n9' | $run

# 설명:
# gates 를 아래 상태가 되도록 a 순서를 준비한 후
#    gates: [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
# 최종적으로 다시 a=9 를 요청하면 연쇄 재귀호출이 발생한다.
#


(python3 <<EOF
import time
from random import seed,randint
# seed(time.time())
# seed(43)
# G,P = 100_000,100_000
G,P = 10,10
A = list(range(P,0,-1))
A[0] = A[-1] = P-1
print(G)
print(P)
print('\n'.join(map(str, A)))
EOF
) | time $run



# 일반 압축
#    gates[ra] = find_root(ra-1)
$run  0.05s user 0.01s system 89% cpu 0.070 total

# 이중 경로 압축
#    gates[ra] = gates[a] = find_root(ra-1)
$run  0.05s user 0.01s system 89% cpu 0.068 total
# 약간 개선. 그런데 차이는 미미하다.

# 리턴 변수
$run  0.05s user 0.01s system 86% cpu 0.066 total
# ok

# 비 재귀, 이중경로 압축
$run  0.06s user 0.01s system 89% cpu 0.068 total

# enumerate 대신 자체 변수
$run  0.05s user 0.01s system 88% cpu 0.068 total

# .rstrip 제거
$run  0.05s user 0.01s system 87% cpu 0.066 total

# generator tuple 리턴
$run  0.05s user 0.01s system 88% cpu 0.065 total

크게 개선이 되진 않음. 지금도 이미 짧은 시간이라, generator 와 같은 것들의 오버헤드 때문인듯.

'''


