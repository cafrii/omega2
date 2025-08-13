'''
recursion error 가 발생하는 것이 이해가 안되어서
랜덤 test case를 생성하여 recursion 수가 일정 이상일 경우 로그 표시하도록 함.

아래에 recursion limit error 발생하는 입력 시퀀스 추가함.

'''

import sys
from heapq import heappush, heappop

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,Q = map(int, input().split())
    edges = []
    for _ in range(Q):
        a,b,c,t = map(int, input().split())
        heappush(edges, (c,t,a,b))
    return N,edges


def solve(N:int, edges:list):
    '''
    '''
    roots = list(range(N+1))
    depth = 0

    def find_root(a:int)->int:
        nonlocal depth
        if roots[a] == a: return a
        depth += 1
        # assert depth < 5, "deep recursion!"
        roots[a] = find_root(roots[a])
        depth -= 1
        return roots[a]

    num_links,total_cost = 0,0
    finished_at = 0
    while edges:
        c,t,a,b = heappop(edges)
        # log("(%d/%d, c %d t %d) %s", a,b,c,t, roots)
        ra,rb = find_root(a),find_root(b)
        # log("       ra/rb %d/%d", ra, rb)
        if ra == rb: continue  # cycle!

        roots[rb] = roots[b] = ra
        total_cost += c
        num_links += 1
        finished_at = max(finished_at, t)

        if num_links >= N-1: break

    if num_links >= N-1:
        return finished_at,total_cost
    else:
        return -1,-1


if __name__ == '__main__':
    inp = get_input()
    t,c = solve(*inp)
    if t < 0: print(-1)
    else: print(t, c)


'''

run=(python3 30797e.py)

echo '4 5\n1 4 1 5\n2 3 1 1000000000\n1 4 1 13\n3 2 1 117\n2 4 1 10' | $run
# -> 117 3
echo '2 2\n1 2 5 1\n2 1 3 2' | $run
# -> 2 3
echo '5 1\n1 4 5 7' | $run
# -> -1


# deep recursion 이 생성되는 예시
10 9
8 9 2 0
7 8 3 0
6 7 4 0
5 6 5 0
4 5 6 0
3 4 7 0
2 3 8 0
1 2 9 0
9 10 10 0

echo '10 9\n8 9 2 0\n7 8 3 0\n6 7 4 0\n5 6 5 0\n4 5 6 0\n3 4 7 0\n2 3 8 0\n1 2 9 0\n9 10 10 0' | $run

맨 마지막 edge, (9, 10) 을 연결하기 직전, roots[] 상태는 다음과 같으며,
[0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 10]

find_root(9) 는 roots[9]->8, roots[8]->7, roots[7]->6, ... 와 같이 총 9회의 재귀 호출이 발생한다.



(python3 <<EOF
N = 1000
Q = N-1
print(N, Q)
for k in range(1,Q):
    # 998 999 1 0
    # 997 998 2 0
    # ...
    # 1   2   998 0
    # 999 1000 999 0
    print(Q-k, Q+1-k, k, 0)
print(Q, Q+1, Q, 0)
EOF
) | time $run

->
  File "/Users/yhlee/work/github/cafrii/omega2/_draft/boj/30797e.py", line 35, in find_root
    roots[a] = find_root(roots[a])
...
  [Previous line repeated 995 more times]
RecursionError: maximum recursion depth exceeded

'''


