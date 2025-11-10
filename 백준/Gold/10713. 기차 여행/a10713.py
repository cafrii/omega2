'''
10713번
기차 여행, 골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	2121	933	712	44.224%

문제
JOI나라에는 N개의 도시가 있고, 각 도시에 1,2,...,N까지의 번호를 갖고 있다.

그리고, 철도가 N-1개 있고, 각 철도에 1,2,...N-1의 번호를 갖고 있다.

철도 i (1 ≦ i ≦ N-1)는 도시 i과 도시 i+1을 양방향으로 연결시키는 철도를 의미한다.

JOI나라의 철도를 타는 방법에는, 티켓을 구입해 승차하는 방법과 IC카드로 승차하는 방법 두 가지가 존재한다.

- 철도 i에 티켓을 구입해 승차할 때는 Ai 원의 비용이 든다.
- 철도 i에 IC카드로 승차하는 경우에는 Bi 원의 비용이 든다.
  하지만 IC카드로 철도를 탈 때는 IC카드를 미리 구입해둬야만 한다.
  철도 i에서 쓸 수 있는 IC카드를 구입하는데는 Ci원의 비용이 든다.
  한번 구입한 IC카드는 몇번이라도 사용할 수 있다.

IC카드가 처리가 간편하기 때문에, IC카드로 승차하는 방법의 운임이 티켓을 구입하는 경우보다 싸다.
즉, i = 1,2,...N-1일 때 Ai > Bi이다.
IC카드는 철도마다 다르기 때문에, 철도 i에서 사용할 수 있는 카드는 다른 철도에서는 사용할 수 없다.

당신은 JOI나라를 여행하기로 마음먹었다.
도시 P1에서 출발해, P2,P3... ,PM 순서의 도시를 방문할 예정이다.
여행은 M-1일간 이루어진다.
j일째 (1 ≦ j ≦ M-1) 에 도시 Pj으로부터 Pj+1으로 이동한다.
이때, 여러 개의 철도를 타는 경우도 있고, 같은 도시를 여러 번 방문할 수도 있다.
JOI나라의 철도는 빨라서 어느 도시도 하루만에 도착할 수 있다

당신은 현재 어느 철도의 IC카드도 갖고있지 않다.
당신은 미리 몇개의 IC카드를 구입해, 이 여행에서 사용되는 비용,
즉 IC카드를 구입하는 비용 + 철도를 타는 비용을 최소화하고 싶다.

JOI나라의 도시 수, 여행의 기간, 그리고 JOI나라의 철도 각각의 운임과, IC카드의 가격이 주어졌을 때,
여행의 비용을 최소화하는 프로그램을 작성하시오.

입력
첫 번째 줄에서는 정수 N, M이 주어진다.
두 번째 줄에는 M개의 정수 P1,P2,...PM이 주어진다.
  j일째 (1 ≦ j ≦ M-1) 에 도시 Pj에서 Pj+1로 이동하는 것을 의미한다.
3번째 줄부터 N-1개의 줄에는 (1 ≦ i ≦ N-1) 3개의 정수 Ai, Bi, Ci가 주어진다.
  각각 철도 i의 티켓을 구입하는 가격, 철도 i를 카드를 사용했을 때 통과하는 가격, IC카드를 구매하는 가격을 의미한다.

출력
여행에 드는 최저 비용을 첫째 줄에 출력하시오.

----

3:53~

검증 완료


'''


import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    Ms = list(map(int, input().split())) # travel path
    assert len(Ms) == M
    P = [(0,0,0)] # prices
    for _ in range(N-1):
        a,b,c = map(int, input().split())
        P.append((a, b, c))
    return N,Ms,P

def solve(N:int, Ms:list[int], P:list[tuple[int,int,int]])->int:
    '''
    Args:
    Returns:

    각 철도 N-1 개를 총 몇번씩 이용하는지를 카운트.
    이것만 알고 있으면 티켓 비용과 IC카드 비용을 그냥 비교해서 더 적은 값으로 선택하면 됨.
    M-1 번의 이동 각각에 대해서 시작/끝 기록. P1->P2 가 2 5 라면 도시 2에 +1, 도시 5에서 -1.
    이 차분 합을 누적 합으로 변환하면 이용 정보 완성.

    '''
    M = len(Ms)

    # usage count (difference)
    uc = [0] * (N+1)
    # uc[k]는 철도 k(도시 k 와 도시 k+1 사이)의 이용 회수
    # uc[0]은 미사용. uc[N]은 철도 N은 존재하지 않지만 편의를 위해 공간 마련.
    # uc[1] 부터 uc[N-1] 만 사용.

    for j in range(1, M): # j: 1 ~ M-1
        # 도시 Ms[j-1] 에서 Ms[j] 로의 이동
        s,e = Ms[j-1],Ms[j]  # start, end
        s1,e1 = min(s,e),max(s,e)
        uc[s1] += 1; uc[e1] -= 1
        log("  (%d) %d->%d, uc %s", j, s, e, uc)
        # e 는 N이 될 수 있음. 철도 N은 없지만 편의를 위해 -1을 기록 허용
    log("uc diff: %s", uc[1:])

    # 누적합으로 변경. uc diff -> uc
    for j in range(1, N+1):
        uc[j] = uc[j-1] + uc[j]
    assert uc[N] == 0

    log("uc sum : %s", uc[1:])

    # 각 철도 별로 비용 비교
    total_cost = 0
    for j in range(1, N):
        if uc[j] == 0: continue
        a,b,c = P[j]
        c1 = a * uc[j]
        c2 = b * uc[j] + c
        total_cost += min(c1, c2)
        log("[%d]: (%d,%d,%d) uc %d, c %d, total %d", j, a, b, c, uc[j], min(c1,c2), total_cost)

    return total_cost


if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
4 4
1 3 2 4
120 90 100
110 50 80
250 70 130
예제 출력 1
550

----
pr=10713
run=(python3 a$pr.py)

echo '4 4\n1 3 2 4\n120 90 100\n110 50 80\n250 70 130' | $run
# 550

'''
