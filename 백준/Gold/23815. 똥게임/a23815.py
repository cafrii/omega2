'''
23815번
똥게임 성공 골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	1202	336	267	27.052%

문제

이 게임은 똥냄새가 너무 나서 도저히 볼 수가 없다!
따라서 당신은 직접 똥게임을 하지 않고 프로그램한테 똥게임을 시킬 것이다.
처음에는 사람 1명으로 시작한다.
당신에게는 총 N번의 턴이 주어지며, 각 턴마다 다음 선택지 4개중 2개가 주어진다.
같은 선택지가 주어질 수도 있다.
각 선택지는 +x, -x, *x, /x \, (1 <= x <= 9) 중 하나로 주어진다.

1. +x를 선택할 경우, 사람의 수가 x명만큼 증가한다.

2. -x를 선택할 경우, 사람의 수가 x명만큼 감소한다.

3. *x를 선택할 경우, 사람의 수가 x배가 된다.

4. /x를 선택할 경우, 사람의 수가 x만큼 나눠진다. 만약 현재 사람 수가 x로 나눠지지 않을 경우 나머지는 버린다.

N개의 선택지 중 1번에 한해 광고를 보고 선택지를 건너뛸 수 있다.
광고를 보지 않고 선택지를 건너뛰지 않아도 된다.
만약 각 턴이 끝난 뒤 현재 사람이 0명 이하가 되면 게임 오버가 된다.
당신은 N번의 선택지를 거친 후 사람의 수를 최대로 만들어야 한다.
어떠한 선택을 하더라도 중간에 사람의 수가 32비트 정수 범위를 넘지 않음을 보장한다.

입력
첫 번째 줄에 선택지의 개수 N, (1 <= N <= 100,000)가 주어진다.

그 이후 N개의 줄에 걸쳐 2개의 선택지가 공백을 사이로 두고 주어진다.

각 선택지는 +x, -x, *x, /x 중 하나로 주어진다 (1 <= x <= 9).

출력
N개의 선택지를 거친 후 최대 사람의 수를 출력한다.
만약 어떤 선택을 하더라도 게임 오버가 된다면 ddong game을 출력한다.

----
7:51~

skip 챈스를 사용한 경우와 사용하지 않은 경우의 상태를 분리해서 dp 테이블 구성.
오직 직전 상태만 참조하므로 굳이 테이블 필요도 없어 보임.
dp_prev 만 저장하면 됨.


'''


log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)


def get_input():
    import sys
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        a,b = input().split()
        A.append((a,b))
    return N,A


def solve(N:int, A:list[tuple[str,str]])->str:
    '''
    Returns:
        answer string
    '''

    def calc(num:int, ops:str)->int:
        '''
        Args: ops 는 문자 두개로 구성된 연산 명령
        Returns: 연산 적용 후 결과
        '''
        if num <= 0: return 0
        op = ops[0]
        arg = int(ops[1])
        ret = (
            num+arg if op=='+' else
            num-arg if op=='-' else
            num*arg if op=='*' else
            num//arg if op=='/' else 0
        )
        return ret if ret > 0 else 0

    dp = [1,0]  # 초기 인원 수
    # 0 이면 game over 상태임.

    for k in range(1, N+1):
        a,b = A[k-1]  # 두 개의 선택지
        prev0,prev1 = dp

        dp[0] = max(calc(prev0, a), calc(prev0, b))  # skip 안 한 경우
        dp[1] = max(
            prev0,        # 이번 단계에서 skip 하는 경우
            calc(prev1, a), calc(prev1, b),
        )
        if dp == [0,0]: break

    ans = max(dp)
    return str(ans) if ans > 0 else 'ddong game'


if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
3
+5 *2
+4 *2
-5 /2
예제 출력 1
12
예제 입력 2
3
+3 *6
-8 -9
-9 -9
예제 출력 2
ddong game

----
run=(python3 a23815.py)

echo '3\n+5 *2\n+4 *2\n-5 /2' | $run
# 12
echo '3\n+3 *6\n-8 -9\n-9 -9' | $run
# ddong game

echo '1\n+1 *3' | $run
# 3
echo '1\n+1 *3' | $run

'''

import time,os
from random import seed,randint,shuffle

def gen_worstcase_input():
    seed(time.time())
    seed(43)
    N = int(os.getenv('_N', '10'))
    A:list[tuple] = []
    ops = ['*','+','-','/','/']
    for i in range(N):
        o1,o2 = sorted([ randint(0,4), randint(0,4) ])
        op1,op2 = ops[o1],ops[o2]
        v1,v2 = randint(1,2),randint(1,2)
        A.append((f'{op1}{v1}', f'{op2}{v2}'))
    return N,A

def test():
    N,A = gen_worstcase_input()
    print(N)
    print('\n'.join( f'{a} {b}' for a,b in A ))

'''
_N=10 python3 -c "from a23815 import test; test()"

_N=10 python3 -c "from a23815 import test; test()" | time $run
# 8

_N=100 python3 -c "from a23815 import test; test()" | time $run
# 1824075
# $run  0.02s user 0.01s system 84% cpu 0.029 total

_N=1000 python3 -c "from a23815 import test; test()" | time $run
# 79452895610535337955673637701276734729789769656
# $run  0.02s user 0.01s system 84% cpu 0.031 total

_N=10000 python3 -c "from a23815 import test; test()" | time $run
# 8671....9030
# $run  0.03s user 0.01s system 65% cpu 0.055 total

'''
