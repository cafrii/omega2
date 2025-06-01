'''
다른 해법들.

놀랍게도, pypy가 아닌 python으로 통과한 솔루션들이 존재한다!
그것도 30배 정도 빠른 경우가 있다?

https://www.acmicpc.net/source/92680603

제출번호    아이디        문제   결과        메모리    시간    언어       코드길이   제출한 시간
92680603  rightoilfe  9019  맞았습니다!!  36504   648    Python 3  1910    1달 전
94958993  cafrii      9019  맞았습니다!!  217952  16640  PyPy3     1958    6분 전 <- 내 제줄


bfs 를 사용한 것은 같은데, 여기에 dp 도 적용한 건가?

'''

import sys

def sol(start, end):
    dp = [0] * L

    def bfs():
        dp[start] = 1
        dp[end] = -1
        queue_for = [start]
        queue_rev = [end]

        for i, j in zip(range(2, 5000), range(-2, -5000, -1)):
            queue2_for = []
            for q in queue_for:
                for k in path_for[q]:
                    if not dp[k]:
                        dp[k] = i
                        queue2_for.append(k)

                    elif dp[k] < 0: return i-1, j+2, k

            queue_for = queue2_for

            queue2_rev = []
            for q in queue_rev:
                for k in path_rev[q]:
                    if not dp[k]:
                        dp[k] = j
                        queue2_rev.append(k)

                    elif dp[k] > 0: return i-1, j+1, k

            queue_rev = queue2_rev

    i, j, k = bfs()
    # 최단 경로 역추적
    answer = [None] * (i-j)

    a = k
    for b in range(i, 0, -1):
        for char, c in zip(('S', 'L', 'R', 'D', 'D'), path_rev[a]):
            if dp[c] == b:
                answer[b-1] = char
                a = c
                break

    a = k
    for b in range(j, 0):
        for char, c in zip(('S', 'L', 'R', 'D'), path_for[a]):
            if dp[c] == b:
                answer[b] = char
                a = c
                break

    return ''.join(answer)


readline = sys.stdin.readline
T = int(readline())
L = 10000
path_for = [(i-1 if i else 9999, 10*i%L + i//1000, i//10 + 1000*i%L, 2*i%L) for i in range(L)]
path_rev = [(0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000, j := i//2, j+5000)
            if i % 2 == 0 else
            (0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000) for i in range(L)]

for _ in range(T):
    A, B = map(int, readline().split())

    sys.stdout.write(sol(A, B) + '\n')
