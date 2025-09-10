'''
3067번
Coins 성공, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	3725	2900	2545	79.906%

문제
우리나라 화폐단위, 특히 동전에는 1원, 5원, 10원, 50원, 100원, 500원이 있다.
이 동전들로는 모든 정수의 금액을 만들 수 있으며 그 방법도 여러 가지가 있을 수 있다.
예를 들어 30원을 만들기 위해서는 1원짜리 30개 또는 10원짜리 2개와 5원짜리 2개 등의 방법이 가능하다.

동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램을 작성하시오.

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 첫 번째 줄에는 동전의 가지 수 N(1 ≤ N ≤ 20)이 주어지고
두 번째 줄에는 N 가지 동전의 각 금액이 오름차순으로 정렬되어 주어진다.
각 금액은 정수로서 1원부터 10000원까지 있을 수 있으며 공백으로 구분된다.
세 번째 줄에는 주어진 N가지 동전으로 만들어야 할 금액 M(1 ≤ M ≤ 10000)이 주어진다.

편의를 위해 방법의 수는 2^31 - 1 보다 작다고 가정해도 된다.

출력
각 테스트 케이스에 대해 입력으로 주어지는 N가지 동전으로
금액 M을 만드는 모든 방법의 수를 한 줄에 하나씩 출력한다.

-----
10:40~

-----
N 가지 동전으로 정확히 금액 M 만들기

처음에는 0-1 배낭 문제의 특수 형태인 줄.. cost = value
그런데, 일단 특정 유형의 동전의 개수를 제한 없이 사용할 수 있으니
이건 배낭과는 다른 문제임.

그래도 배낭 문제 풀 때의 구조를 비슷하게 유지해 봄.
바깥 루프에 물건 종류 (동전 유형), 안쪽 루프에는 완성할 금액.

dp[k][j] 는 dp[k-1] 의 값들을 활용.
현재 동전을 하나 쓰는 경우, 둘 쓰는 경우, ...
dp[k][j] = dp[k-1][j-v] + dp[k-1][j-2v] + dp[k-1][j-3v] + ...

그런데 또 생각해 보면, 이전 동전 하나도 쓰지 않고, 현재 동전 만으로 구성할 수도 있음.
dp[k][j] = dp[k][j] + (1 if j%v==0 else 0)

위 두 식을 하나로 합칠 수 있는가?
간단한 몇 가지 예시를 직접 그려 보니, 밑에서 부터 쌓아 올리는 것이 낫겠다고 판단됨.

처음부터 이런 점화식을 바로 구상해 내기엔 아직 내공이 부족한 듯..

------
채점 확인 완료.

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    def gen():
        for _ in range(C):
            N = int(input().rstrip()) # number of coin types
            A = list(map(int, input().split()))
            assert len(A)==N, "wrong A"
            M = int(input().rstrip()) # goal, 1~10_000
            yield A,M
    return gen()


def solve_dp(A:list[int], M:int)->int:
    '''
    Args:
        A: coin types
        M: goal
    Returns: number of all cases to compose M using A[]-typed coins
    '''
    N = len(A) # sorted by ascending order
    dp = [0] * (M+1)
    # dp[k]: number of cases to compose value k

    dp[0] = 1
    for cv in A: # for each coin value
        for j in range(cv, M+1):
            dp[j] += dp[j-cv]
    return dp[M]

if __name__ == '__main__':
    it = get_input()
    print('\n'.join(map(str, (solve_dp(a,m) for a,m in it) )))


'''

예제 입력 1
3
2
1 2
1000
3
1 5 10
100
2
5 7
22
예제 출력 1
501
121
1
-------

run=(python3 3067.py)

echo '3\n2\n1 2\n1000\n3\n1 5 10\n100\n2\n5 7\n22' | $run
# 501
# 121
# 1

echo '1\n3\n1 5 10\n100' | $run
# 121
echo '1\n2\n2 3\n10' | $run
# 2

'''
