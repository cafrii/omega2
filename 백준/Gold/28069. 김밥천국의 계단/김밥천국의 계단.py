import sys

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    return N,K

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

def solve_timeout(N:int, K:int)->str:
    '''
    using plain dp
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

    # dp[0]에 K번째 도달 가능 여부 정보가 저장되어 있음
    return 'minigimbob' if dp[0] > 0 else 'water'

def solve2_timeout(N:int, K:int)->str:
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

        하지만 N,K 가 100000 에서는 종료를 못함 (timeout!)
        더 개선이 필요.
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
    dp.add(N) # N 에서부터 시작, 역방향으로 내려감.

    for k in range(1, K+1):
        dpx = set()  # 다음 단계의 set
        for n in dp:
            nx1, nx2 = n-1, find_prev(n)
            if nx1 >= 0: dpx.add(nx1)
            if nx2 >= 0: dpx.add(nx2)
        dp = dpx
        if 0 in dp: break  # 0에 더 일찍 도달했으면 성공임. 0에는 계속 머무를 수 있기 때문.

    return 'minigimbob' if 0 in dp else 'water'

if __name__ == '__main__':
    print(solve3_set(*get_input()))
