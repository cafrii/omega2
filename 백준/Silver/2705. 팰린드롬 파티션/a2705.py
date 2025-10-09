'''
2705번
팰린드롬 파티션, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	1519	950	710	66.604%

문제
양의 정수 N의 파티션은 합이 N이 되는 수열을 말한다. 보통 숫자 사이에 +를 넣어서 나타낸다. 예를 들면

15 = 1+2+3+4+5 = 1+2+1+7+1+2+1 이다.

어떤 파티션을 앞에서 읽을 때와 뒤에서 읽을 때가 같으면 이 파티션을 팰린드롬 파티션이라고 한다.
위의 예에서 첫 번째 파티션은 팰린드롬 파티션이 아니지만, 두 번째 파티션은 팰린드롬 파티션이다.

어떤 파티션이 m개의 정수로 이루어져 있다면,
왼쪽 절반은 처음 floor(m/2)개의 원소, 오른쪽 절반은 마지막 floor(m/2)개의 원소이다.

재귀적인 팰린드롬 파티션은 어떤 파티션이 팰린드롬이면서,
왼쪽 절반과 오른쪽 절반이 재귀적인 팰린드롬이거나, 비어있을 때 이다.
모든 정수는 적어도 2개의 재귀적인 팰린드롬 파티션을 항상 갖는다. (n과, 1 n개)

7의 재귀적인 팰린드롬 파티션은 다음과 같이 6가지가 있다.

7, 1+5+1, 2+3+2, 1+1+3+1+1, 3+1+3, 1+1+1+1+1+1+1

어떤 수 N을 입력받은 다음에, 재귀적인 팰린드롬 파티션의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T(1 <= T <= 1,000)가 주어진다.
각 테스트 케이스는 양의 정수 1개로 이루어져있고, 이 수가 문제에서 설명한 N이고, 1,000보다 작거나 같다.

출력
각 테스트 케이스에 대해 한 줄에 하나씩 N의 재귀적인 팰린드롬 파티션의 개수를 출력한다.

----
9:45~

----
recursive dp 로 계산
제출, 검증 완료

'''


#def log(fmt, *args): print(fmt % args, file=sys.stderr)
log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)


def get_input():
    import sys
    input = sys.stdin.readline
    T = int(input().rstrip())
    A = []
    for _ in range(T):
        A.append(int(input().rstrip()))
    return A,

def solve(A:list[int])->list[int]:
    '''
    Args:
        A: list of N, to be solved against. 1<=N<=1000
    Returns:
        answer list.
        answer: number of recursive palindromes on number N
    '''
    # recursion depth:
    # max N is 1000 -> log_2(1000) = log 1000/log 2 ~= 10

    max_n = max(A)
    dp = [0] * (max_n+1)
    # dp[k]는 숫자 k의 재귀적인 팰린드롬 파티션의 개수

    # 미리 계산된 몇 개의 답
    dp[1] = 1  # 1
    dp[2] = 2  # 1+1, 2
    dp[3] = 2  # 1+1+1, 3
    dp[4] = 4  # 1+1+1+1, 2+2, 1+2+1, 4
    # dp[5] = 4  # 1+1+1+1+1, 2+1+2, 1+3+1, 5
    # dp[6] = 6  # 1+1+1+1+1+1, 3+3, 1+1+2+1+1, 2+2+2, 1+4+1, 6
    # dp[7] = 6  # 1+1+1+1+1+1+1, 3+1+3, 1+1+3+1+1, 2+3+2, 1+5+1, 7

    def dfs(N:int)->int:
        if N <= 0: return 0
        if dp[N] > 0: return dp[N]
        # <side> [<center>] <side> 형태
        # center 는 side 값에 따라서 없을 수도 있음.
        # side 가 0 인 경우는 N 단독인 경우와 같음.
        # side 값을 1부터 키워가며 찾음.
        num = 1   # N 단독.
        for side in range(1, N//2 + 1): # side: 1 ~ N//2
            num += dfs(side)
        dp[N] = num
        return num

    ans = []
    for n in A:
        ans.append(dfs(n))
    return ans

if __name__ == '__main__':
    # ans = solve(*get_input())
    # for a in ans:
    #     print(a)

    print('\n'.join(map(str, solve(*get_input()))))


'''
예제 입력 1
3
4
7
20
예제 출력 1
4
6
60
----

run=(python3 a2705.py)


echo '3\n4\n7\n20' | $run
# 4
# 6
# 60

echo '1\n5' | $run



'''

