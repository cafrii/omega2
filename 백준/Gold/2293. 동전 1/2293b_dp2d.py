'''

dp 로 도전.
마땅히 생각이 안나서, recursive 로 먼저 시도해 보니 중복 계산들이 보임.
그 중복되는 부분들을 memoization 으로 최적화.
그러다 보니 2차원 dp가 되었음.

하지만, 이렇게 해도 별로 빨라지지 않았음. 아래 처럼 N=6, K=10000 으로 해도 벌써 시간 초과.

echo '6 10000\n1\n2\n5\n7\n11\n13' | time $run 2> /dev/null
# $run 2> /dev/null  6.49s user 0.05s system 99% cpu 6.567 total

이 버전은 제출하지 않음.


'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input().rstrip()))
    return A,K



def solve_dp_recursive(A:list[int], K:int)->int:
    '''
    Args:
        A[]: list of unit price of each coin
        K: target value which we will compose using coins.
    Returns:
        the number of cases we can compose K using any number of provided coins.

    Algo:
        fix each coin counts one by one, controlling target value.
        use recursive call with some memoization

    '''

    MAX_K = 10_000
    INF = int(2**31)

    A.sort(reverse=True) # bigger coin first
    N = len(A)

    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, N+20))

    dp = [ [INF]*(MAX_K+1) for n in range(N) ]
    # dp[n][k]: n 번째 까지의 동전을 사용하여 k 를 만들어내는 경우의 수

    for n in range(N):
        dp[n][0] = 1  # 0을 만드는 경우의 수는 항상 1. (모든 동전을 사용하지 않는 것)

    def get_count(coin_id:int, ksum:int)->int:
        '''
            coin_id: 사용할 동전의 종류. 0 ~ len(A)-1
        '''
        if not (0<=coin_id<N and ksum<=MAX_K): return 0
        if dp[coin_id][ksum] < INF:
            # log("        use saved dp[%d][%d] %d", coin_id, ksum, dp[coin_id][ksum])
            return dp[coin_id][ksum]

        cnt = 0
        if coin_id == N-1: # 한 종류만 남음
            if ksum % A[coin_id] == 0:
                cnt = 1
        else:
            for j in range(ksum // A[coin_id], -1, -1):
                # coin_id 동전을 j 개 사용하는 경우.
                # A[coin_id] * j 만큼 줄어든 새 target 으로 다음 단계 호출.
                cnt += get_count(coin_id+1, ksum - A[coin_id]*j)
                # 다음 단계의 모든 경우의 수 총합이 이 단계에서의 경우의 수

        dp[coin_id][ksum] = cnt
        log(" dp[%d][%d] = %d", coin_id, ksum, cnt)
        return cnt

    return get_count(0, K)


if __name__ == '__main__':
    inp = get_input()
    r = solve_dp_recursive(*inp)
    print(r)



'''
예제 입력 1
3 10
1
2
5
예제 출력 1
10



----
run=(python3 2293b_dp2d.py)

echo '3 10\n1\n2\n5' | $run
# -> 10

echo '3 100\n1\n2\n5' | $run
# 541

echo '4 100\n1\n2\n5\n10' | $run
# 2156


echo '8 100\n1\n2\n5\n7\n11\n13\n17\n19' | $run
# 51777

echo '6 10000\n1\n2\n5\n7\n11\n13' | $run
#

echo '7 10000\n1\n2\n5\n7\n11\n13\n17' | $run
#

echo '8 10000\n1\n2\n5\n7\n11\n13\n17\n19' | $run
#


echo '100 10000\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31\n32\n33\n34\n35\n36\n37\n38\n39\n40\n41\n42\n43\n44\n45\n46\n47\n48\n49\n50\n51\n52\n53\n54\n55\n56\n57\n58\n59\n60\n61\n62\n63\n64\n65\n66\n67\n68\n69\n70\n71\n72\n73\n74\n75\n76\n77\n78\n79\n80\n81\n82\n83\n84\n85\n86\n87\n88\n89\n90\n91\n92\n93\n94\n95\n96\n97\n98\n99\n100' | time $run


'''


