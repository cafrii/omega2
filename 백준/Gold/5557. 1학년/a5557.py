'''
5557번
1학년, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	22769	11034	8700	48.557%

문제
상근이가 1학년 때, 덧셈, 뺄셈을 매우 좋아했다.
상근이는 숫자가 줄 지어있는 것을 보기만 하면, 마지막 두 숫자 사이에 '='을 넣고,
나머지 숫자 사이에는 '+' 또는 '-'를 넣어 등식을 만들며 놀고 있다.
예를 들어, "8 3 2 4 8 7 2 4 0 8 8"에서 등식 "8+3-2-4+8-7-2-4-0+8=8"을 만들 수 있다.

상근이는 올바른 등식을 만들려고 한다. 상근이는 아직 학교에서 음수를 배우지 않았고, 20을 넘는 수는 모른다.
따라서, 왼쪽부터 계산할 때, 중간에 나오는 수가 모두 0 이상 20 이하이어야 한다.
예를 들어, "8+3+2-4-8-7+2+4+0+8=8"은 올바른 등식이지만, 8+3+2-4-8-7이 음수이기 때문에, 상근이가 만들 수 없는 등식이다.

숫자가 주어졌을 때, 상근이가 만들 수 있는 올바른 등식의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N이 주어진다. (3 ≤ N ≤ 100)
둘째 줄에는 0 이상 9 이하의 정수 N개가 공백으로 구분해 주어진다.

출력
첫째 줄에 상근이가 만들 수 있는 올바른 등식의 개수를 출력한다. 이 값은 2^63 - 1 이하이다.

----

8:46~

---
그냥 간단한 dp로 해결 될 듯?

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    assert len(A) == N
    return N,A

def solve(N:int, A:list[int])->int:
    '''
    Args:
        N: length of array A
        A: list of numbers of length N.
            last number is what we should make by composing numbers.
    Returns:
        number of valid expressions possible
    Logic:
        A[0] 부터 A[N-1] 까지의 총 N개의 배열이 주어지는데
        사실 A[N-2] 까지가 조합(수식)에 사용할 수 있는 숫자들이고
        마지막 A[N-1]은 만들어야 하는 타겟 목표이다.
        따라서 dp는 입력 A에 맞게 0부터 N-2 까지만 돌리고,
        dp[N-2][] 중에서 목표 A[N-1]에 해당하는 것을 택하면 정답이 된다.
    '''

    dp = [ [0]*21 for _ in range(N) ]

    dp[0][A[0]] = 1

    for k in range(1, N-1): # k: 1 ~ N-2
        # dp[k][j] 를 만드는 방법은 dp[k-1][i]에 A[k]를 + 또는 - 연산을 수행.

        for i in range(0, 21): # i: 0~20
            if dp[k-1][i] == 0: continue
            if i+A[k] <= 20:
                dp[k][i+A[k]] += dp[k-1][i]
            if i-A[k] >= 0:
                dp[k][i-A[k]] += dp[k-1][i]

    return dp[N-2][A[N-1]]


if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
11
8 3 2 4 8 7 2 4 0 8 8
예제 출력 1
10
예제 입력 2
40
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1
예제 출력 2
7069052760

----
run=(python3 a5557.py)

echo '11\n8 3 2 4 8 7 2 4 0 8 8' | $run
# 10

echo '40\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1' | $run
# 7069052760

echo '3\n1 2 3' | $run
# 1


'''


