
from typing import List, Tuple

def solve(K:int, items:List[Tuple[int,int]]):
    '''
        항목이 하나 추가될 때 마다, 모든 가능한 W 에 대해서 이력을 기록 관리해야 함.
            item[i] 가 추가 고려 할 때
            item[0:i] 까지의 부분 솔루션에다
            새로 추가된 item[i] 를 고려하여 상태를 갱신한다.
        try
            2차원 테이블을 관리
                V2[w][item]
            앞에서는 W[], V[] 두 개를 관리했으나
            이제 V2 배열의 첫번째 dimension 에 W 정보가 포함되므로
            하나의 2차원 배열이면 충분.
        try2
            두 축을 바꾼다. w의 수가 적지 않으니..
                Vx[item][w]
            그리고 계산 편의를 위해 items+1 크기로 함. 즉 Vx[0]은 zeros
    '''
    N = len(items)
    Vx = [ [0] * (K+1) ] # no-item

    # Vx[0][:] 은 비워두고 Vx[1] 부터 채워나감.
    for i in range(1, N+1):
        # i번째 item 고려
        Wi,Vi = items[i-1]
        # print('** item %d: w %d, v %d' % (i, Wi, Vi))

        # 이번 item을 추가하지 않은 경우를 먼저 전제하고 시작.
        Vx.append( Vx[i-1].copy() )

        # Wi 를 추가할 수 있는 경우만 업데이트.
        '''        i-1   i
            V[0]    A
            ..        \
            V[w]        A+Wi
        '''
        for w in range(K+1-Wi):
            # w == 0 인 경우는 항상 고려 가능.
            # 그 외의 경우에서 이전 단계의 V 가 0 이라는 건, 부합하는 조건이 없다는 얘기.
            # 그런데.. value 가 0 인 item 도 있긴 한데.. 고려할 필요가 있을까?
            if w > 0 and Vx[i-1][w] == 0:
                continue

            # 직전의 w 값 에다 현재 Wi 를 더하는 경우임.
            if Vx[i-1][w] + Vi > Vx[i][w+Wi]:
                Vx[i][w+Wi] = Vx[i-1][w] + Vi
                # print('    V[%d][%d] = %d' % (i, w+Wi, Vx[i][w+Wi]))
        # show
        # print(Vx[i])

    return max(Vx[N])



N,K = map(int, input().split())  # 1~100
WV = []
for _ in range(N):
    WV.append(tuple(map(int, input().split())))

print(solve(K, WV))