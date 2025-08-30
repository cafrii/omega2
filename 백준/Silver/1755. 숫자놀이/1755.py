'''
1755번
숫자놀이 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	7111	4414	3883	63.949%

문제
79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다.
80은 마찬가지로 "eight zero"라고 읽는다. 79는 80보다 작지만,
영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.

문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면
M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.

입력
첫째 줄에 M과 N이 주어진다.

출력
M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.

'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

if __name__ == '__main__':
    input = sys.stdin.readline
    M,N = map(int, input().split())

    d2s = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    A = []
    for d in range(M,N+1):
        if d < 10:
            s = d2s[d]
        elif d <= 99:
            s = f'{d2s[d//10]} {d2s[d%10]}'
        else:
            s = '?'
        A.append((s, d))

    A.sort()

    BL = []
    while A:
        BL.append(A[:10])
        del A[:10]
    for b in BL:
        print(' '.join( str(d) for _,d in b ))



'''
예제 입력 1
8 28
예제 출력 1
8 9 18 15 14 19 11 17 16 13
12 10 28 25 24 21 27 26 23 22
20

---
run=(python3 1755.py)

echo '8 28' | $run
# 8 9 18 15 14 19 11 17 16 13
# 12 10 28 25 24 21 27 26 23 22
# 20

echo '8 27' | $run
# 8 9 18 15 14 19 11 17 16 13
# 12 10 25 24 21 27 26 23 22 20

echo '1 1' | $run
# 1

echo '7 10' | $run


'''

