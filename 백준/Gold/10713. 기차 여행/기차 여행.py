import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    Ms = list(map(int, input().split())) # travel path
    #assert len(Ms) == M
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
        # e 는 N이 될 수 있음. 철도 N은 없지만 편의를 위해 -1을 기록 허용

    # 누적합으로 변경. uc diff -> uc
    for j in range(1, N+1):
        uc[j] = uc[j-1] + uc[j]
    #assert uc[N] == 0

    # 각 철도 별로 비용 비교
    total_cost = 0
    for j in range(1, N):
        if uc[j] == 0: continue
        a,b,c = P[j]
        c1 = a * uc[j]
        c2 = b * uc[j] + c
        total_cost += min(c1, c2)
    return total_cost

if __name__ == '__main__':
    print(solve(*get_input()))
