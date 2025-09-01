'''
2591번
숫자카드 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	7593	2505	1770	31.789%

문제
1부터 34까지 수가 적힌 카드가 충분히 많이 있다.
이들 중 몇 장을 일렬로 늘어놓고, 그 숫자를 차례로 적었다.
예를 들어 아래와 같이 카드가 놓인 경우 숫자를 차례로 적으면 27123이 된다.
2   7   12  3

나중에, 적어 놓은 것에 맞게 다시 카드를 늘어놓으려고 보니, 방법이 여러 가지일 수 있다는 것을 알았다.
예를 들어 27123의 경우 아래와 같이 여섯 가지 다른 방법이 있다.
27  1   23
27  12  3
2   7   1   23
2   7   12  3
27  1   2   3
2   7   1   2   3

카드의 숫자를 차례로 적어 놓은 것이 주어질 때, 위와 같이 그것을 가지고 거꾸로 카드의 배열을 찾으려고 한다.
가능한 카드의 배열이 모두 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫 줄에 카드의 숫자를 차례로 적어 놓은 것이 주어지며, 이것은 최대 40자 이하의 숫자로 이루어진다.

출력
첫 줄에 가능한 카드 배열이 몇 개인지를 출력한다.

----

9:59~10:28

간단한 1차원 dp 문제.

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    A = input().rstrip()
    return A,  # return as tuple[str]

def solve(A:str):
    '''
    Args:
        A: list of digits, max len(A) 40
    Returns:
        number of possible method that compose the digits using card 1~34
    '''
    N = len(A) # number of digits
    dp = [0] * (N+1)
    # dp[k] 는 첫 k개의 숫자 (A[:k], 즉 A[0]~A[k-1]) 를 생성하는 조합 경우의 수

    dp[0] = 1

    for k in range(1, N+1):
        # dp[k] 는 첫 k개의 숫자 (A[:k], 즉 A[0]~A[k-1]) 를 생성하는 조합 경우의 수
        # 1. A[:k-1] 로 만든 경우의 수에 A[k-1]을 추가 고려하는 경우
        # 2. A[:k-2] 로 만든 경우의 수에 A[k-2],A[k-1] 을 추가 고려하는 경우
        msg = []
        n1 = int(A[k-1]) if k >= 1 else 0
        n2 = int(A[k-2:k]) if k >= 2 else 0
        if 1 <= n1 <= 9:
            dp[k] += dp[k-1]
            msg.append(f"+{dp[k-1]}({n1})")
        if 10 <= n2 <= 34:
            dp[k] += dp[k-2]
            msg.append(f"++{dp[k-2]}({n2})")

        log("dp[%d]: %s -> %d", k, ' '.join(msg), dp[k])

    return dp[N]

if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
27123
예제 출력 1
6

----

run=(python3 2591.py)

echo '27123' | $run
#

'''
