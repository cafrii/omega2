'''
2313번
보석 구매하기, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	1665	429	348	27.773%

문제
보석 가게에 여러 가지의 보석이 진열되어 있다.
각각의 보석은 정수로 표현되는 가치가 있다.
때로는 저주받은 보석이 있기 때문에 가치가 음수가 될 수도 있다.

보석들은 총 n개의 줄에 나열되어 있다.
이제 당신은 각각의 줄에서 몇 개의 보석을 구매하려 한다.
이때, 각 줄에서 보석을 구매할 때 연속적인 보석들을 구매해야 한다.
즉, 어느 한 줄에서 1, 2번 보석을 구매할 수도 있고, 2, 3번 보석을 구매할 수도 있지만,
1, 3번 보석을 구매할 수는 없다.

구매하는 보석의 가치의 총 합이 최대가 되도록
보석을 구매하는 방법을 찾아내는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 1,000)이 주어진다.
다음 2xn개의 줄에는 n개의 줄에 나열된 보석들에 대한 정보가 주어진다.
먼저 각 줄에 나열된 보석의 개수 L(1 ≤ L ≤ 1,000)이 주어지고,
그 다음 줄에 L개의 정수들이 주어진다.
각 정수는 각 보석의 가치를 나타낸다.
보석의 가치는 절댓값이 10,000보다 작거나 같은 정수이다.

출력
첫째 줄에 보석의 가치의 총 합의 최댓값을 출력한다.
다음 n개의 줄에는, 줄에서 몇 번째 보석부터 몇 번째 보석까지를 구매했는지를 출력한다.

만약 최대가 되는 경우가 여럿이면, 구매한 보석들의 총 개수가 최소가 되는 방법을 출력한다.
이와 같은 경우도 여럿이라면, 출력한 nx2개의 수들을 하나의 수열로 생각하여,
사전식으로 가장 앞에 오는 경우를 출력한다.

-------

9:45~10:25

아주 여러가지 문제가 복합적으로 되어 있음.
일단 각 줄에서는 부분수열 합이 최대가 되는 것을 구하면 된다. 각 라인 별로 dp 적용.
단, 단순히 최대값만 찾아서는 안되고 시작, 끝 값도 기억해 두어야 함.
동점자가 여럿인 경우는 (1) 짧은 수열 우선, (2) 왼쪽 (먼저오는) 수열 우선 을 적용한다.

'''




import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        L = int(input().rstrip())
        B = list(map(int, input().split()))
        assert len(B) == L
        A.append(B)
    return N,A

def solve(N:int, A:list[list[int]])->list[str]:
    '''
    Args:
    Returns:
    '''
    NINF = int(-1e8) # -(1_000*10_000 + 1)  # negative infinity

    def find_max_subseq(seq:list[int])->list[int]:
        '''
        Returns: [ start_idx, end_idx, max_sum ]
        '''
        n = len(seq)
        log("**** %s", seq)

        # format of dp and max_kv: [ start_idx, end_idx, max_sum ]
        # index is 0-based.

        dp = [ [k, k, v] for k,v in enumerate(seq) ]
        # 자기 자신 단독으로만 구성된 경우로 초기화
        max_kv = dp[0][:]

        for k in range(1, n): # k: 1 ~ n-1

            if dp[k-1][2] > 0:
                # 직전의 수열을 이어서 하는 것이 도움이 되는 경우임. 끝 인덱스는 현재 인덱스
                dp[k] = [dp[k-1][0], k, dp[k-1][2] + seq[k]]

            # 최대값 추척
            if dp[k][2] < max_kv[2]: continue

            if dp[k][2] > max_kv[2]:  # 새로운 최대값
                max_kv = dp[k][:] # (dp[k][0], k, dp[k][2])
                continue

            # dp[k][2] == max_kv[2]:  # 동점자인 경우.
            # 보석 개수가 최소가 되는 것을 선택
            if dp[k][1] - dp[k][0] > max_kv[1] - max_kv[0]:
                continue

            if dp[k][1] - dp[k][0] < max_kv[1] - max_kv[0]:
                max_kv = dp[k][:]

            # dp[k][1] - dp[k][0] == max_kv[1] - max_kv[0]:
            # 여전히 동점자. 사전식, 즉, 먼저 발견된 것 우선. 따라서 갱신 없이 skip
            pass

        log("==> %s", max_kv)
        return max_kv

    ans = ['']
    max_sum = 0
    for i in range(N):
        s,e,mx = find_max_subseq(A[i])
        max_sum += mx
        ans.append(f'{s+1} {e+1}')
    ans[0] = str(max_sum)
    return ans

if __name__ == '__main__':
    print('\n'.join(solve(*get_input())))


'''
예제 입력 1
2
5
30 70 -10 10 0
9
90 80 70 60 0 -60 0 60 -60
예제 출력 1
400
1 2
1 4

----
pr=2313
run=(python3 a$pr.py)

echo '2\n5\n30 70 -10 10 0\n9\n90 80 70 60 0 -60 0 60 -60' | $run
# 400
# 1 2
# 1 4


echo '1\n5\n-5 -4 -3 -2 -1' | $run
# -1
# 5 5

echo '1\n5\n1 2 3 -6 6' | $run
# 6
# 5 5

echo '1\n5\n5 1 -10 2 4' | $run
# 6
# 1 2

echo '1\n5\n5 1 -1 2 4' | $run
# 11
# 1 5

echo '1\n3\n1 1 -10' | $run
# 2
# 1 2

echo '1\n4\n2 3 -10 5' | $run
# 5
# 4 4

echo '1\n5\n-1 -2 1 -3 -4' | $run
# 1
# 3 3

echo '1\n4\n-1 -2 -3 -4' | $run


'''

