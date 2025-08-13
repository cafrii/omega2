'''
1717번
집합의 표현 스페셜 저지
골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	124814	41199	25172	29.070%

문제
초기에 $n+1$개의 집합 ${0}, {1}, {2}, dots , {n}$이 있다.
여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.

입력
첫째 줄에 $n$, $m$이 주어진다.
$m$은 입력으로 주어지는 연산의 개수이다.
다음 $m$개의 줄에는 각각의 연산이 주어진다. 합집합은 $0$ $a$ $b$의 형태로 입력이 주어진다.
이는 $a$가 포함되어 있는 집합과, $b$가 포함되어 있는 집합을 합친다는 의미이다.
두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 $1$ $a$ $b$의 형태로 입력이 주어진다.
이는 $a$와 $b$가 같은 집합에 포함되어 있는지를 확인하는 연산이다.

출력
1로 시작하는 입력에 대해서 $a$와 $b$가 같은 집합에 포함되어 있으면 "YES" 또는 "yes"를,
그렇지 않다면 "NO" 또는 "no"를 한 줄에 하나씩 출력한다.

제한
- $1 ≤ n ≤ 1,000,000$
- $1 ≤ m ≤ 100,000$
- $0 ≤ a, b ≤ n$
- $a$, $b$는 정수
- $a$와 $b$는 같을 수도 있다.



--------

2:49~3:01

dsu 의 원형 같은 문제


'''



import sys
from typing import Iterator

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input()->tuple[int,Iterator]:
    input = sys.stdin.readline
    N,M = map(int, input().split())
    def gen():
        for _ in range(M):
            c,a,b = map(int, input().split())
            yield c,a,b
        return
    return N,gen()

def solve(N:int,it:Iterator)->Iterator:
    '''
    '''
    roots = list(range(N+1))

    def find_root(a:int):
        if a == roots[a]: return a
        stack = []
        while a != roots[a]:
            stack.append(a)
            a = roots[a]
        for s in stack: roots[s] = a
        return a

    for cmd,a,b in it:
        ra,rb = find_root(a),find_root(b)
        if cmd == 1:
            yield 'YES' if ra == rb else 'NO'
        else:
            if ra == rb: continue
            roots[b] = roots[rb] = ra
    return

if __name__ == '__main__':
    inp = get_input()
    # it = solve(*inp)
    # print('\n'.join( s for s in it ))
    # print('\n'.join( it ))
    for s in solve(*inp): print(s)


'''
예제 입력 1
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
예제 출력 1
NO
NO
YES


run=(python3 1717.py)

echo '7 8\n0 1 3\n1 1 7\n0 7 6\n1 7 1\n0 3 7\n0 4 2\n0 1 1\n1 1 1' | $run
# -> n n Y

echo '10 6\n0 0 0\n0 0 0\n1 0 0\n1 0 1\n0 0 1\n1 1 0' | $run
# -> Y n Y

echo '2 2\n0 1 2\n1 1 2' | $run
# -> Y
echo '7 4\n0 1 3\n0 7 6\n0 3 6\n1 7 6' | $run
# -> Y

'''
