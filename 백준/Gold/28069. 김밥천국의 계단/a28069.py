'''
김밥천국의 계단, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	2749	833	655	29.678%

문제
민희는 미니김밥이 유명한 천국에 가려고 합니다.

천국 문 앞에는 무한히 많은 계단이 있고 가장 아래 계단의 번호가 0번이며, 위로 올라가면서 순서대로 번호가 붙어있습니다.
그중 $N$번째 계단 옆에 김밥 가게가 있습니다.

민희는 매번 다음의 2가지 행동 중 하나를 선택해서 총 $K$번 행동할 수 있으며,
정확히 $K$번째 행동에서 $N$번째 계단에 도달하면 미니김밥을 먹을 수 있습니다.

1. 계단 한 칸을 올라갑니다.

2. 민희가 집에서 가지고 온 지팡이를 계단에 두드립니다.
만약 민희가 i 번째 계단에서 지팡이를 두드리면 i + ⌊ i/2 ⌋ 번째 계단으로 순간이동합니다.
현재 민희는 0번째 계단에 있습니다. 민희가 미니김밥을 먹을 수 있을지 구해 봅시다.

입력
첫 번째 줄에 계단 개수에 해당하는 N, 계단을 오르는 횟수 K가 주어진다.
(1 <= N, K <= 1,000,000)

출력
민희가 N개의 계단을 K번 만에 올라 미니김밥을 먹을 수 있으면 minigimbob 을, 그러지 못해 물만 마신다면 water 을 출력한다.


----
## 사고 과정

간단해 보이는데 왜 골드 레벨?

그냥 dp 배열 잡고, N에 도달할 때 까지 계속 업데이트 해 보면 되지 않나?
그런데 N, K 값의 범위가 꽤 크다. 최대 백만.
한 루프 마다 노드 수가 두 배씩 커진다. (겹치는 것 제외)
노드 수 관리는 어려우니, 각 루프 마다 최대, 최소범위를 잡고 그 범위 내에서만 dp 업데이트를 하자.

확인된 문제점:
최소 step으로 가야 하는 것이 목표가 아니고, 지정한 K step을 정확히 맞춰야 한다.
따라서, 각 dp 단계에서 min, max 등을 마음대로 선택하여 택일 할 수 없다!
가능한 모든 노드를 다 기억해야만 한다!

계속 지팡이를 두드린다면 위치 이동은?
0 1 2 3 4 6 9 13 19 28 42 63 94 141 211 316 474 711 1066 1599 2398 3597 5395 8092 12138 18207 27310 40965 61447 92170 138255 207382 311073 466609 699913 1049869
총 32번 만에 넘어감.
한 스텝 마다 노드 수는 두배. 최소 총 노드는 2^32. 비현실적. 다른 방법 찾아보자.

i + i//2 가 정수로 딱 떨어지는 수는 몇 개 안될 듯.
목적지에서부터 거꾸로 내려온다.
이것도 마찬가지로 경우의 수 관리가 안됨. (하지만 나중에는 결국 이 아이디어 사용하게 됨)

역시 골드 레벨이 맞는 듯.

이것은 동전 문제와도 비슷해 보이는 듯.
두 종류의 동전이 주어지고, 동전은 무한대로 사용 가능. 정확히 K개 동전을 사용하여 N을 맞추면 된다.
동전 한 종류는 1원 짜리. 그런데 나머지 한 동전은 그 값어치가 고정되지 않고, 현재 총 가치의 함수로 주어진다.
이건 동전을 언제 사용할 것인지에 따라 가치가 달라진다??
아.. 쉽지 않네.

inner loop 의 iteration 범위를 최적화 하기 위해 mn, mx 를 관리하는 아이디어를 적용해도
별로 나아지지 않은 이유는, 이 dp 배열이 굉장히 sparse 하기 때문임.
특히 초반에 N 값이 클 때, 66% 지점 이동을 하면 그 사이가 많이 비어있음.

array 대신 dict 나 set 이용해 보자.
특정 단계는 직전 단계의 dp 만 참조하므로, on/off 정보만 저장하면 됨. set 이면 충분.

결과: 성공.

'''

import sys


def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    return N,K


# 여기서 나누기 연산이 꽤 많이 사용되는데, 다행히 병목 지점은 아닌 듯.
def find_prev(n:int)->int:
    '''
    find i, which i + (i//2) == n
    return -1 if not exist
    '''
    f,i = n/3,n//3
    if f == i:
        return i*2
    i = int(f*2)
    # there are two canidates: i, i+1
    if i + i//2 == n: return i
    if (i+1) + (i+1)//2 == n: return i+1
    return -1


