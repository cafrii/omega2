'''
다른 방법의 dp로 풀이

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    # reverse graph
    rgraph = [ [] for _ in range(N+1) ]
    for _ in range(M):
        a,b = map(int, input().split()) # a->b
        rgraph[b].append(a)
    return N,rgraph

def solve_dp(N:int, rgraph:list[list[int]])->list[int]:
    '''
    입력을 받을 때 a->b 관계 (b 의 선수 과목이 a) 를 b 기준으로 저장.
    모든 (a...) -> b 에 대해서 a < b 라는 사실을 활용하면 sort() 없이 계산 가능.
    '''
    preq = [1] * (N+1)
    for b in range(1, N+1):
        if not rgraph[b]: continue
        # rgraph[b] = [a1, a2, a3, ..]  a1->b, a2->b, a3->b, ..
        #   all (a1,a2,a3,..) are greater than b, by pre-condition.
        preq[b] = max(preq[a] for a in rgraph[b]) + 1
    return preq[1:]
    # del preq[0]; return preq

if __name__ == '__main__':
    inp = get_input()
    print(*solve_dp(*inp))




'''
예제 입력 1
3 2
2 3
1 2
예제 출력 1
1 2 3

run=(python3 14567.py)

echo '3 2\n2 3\n1 2' | $run
# 1 2 3

예제 입력 2
6 4
1 2
1 3
2 5
4 5
예제 출력 2
1 2 2 1 3 1

echo '6 4\n1 2\n1 3\n2 5\n4 5' | $run
# 1 2 2 1 3 1


echo '1 0' | $run
# 1
echo '3 0' | $run
# 1 1 1
echo '3 1\n2 3' | $run
# 1 1 2



# 과목의 수: 1 ≤ N ≤ 1000
# 선수조건:  0 ≤ M ≤ 500_000


(python3 <<EOF
from random import randint,seed
seed(43)
N,M = 1000,500_000
links = []
for _ in range(M):
    a = randint(1,N-1)
    b = randint(a+1,N)
    links.append((a,b))
# links.sort(key = lambda x: x[0])
print(N,M)
for a,b in links:
    print(a,b)
EOF
) | time $run


'''
