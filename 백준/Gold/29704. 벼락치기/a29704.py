'''
29704번
벼락치기 성공, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	950	620	517	70.054%

문제
숙명여자대학교의 알고리즘 학회 ALGOS에 합격한 혜민이는 너무 기뻐 마음이 들뜬 나머지 프로그래밍 과제가 있는 것을 잊어버리고 말았다.
프로그래밍 과제로는 다양한 난이도의 문제 $N$개가 주어지고, 앞으로 $T$일의 제출 기한이 남아있다.
만약 제출 기한 내에 문제를 제출 못 하면, 제출하지 못한 문제마다 정해져 있는 벌금을 내야 한다.
혜민이는 벌금을 내고 싶지 않기 때문에, 내는 벌금의 총금액이 가능한 한 적어지도록 문제를 풀려고 한다.

문제를 해결하는 데 소요되는 일수와 그 문제를 제출 기한 내에 해결하지 못할 경우 내야 하는 벌금이 주어질 때,
혜민이가 내야 하는 벌금의 최소 금액을 구해보자.
제출 기한 $T$일이 지났을 때, 제출하지 못한 문제별 벌금의 합이 혜민이가 최종적으로 내야 하는 벌금이다.
단, 혜민이는 아직 프로그래밍에 익숙하지 않아서 한 번에 한 개의 문제만 해결할 수 있다.

해결하는 데 소요되는 일수	벌금
문제1	2	5000
문제2	1	1000
문제3	1	2000

예를 들어, 프로그래밍 과제로 위와 같이 $3$개의 문제가 주어졌다고 가정해 보자.
제출 기한이 $3$일 남았다면, 첫째 날에 $3$번 문제를 해결하고, 둘째 날과 셋째 날에 걸쳐 $1$번 문제를 해결하면
$2$번 문제의 벌금인 $1,000$원만 내면 된다.

혜민이가 가능한 한 적은 벌금을 낼 수 있게 도와주자.

입력
첫째 줄에 문제의 개수 $N(1 <= N <= 1,000)$과 남은 제출 기한 $T(1 <= T <= 1,000)$가 주어진다.

둘째 줄부터 $N$개의 줄에 걸쳐 $i$번 문제를 푸는 데 걸리는 일수 $d_i$$(1 <= d_i <= 1,000)$와
해당 문제의 벌금 $m_i$$(1 <= m_i <= 5,000)$이 주어진다.

출력
최종적으로 내는 벌금이 최소가 되도록 문제를 풀었을 때, 혜민이가 내야 하는 벌금을 출력한다.

만약, 기한 내에 모든 문제를 해결할 수 있다면 $0$을 출력한다.

----
9/30, 7:11~7:52

----
0-1 배낭 문제의 거의 유사하다.

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,T = map(int, input().split())
    A = []
    for _ in range(N):
        d,m = map(int, input().split())
        A.append((d, m)) # (days, penalty)
    return N,T,A

def solve(N:int, T:int, A:list[tuple[int,int]])->int:
    '''
    Args:
        T: allowed days
        A: [ (days, penalty), ...]
    Returns:

    Logic:
        풀 수 있는 문제들의 벌금의 합을 구하고 이 값이 최대가 되도록 한다. 전체 벌금에서 피할 수 있는 최대 벌금을 빼면 최소 벌금이 된다.
        이렇게 하면 01 배낭 문제와 같은 형태가 됨.
        배낭 크기 (허용 가능한 무게) == 날 수
        물건의 가치 == 피할 수 있는 벌금
    '''
    total_value = sum(t[1] for t in A)
    log("T %d, sum val %d", T, total_value)

    dp = [0] * (T+1)
    # dp[t]는 t라는 시간(날짜)가 주어졌을 때 얻을 수 있는 최대 가치(벌금)의 합.

    for c,v in A:  # cost and value
        # 선택한 항목의 cost의 총 합은 T보다 같거나 작아야 함.
        # 선택한 항목의 value 가 최대가 되어야 함.
        # 이 문제를 풀기로 선택한다면, c 만큼의 비용을 들이고(c days를 소비하고), v 만큼의 이득을 얻음(v 만큼의 벌금을 회피)
        # 기존 조건 보다 더 나은 조건이라면 이것을 채택함.
        log("cost %d, value %d", c, v)
        dpx = dp.copy()  # dp for next
        for t in range(c, T+1):  # t: c ~ T
            # 선택한 경우:      dp[t-c] + v
            # 선택 안하는 경우:  dp[t]
            if dp[t-c] + v > dp[t]:
                dpx[t] = dp[t-c] + v
        dp = dpx
        log("dp: %s", dp)

    # 제출 기한을 꼭 다 채워야 하는 것은 아니므로, 전체 dp 중에서 최대 값을 찾는다.
    return total_value - max(dp)



def solve2(N:int, T:int, A:list[tuple[int,int]])->int:
    '''
    Args:
        T: allowed days
        A: [ (days, penalty), ...]
    Returns:

    Logic:
        solve()에서 좀 더 최적화.
        dp, dpx 두 벌 대신 dp 한 벌만 관리.
        t iteration 방향을 역방향으로 하면 됨.
    '''
    total_penalty = sum(t[1] for t in A)
    # log("T %d, sum val %d", T, total_penalty)

    dp = [0] * (T+1)
    # dp[t]는 t라는 시간(날짜)가 주어졌을 때 얻을 수 있는 최대 가치(벌금)의 합.

    for c,v in A:  # cost and value

        for t in range(T, c-1, -1):
            # if dp[t-c] + v > dp[t]:
            #     dp[t] = dp[t-c] + v
            dp[t] = max(dp[t], dp[t-c]+v)


    # 제출 기한을 꼭 다 채워야 하는 것은 아니므로, 전체 dp 중에서 최대 값을 찾는다.
    return total_penalty - max(dp)



if __name__ == '__main__':
    # print(solve(*get_input()))
    print(solve2(*get_input()))


'''
예제 입력 1
3 3
2 5000
1 1000
1 2000
예제 출력 1
1000
예제 입력 2
4 5
2 5000
2 2000
2 3000
3 1000
예제 출력 2
3000
예제 입력 3
3 6
1 1000
2 4000
3 2000
예제 출력 3
0
----
run=(python3 a29704.py)

echo '3 3\n2 5000\n1 1000\n1 2000' | $run
# 1000
echo '4 5\n2 5000\n2 2000\n2 3000\n3 1000' | $run
# 3000
echo '3 6\n1 1000\n2 4000\n3 2000' | $run
# 0


'''

