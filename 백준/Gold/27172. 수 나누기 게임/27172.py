'''
27172번
수 나누기 게임

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	9947	4228	3272	40.103%

문제
《보드게임컵》을 준비하다 지친 은하는 보드게임컵 참가자들을 경기장에 몰아넣고 결투를 시키는 게임 《수 나누기 게임》을 만들었습니다.

《수 나누기 게임》의 규칙은 다음과 같습니다.

- 게임을 시작하기 전 각 플레이어는 1 부터 1,000,000 사이의 수가 적힌 서로 다른 카드를 잘 섞은 뒤 한 장씩 나눠 가집니다.
- 매 턴마다 플레이어는 다른 플레이어와 한 번씩 결투를 합니다.
- 결투는 서로의 카드를 보여주는 방식으로 진행되며, 플레이어의 카드에 적힌 수로 다른 플레이어의 카드에 적힌 수를 나눴을 때, 나머지가 0이면 승리합니다.
  플레이어의 카드에 적힌 수가 다른 플레이어의 카드에 적힌 수로 나누어 떨어지면 패배합니다.
  둘 다 아니라면 무승부입니다.
- 승리한 플레이어는 1 점을 획득하고, 패배한 플레이어는 1 점을 잃습니다. 무승부인 경우 점수의 변화가 없습니다.
- 본인을 제외한 다른 모든 플레이어와 정확히 한 번씩 결투를 하고 나면 게임이 종료됩니다.

《수 나누기 게임》의 결과를 가지고 한별이와 내기를 하던 은하는 게임이 종료되기 전에 모든 플레이어의 점수를 미리 알 수 있을지 궁금해졌습니다.
은하를 위해 각 플레이어가 가지고 있는 카드에 적힌 수가 주어졌을 때, 게임이 종료된 후의 모든 플레이어의 점수를 구해주세요.

입력
첫 번째 줄에 플레이어의 수 N이 주어집니다.
두 번째 줄에, 첫 번째 플레이어부터 N 번째 플레이어까지 각 플레이어가 가지고 있는 카드에 적힌 정수 x_{1}, ..., x_{N} 이 공백으로 구분되어 주어집니다.

출력
첫 번째 플레이어부터 N$번째 플레이어까지 게임이 종료됐을 때의 각 플레이어의 점수를 공백으로 구분하여 출력해주세요.

제한
- 2 <= N <= 100000
- 모든 1 <= i <= N 에 대해, 1 <= x_{i} <= 1000000 입니다.
- 모든 1 <= i < j <= N 에 대해, x_{i} != x_{j} 입니다. 즉, 어떤 수도 x 에서 두 번 이상 등장하지 않습니다.


---

2:55~

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    assert len(A) == N, f"wrong size {len(A)}, {N}"
    return A


MAX_VAL = 1_000_000

def solve_slow(A:list[int])->list[int]:
    '''
    '''
    N = len(A)
    indices = [-1]*(MAX_VAL+1)
    for i,a in enumerate(A):
        indices[a] = i
    A.sort()

    scores = [0]*N
    for ib in range(1, N):
        b = A[ib]
        for ia in range(ib):
            a = A[ia]
            # assert a < b
            if b % a == 0: # a wins
                scores[ia] += 1
                scores[ib] -= 1

    # re-arrange scores
    result = [0]*N
    for k in range(N):
        result[indices[A[k]]] = scores[k]
    return result



def solve_fast2(A:list[int])->list[int]:
    '''
    implement without mod(%) operation
    sort() is not used also
    '''
    N = len(A)
    mx = max(A)
    bf = [0] * (mx+1)  # boolean flag whether the index is in A
    for a in A:
        bf[a] = 1

    scores = [0] * (mx+1)
    for a in A:
        if a+a > mx:
            continue
        for b in range(a+a,mx+1,a):
            if bf[b]: # only if b is in A
                scores[b] -= 1
                scores[a] += 1

    # return re-arranged scores
    return [ scores[a] for a in A ]



if __name__ == '__main__':
    inp = get_input()
    # res = solve_slow(inp)
    res = solve_fast2(inp)
    print(' '.join(map(str, res)))




'''

예제 입력 1
3
3 4 12
예제 출력 1
1 1 -2

예제 입력 2
4
7 23 8 6
예제 출력 2
0 0 0 0

run=(python3 27172.py)

echo '3\n3 4 12' | $run
echo '4\n7 23 8 6' | $run


export _N=1000

(python3 <<EOF
import time,os
from random import seed,randint,shuffle
# seed(time.time())
seed(43)
N = int(os.getenv('_N', '10'))
print(N)
A = list(range(2,max(2+N,1000)))
shuffle(A)
print(*A[0:N])
EOF
) | time $run


N=10000
slow
->
$run  2.09s user 0.01s system 99% cpu 2.106 total


fast
$run  0.03s user 0.01s system 82% cpu 0.040 total
$run  0.03s user 0.01s system 83% cpu 0.041 total

N=100000
$run  0.15s user 0.01s system 53% cpu 0.298 total
$run  0.14s user 0.01s system 70% cpu 0.218 total
'''
