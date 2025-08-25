'''
14567번
선수과목 (Prerequisite) 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
5 초	256 MB	9068	5994	4524	66.063%

문제
올해 Z대학 컴퓨터공학부에 새로 입학한 민욱이는 학부에 개설된 모든 전공과목을 듣고 졸업하려는 원대한 목표를 세웠다.
어떤 과목들은 선수과목이 있어 해당되는 모든 과목을 먼저 이수해야만 해당 과목을 이수할 수 있게 되어 있다.
공학인증을 포기할 수 없는 불쌍한 민욱이는 선수과목 조건을 반드시 지켜야만 한다.
민욱이는 선수과목 조건을 지킬 경우 각각의 전공과목을 언제 이수할 수 있는지 궁금해졌다.
계산을 편리하게 하기 위해 아래와 같이 조건을 간소화하여 계산하기로 하였다.

1. 한 학기에 들을 수 있는 과목 수에는 제한이 없다.
2. 모든 과목은 매 학기 항상 개설된다.

모든 과목에 대해 각 과목을 이수하려면 최소 몇 학기가 걸리는지 계산하는 프로그램을 작성하여라.

입력
첫 번째 줄에 과목의 수 N(1 ≤ N ≤ 1000)과 선수 조건의 수 M(0 ≤ M ≤ 500000)이 주어진다.
선수과목 조건은 M개의 줄에 걸쳐 한 줄에 정수 A B 형태로 주어진다.
A번 과목이 B번 과목의 선수과목이다.
A < B인 입력만 주어진다. (1 ≤ A < B ≤ N)

출력
1번 과목부터 N번 과목까지 차례대로 최소 몇 학기에 이수할 수 있는지를 한 줄에 공백으로 구분하여 출력한다.

----

6:02~6:35

----
시간 개선

1.
topological sorting (khan 알고리즘) -> 14567b_ts.py

2.
또 다른 dp 방식인데, sort() 사용하지 않는 새 방식. -> 14567c_dp.py


시간 개선 결과

97827400  cafrii  14567  맞았습니다!!  45144KB   392ms Python 3   735B   <- 14567c_dp.py
97826401  cafrii  14567  맞았습니다!!  52496KB   556ms Python 3  1286B   <- 14567b_ts.py
97819287  cafrii  14567  맞았습니다!!  94704KB  1204ms Python 3   609B   <- 14567.py

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

'''
과목: 1~ 양수.
과목의 수: 1 ≤ N ≤ 1000
선수조건:  0 ≤ M ≤ 500_000
'''

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    links = []
    for _ in range(M):
        a,b = map(int, input().split())
        links.append((a,b))
    return N,links

def solve_dp(N:int, links:list[tuple[int,int]])->list[int]:
    '''
    진입 노드 관점에서의 dp.
    a -> b 간선 (b 의 선수 과목이 a) 인 경우, b 의 차수 (수강 학기) 를 dp로 계산

    '''
    links.sort()
    dp = [1] * N
    for a,b in links:
        dp[b-1] = max(dp[a-1]+1, dp[b-1])
    return dp

if __name__ == '__main__':
    inp = get_input()
    lst = solve_dp(*inp)
    print(' '.join(map(str, lst)))




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
