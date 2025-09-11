'''
12026번
BOJ 거리 성공 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	4395	2677	2203	62.355%

문제
BOJ 거리는 보도블록 N개가 일렬로 놓여진 형태의 도로이다. 도로의 보도블록은 1번부터 N번까지 번호가 매겨져 있다.

스타트의 집은 1번에 있고, 링크의 집은 N번에 있다. 스타트는 링크를 만나기 위해서 점프해가려고 한다.

BOJ거리의 각 보도블록에는 B, O, J 중에 하나가 쓰여 있다. 1번은 반드시 B이다.

스타트는 점프를 통해서 다른 보도블록으로 이동할 수 있다.
이때, 항상 번호가 증가하는 방향으로 점프를 해야 한다.
만약, 스타트가 현재 있는 곳이 i번이라면, i+1번부터 N번까지로 점프를 할 수 있다.
한 번 k칸 만큼 점프를 하는데 필요한 에너지의 양은 k*k이다.

스타트는 BOJ를 외치면서 링크를 만나러 가려고 한다.
따라서, 스타트는 B, O, J, B, O, J, B, O, J, ... 순서로 보도블록을 밟으면서 점프를 할 것이다.

스타트가 링크를 만나는데 필요한 에너지 양의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 1 ≤ N ≤ 1,000이 주어진다.
둘째 줄에는 보도블록에 쓰여 있는 글자가 1번부터 순서대로 주어진다.

출력
스타트가 링크를 만나는데 필요한 에너지 양의 최솟값을 출력한다.
만약, 스타트가 링크를 만날 수 없는 경우에는 -1을 출력한다.

----
9/11, 9:42~10:30

----
1차원 dp. forward update


'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = input().rstrip() # block name. one of 'B','O','J'
    assert len(A) == N
    return N,A

def solve(N:int, A:str)->int:
    '''
    '''
    dp = [-1]*N
    label = 'BOJ'
    dp[0] = 0

    def find_next(sub:str, cur:int):
        j = A.find(sub, cur+1, N) # j cannot be 0 if found
        return j if j>0 else 0  # 0 means 'not-found'

    def update_dp(k:int, j:int): # jump from k to j (k < j)
        new = dp[k] + (j-k)*(j-k)
        if dp[j] < 0: dp[j] = new
        else: dp[j] = min(dp[j], new)

    for k in range(N):
        if dp[k] < 0: continue
        cur = A[k]
        nxt = label[(label.index(cur) + 1) % 3]
        # log("k %d, %s > %s", k, cur, nxt)

        j = k
        while j := find_next(nxt, j):
            update_dp(k, j)

        # log("k %d, %s > %s, dp %s", k, cur, nxt, dp)


    return dp[N-1]


if __name__ == '__main__':
    # r = solve(*get_input())
    # print(r)
    print(solve(*get_input()))


'''

예제 입력 1
9
BOJBOJBOJ
예제 출력 1
8
예제 입력 2
9
BOJBOJBOJ
예제 출력 2
8
예제 입력 3
8
BJJOOOBB
예제 출력 3
-1
예제 입력 4
13
BJBBJOOOJJJJB
예제 출력 4
50
예제 입력 5
2
BO
예제 출력 5
1
예제 입력 6
15
BJBOJOJOOJOBOOO
예제 출력 6
52

----
run=(python3 12026.py)

echo '9\nBOJBOJBOJ' | $run
# 8
echo '8\nBJJOOOBB' | $run
# -1
echo '13\nBJBBJOOOJJJJB' | $run
# 50
echo '2\nBO' | $run
# 1
echo '15\nBJBOJOJOOJOBOOO' | $run
# 52

echo '1\nB' | $run
# 0

(python3 <<EOF
N = 1000
label='BOJ'
A = ''.join( label[k%3] for k in range(N) )
print(N); print(A)
EOF
) | time $run


'''
