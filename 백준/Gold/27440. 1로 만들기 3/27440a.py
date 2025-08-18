'''

너무 느려서 실패


'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N

def solve_fail(N:int):
    '''
    거꾸로 1에서부터 N에 도달하기 위한 최소 연산 회수 세기
        op1: +1
        op2: x2
        op3: x3
    '''
    min_op_count = 1000
    moc_updated = 0

    lm = sys.getrecursionlimit()
    log("recursion limit: %d", lm)
    sys.setrecursionlimit(max(lm, min_op_count+50))


    def back(num:int, ops:str):
        nonlocal min_op_count, moc_updated
        if num == N:
            min_op_count = min(min_op_count, len(ops))
            moc_updated += 1
            log("ops: %s", ops)
            return True
        if num > N: return False # 실패!
        if len(ops) >= min_op_count: # pruning
            return False  # 더 짧은 성공 case가 있으니 시도하는 게 무의미함.

        back(num*3, ops + '3')
        back(num*2, ops + '2')
        back(num+1, ops + '1')

    back(1, '')

    return min_op_count



if __name__ == '__main__':
    print(solve_fail(get_input()))


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
$run  1.84s user 0.13s system 99% cpu 1.982 total


'''

