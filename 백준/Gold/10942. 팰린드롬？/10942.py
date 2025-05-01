'''
10942

팰린드롬? 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초 (하단 참고)	256 MB	67751	21194	14419	30.629%

문제

명우는 홍준이와 함께 팰린드롬 놀이를 해보려고 한다.

먼저, 홍준이는 자연수 N개를 칠판에 적는다. 그 다음, 명우에게 질문을 총 M번 한다.

각 질문은 두 정수 S와 E(1 ≤ S ≤ E ≤ N)로 나타낼 수 있으며, S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지를 물어보며,
명우는 각 질문에 대해 팰린드롬이다 또는 아니다를 말해야 한다.

예를 들어, 홍준이가 칠판에 적은 수가 1, 2, 1, 3, 1, 2, 1라고 하자.

S = 1, E = 3인 경우 1, 2, 1은 팰린드롬이다.
S = 2, E = 5인 경우 2, 1, 3, 1은 팰린드롬이 아니다.
S = 3, E = 3인 경우 1은 팰린드롬이다.
S = 5, E = 7인 경우 1, 2, 1은 팰린드롬이다.

자연수 N개와 질문 M개가 모두 주어졌을 때, 명우의 대답을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열의 크기 N (1 ≤ N ≤ 2,000)이 주어진다.

둘째 줄에는 홍준이가 칠판에 적은 수 N개가 순서대로 주어진다. 칠판에 적은 수는 100,000보다 작거나 같은 자연수이다.

셋째 줄에는 홍준이가 한 질문의 개수 M (1 ≤ M ≤ 1,000,000)이 주어진다.

넷째 줄부터 M개의 줄에는 홍준이가 명우에게 한 질문 S와 E가 한 줄에 하나씩 주어진다.

출력
총 M개의 줄에 걸쳐 홍준이의 질문에 대한 명우의 답을 입력으로 주어진 순서에 따라서 출력한다. 팰린드롬인 경우에는 1, 아닌 경우에는 0을 출력한다.

'''

import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

MAX_LEN_N = 2000

# answer matrix
# A[j][k]: Ns[j:k+1] 이 팰린드롬이면 1
#
A = [ [0]*MAX_LEN_N for k in range(MAX_LEN_N) ]


def solve(N:list[int]):
    '''
    2000x2000 크기의 정답 표를 미리 만들어 두도록 하자.
    Returns ...
    '''
    len_n = len(N)
    for k in range(len_n):
        # log('k = %d', k)
        A[k][k] = 1
        # k가 center 인 홀수 길이의 팰린드롬 모두 검사
        for j in range(1, min(k, len_n-1-k)+1):
            if N[k-j] != N[k+j]:
                break
            A[k-j][k+j] = 1
            # log('odd  (%d ~ %d), %s', k-j, k+j, N[k-j:k+j+1])
        # N[k:k+2] 부터 커져가는 짝수 길이의 팰린드롬 검사
        for j in range(0, len_n):
            if k-j < 0 or len_n <= k+1+j:
                break
            if N[k-j] != N[k+1+j]:
                break
            A[k-j][k+1+j] = 1
            # log('even (%d ~ %d), %s', k-j, k+1+j, N[k-j:k+1+j])

    return A


_ = int(input().strip())
Ns = list(map(int, input().split()))

ans = solve(Ns)

M = int(input().strip())
# SE = []
for _ in range(M):
    s,e = map(int, input().split())
    print(ans[s-1][e-1])



'''
예제 입력 1
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7

예제 출력 1
1
0
1
1


echo '7\n1 2 1 3 1 2 1\n4\n1 3\n2 5\n3 3\n5 7' | python3 10942.py
-> 1 0 1 1

echo '3\n1 0 1\n1\n1 3' | python3 10942.py
-> 1




(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,M = 2000,1_000_000
# N,M = 20,1
print(N)
print(' '.join([ str(randint(1,10)) for k in range(N) ]))
print(M)
for _ in range(M):
    s,e = randint(1,N),randint(1,N)
    if s>e: s,e = e,s
    print(s,e)
EOF
) | time python3 10942.py > /dev/null
/dev/ttys051

'''
