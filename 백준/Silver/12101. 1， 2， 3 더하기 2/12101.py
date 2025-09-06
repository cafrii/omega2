'''
12101번
1, 2, 3 더하기 2 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	4835	3059	2499	63.620%

문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1

이를 사전순으로 정렬하면 다음과 같이 된다.

1+1+1+1
1+1+2
1+2+1
1+3
2+1+1
2+2
3+1

정수 n과 k가 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법 중에서 k번째로 오는 식을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n과 k가 주어진다. n은 양수이며 11보다 작고, k는 231-1보다 작거나 같은 자연수이다.

출력
n을 1, 2, 3의 합으로 나타내는 방법 중에서 사전 순으로 k번째에 오는 것을 출력한다.
k번째 오는 식이 없는 경우에는 -1을 출력한다.


------
1:57~2:23

검증 완료. 채점 완료.

'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    return N,K

def solve(N:int, K:int)->str:
    '''
    finds K-th element (1-based) in lexicographic order
    among the cases to compose N using 1, 2 or 3.
    Args:
        N: target number to compose. 1 ~ 11
        K: order to find. 1 <= K <= N
    Returns:
        answer string or '-1' if no answer
    '''

    alloc_n = max(4, N)
    dp:list[list[str]] = [ [] for j in range(alloc_n+1) ]
    # dp[j]는 정수 j를 만드는 방법에 사용되는 숫자들을 문자열 형태로 붙여 표시한 것.

    dp[1] = ['1']
    dp[2] = ['11', '2']
    dp[3] = ['111', '21', '12', '3']

    for j in range(4, N+1):
        for s in dp[j-1]: dp[j].append(s + '1')
        for s in dp[j-2]: dp[j].append(s + '2')
        for s in dp[j-3]: dp[j].append(s + '3')

    # dp[N]은 N을 만드는 방법의 문자열. 정렬 후 검색.
    a1 = sorted(dp[N])
    log("%s", a1)

    # 주의: 문제에서의 K번째는 1부터 시작하는 인덱스임.
    return '+'.join(a1[K-1]) if len(a1)>=K else '-1'


if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
4 3
예제 출력 1
1+2+1
예제 입력 2
4 5
예제 출력 2
2+1+1
예제 입력 3
4 7
예제 출력 3
3+1
예제 입력 4
4 8
예제 출력 4
-1
----

run=(python3 12101.py)

echo '4 3' | $run
# 1+2+1
echo '4 5' | $run
# 2+1+1
echo '4 7' | $run
# 3+1
echo '4 8' | $run
# -1

echo '1 1' | $run
# 1
echo '2 3' | $run
# -1
echo '3 100' | $run
# -1
echo '11 500' | $run
# 3+3+2+1+2


'''