def solve(N:int, K:int)->str:
    '''
    using plain dp
        역방향 탐색.
        inner loop의 min, max 범위 추적 최적화.
    결과:
        timeout 실패 예상.
        미제출.
    Args:
        N: target goal
        K: allowed steps
    Returns:
        str
    '''

    dp = [-1] * (N+1)
    dp[N] = 0
    mn,mx = N,N

    for k in range(1, K+1):
        mn2 = mx  # next mn value
        for n in range(mx, mn-1, -1):
            if dp[n] != k-1: continue
            nx1, nx2 = n-1, find_prev(n)
            if nx1 >= 0:
                dp[nx1] = k
                mn2 = min(mn2, nx1)
            if nx2 >= 0:
                dp[nx2] = k
                mn2 = min(mn2, nx2)
        mn,mx = mn2, mx-1
        # log("k %3d, (%d~%d): dp %s", k, mn,mx, dp)

    # dp[0]에 K번째 도달 가능 여부 정보가 저장되어 있음
    return 'minigimbob' if dp[0] > 0 else 'water'



def solve2(N:int, K:int)->str:
    '''
    추가 개선:
        mn 값을 추적하지 않음. 내부 루프는 항상 mx 부터 0 까지 순회.
        범위 최소값 mn 을 추적하기 위한 overhead 가
        inner loop를 0 부터가 아닌 mn 부터 시작함으로써 얻는 이득보다 더 클 것이라는 가정임.
    결과:
        몇 개의 샘플 입력에 대해 측정해 보면, solve() 대비 약간 개선은 된 듯 하지만 큰 차이는 없음.
        모든 입력에 대해 다 그렇다는 보장도 없음.
        다만, 코드는 solve() 보다 약간 더 간단해 지긴 했음.

        # 3.369 <- solve()에서 dpx mem alloc 하지 않도록 개선한 버전
        # 3.182 <- solve2() 사용
    결과
        N,K 가 100000 에서는 종료를 못함 (timeout!)
        더 개선이 필요해 보임.
    '''

    dp = [-1] * (N+1)
    dp[N] = 0
    mx = N  # inner loop range 의 최대값은 계속 추적함. 관리가 쉽기 때문.

    for k in range(1, K+1):
        for n in range(mx, -1, -1):
            if dp[n] != k-1: continue
            nx1, nx2 = n-1, find_prev(n)
            if nx1 >= 0: dp[nx1] = k
            if nx2 >= 0: dp[nx2] = k
        mx = mx-1
        # log("k %3d, (%d~%d): dp %s", k, mn,mx, dp)

    # dp[0]에 K번째 도달 가능 여부 정보가 저장되어 있음
    return 'minigimbob' if dp[0] > 0 else 'water'



def solve3_set(N:int, K:int)->str:
    '''
    Args:
        N: target goal
        K: allowed steps
    Returns:
        str
    개선:
        앞선 코드 수행의 로그를 보면 dp 배열이 상당히 sparse 하므로, 배열 대신 set 를 이용.
        set 의 크기가 너무 많이 커질 경우 메모리 문제가 발생할 수 있으니 확인 필요함.
    결과:
        worst case 인 N,K 가 1,000,000 인 경우, dp set 에 최대 736개의 요소가 저장됨.
        이 정도면 별 문제 안됨.
    수행 시간
        # 0.036 sec
    '''

    dp = set()
    dp.add(N)

    for k in range(1, K+1):
        dpx = set()
        for n in dp:
            nx1, nx2 = n-1, find_prev(n)
            if nx1 >= 0: dpx.add(nx1)
            if nx2 >= 0: dpx.add(nx2)
        dp = dpx
        log("k %3d, dp (%d) %s", k, len(dp), dp)
        if 0 in dp: break  # 0에 더 일찍 도달했으면 성공임. 0에는 계속 머무를 수 있기 때문.

    return 'minigimbob' if 0 in dp else 'water'




if __name__ == '__main__':
    # print(solve(*get_input()))
    # print(solve2(*get_input()))
    print(solve3_set(*get_input()))


'''
예제 입력 1
5 2
예제 출력 1
water
예제 입력 2
42 10
예제 출력 2
minigimbob

---
run=(python3 a28069.py)

echo '5 2' | $run
# water
echo '42 10' | $run
# minigimbob

echo '100 100' | time $run
# minigimbob
# $run  0.02s user 0.01s system 94% cpu 0.027 total

echo '1000 1000' | time $run 2> /dev/null
# $run 2> /dev/null  0.12s user 0.01s system 98% cpu 0.133 total

echo '10000 10000' | time $run
# $run  7.21s user 0.02s system 99% cpu 7.260 total    <- 최초 solve() 구현
# $run  3.36s user 0.01s system 99% cpu 3.369 total    <- solve()에서 dpx 사용하지 않도록 개선
# $run  3.15s user 0.02s system 99% cpu 3.182 total    <- solve2(), mn 값 사용하지 않음.


echo '1000000 1000000' | time $run
#!! timeout!!
# $run  0.02s user 0.01s system 86% cpu 0.036 total   <- solve3_set() 사용

'''
