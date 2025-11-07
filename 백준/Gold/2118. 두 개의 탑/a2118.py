'''
2118번
두 개의 탑 성공, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	3810	1470	1087	42.050%

문제
1번부터 N번까지의 지점이 있다. 각각의 지점들은 차례로, 그리고 원형으로 연결되어 있다.
이 지점들 중 두 곳에 두 개의 탑을 세우려고 하는데, 두 탑의 거리가 최대가 되도록 만들려고 한다.

지점들이 원형으로 연결되어 있기 때문에, 두 지점 사이에는 시계방향과 반시계방향의 두 경로가 존재한다.
두 지점 사이의 거리를 잴 때에는, 이러한 값들 중에서 더 작은 값을 거리로 한다.

연결되어 있는 두 지점 사이의 거리가 주어졌을 때, 두 탑의 거리의 최댓값을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 지점의 개수 N(2 ≤ N ≤ 50,000)이 주어진다.
다음 N개의 줄에는 차례로 두 지점 사이의 거리가 양의 정수로 주어진다.
전체 거리의 총 합은 1,000,000,000을 넘지 않는다.

출력
첫째 줄에 답을 출력한다.

--------

5:30~5:37
일단 누적합 계산용 테이블은 미리 만들어 놓는다.
하나의 연속된 숫자 그룹을 선택하면 숫자 그룹의 합과 숫자 그룹 이외의 합 중 작은 값을 기록.

6:13~6:17
시작 숫자 S, 끝 숫자 E 두개를 고른다.
그러면 S-E 의 누적합, E-S 누적합 둘을 O(1)에 구할 수 있다.
전체 합에서 S-E 누적합을 빼면 E-S 누적합이 된다.
모든 S,E 조합에 대해 다 계산하려면 O(N^2)이다. 이건 사용 불가.

10:46~
투포인터 방식 적용. 포인터 이동 시점 판단을 좀 고민해야 함.
잘 생각해 보니, S를 증가해야 하는 시점, E를 증가해야 하는 시점이 명확하다.
내합, 외합이 동일한 경우가 좀 문제가 된다..

----
검증 완료.

'''



import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = [ int(input().rstrip()) for _ in range(N) ]
    return N,A

def solve(N:int, A:list[int])->int:
    '''
    Args:
    Returns:
    '''

    # 누적합 구해놓기
    asum = [0] * (N+1)
    # asum[k] 는 첫 k개 요소의 합. 즉, A[0] 부터 A[k-1] 까지의 합

    for k in range(N): # k: 0 ~ N-1
        asum[k+1] = asum[k] + A[k]

    # A[j] 부터 A[k]의 합은 asum[k+1] - asum[j] 이다.
    total_sum = asum[N]

    def bruteforce():
        # 범위의 시작, 끝 인덱스.
        # 안쪽 합 [s, e) 와 바깥쪽 합 [e, s) 를 비교해야 함.
        # 바깥 합은 총합에서 안쪽 합을 빼면 됨.
        max_dist = -1
        max_dist_pair = (0,0)
        for s in range(N):
            for e in range(s+1, N+1):
                if s==0 and e==N: continue
                # 내합 [s, e)
                isum = asum[e] - asum[s]
                # 외합 [e, s). 분할되어 있을텐데 그냥 전체에서 빼기로 계산
                osum = total_sum - isum
                dist = min(isum, osum)
                if dist > max_dist:
                    max_dist_pair = (s,e,isum,osum)
                max_dist = max(max_dist, dist)

        log("max dist %d, (%d,%d) i%d, o%d", max_dist, *max_dist_pair)
        return max_dist


    def twopointer():
        max_dist = -1
        s,e = 0,1
        while True:
            # if s==0 and e==N: continue

            # log("[%d] %d, [%d] %d", s, A[s], e, A[e] if e<N else -1)
            # 내합 [s, e)
            isum = asum[e] - asum[s]
            # 외합 [e, s). 양쪽으로 분할되어 있을텐데 그냥 전체에서 빼기로 계산
            osum = total_sum - isum

            dist = min(isum, osum)
            # if dist > max_dist:
            #     log("-> i%d, o%d, dist %d", isum, osum, dist)

            max_dist = max(max_dist, dist)

            if e >= N:
                break

            if isum < osum:
                e += 1
            elif isum > osum:
                s += 1
            # else: # isum == osum
            # 이 경우는 좀 복잡해진다.
            # 최대한 내합, 외합이 비슷하게 만들어야 하니 적은 쪽을 이동해야 한다.
            elif A[s] < A[e]:
                s += 1
            elif A[s] > A[e]:
                e += 1
            else: # 양쪽 둘 다 같으면 둘 다 이동.
                s,e = s+1,e+1

        return max_dist

    # a1 = bruteforce()
    # a2 = twopointer()
    # # log("result compare: a1 %d, a2 %d", a1, a2)
    # assert a1 == a2, f'mismatch! {a1} != {a2}, A: {A}'

    return twopointer()



def solve2(N:int, A:list[int])->int:
    '''
    https://www.acmicpc.net/source/92356727
    다른 사람 해법. 코드가 좀 더 간결해 보임. 미리 prefix sum 계산 안해도 됨.
    '''

    total = sum(A)
    l = 0
    r = 0
    clock = 0  # 시계방향 거리

    answer = 0
    while l <= r and r < N:
        aclock = total - clock  # 반시계방향 거리
        cur = min(clock, aclock)  # 현재 거리

        if clock < aclock:
            # 시계방향 거리가 반시계방향보다 작으면
            # r을 늘려줘 시계방향 거리를 늘려줌
            clock += A[r]
            r += 1
        else:
            # 시계방향 거리가 반시계방향보다 크면
            # l을 늘려줘 반시계방향 거리를 늘려줌
            clock -= A[l]
            l += 1

        # 정답은 현재 거리 중 최대값
        answer = max(answer, cur)
    return answer


if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
5
1
2
3
4
5
예제 출력 1
7

----
pr=2118
run=(python3 a$pr.py)

echo '5\n1\n2\n3\n4\n5' | $run
# 7

echo '2\n3\n4' | $run
# 3
echo '3\n7\n9\n1' | $run
# 8



'''

#-------------------------
import time,os
from random import seed,randint,shuffle

def gen_worstcase_input():
    seed(time.time())
    seed(43)
    N = int(os.getenv('_N', '30'))
    A = [ randint(1,99) for _ in range(N) ]
    return N,A

def test():
    N,A = gen_worstcase_input()
    print(N)
    print('\n'.join(map(str, A)))


'''
worst case simulation

_N=10 python3 -c "from a11909 import test; test()" | time $run

python3 -c "from a$pr import test; test()" | time $run

_N=50000 python3 -c "from a$pr import test; test()" | time $run
# 1254321
# for seed(43)

'''

