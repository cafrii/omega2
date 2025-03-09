'''
12865

평범한 배낭
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	160658	61727	38631	36.416%

문제
이 문제는 아주 평범한 배낭에 관한 문제이다.

한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에,
가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데,
해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

입력으로 주어지는 모든 수는 정수이다.

출력
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

'''


from typing import List, Tuple

def solve_wrong(K:int, items:List[Tuple[int,int]]):
    num_items = len(items)

    # 0 ~ i-1 개로 구성된 과거 단계의 솔루션
    # W[], V[] # 가능한 최대 무게 합, 최대 value

    # 최대 100 개 이므로 공간은 미리 할당.
    W = [0] * num_items
    V = [0] * num_items


    for i in range(num_items): # 0 ~ len_items-1
        Wi,Vi = items[i] # weight and value of i-th item

        # i 번째 item 검토 (Wi, Vi)
        print(f'({i}) w {Wi}, v {Vi}, K {K}')

        if i == 0:
            W[0],V[0] = Wi,Vi
            continue

        # case 1: 이번 item 을 추가하려는 경우
        Wsum,Vmax = 0,0
        for k in range(i-1, 0, -1):
            if W[k] + Wi > K:
                continue # 무게 초과!
            elif V[k] + Vi > Vmax:
                Wsum = W[k] + Wi
                Vmax = V[k] + Vi

        # case 2: 이번 것을 추가하지 않은 경우도 고려
        if Vmax < V[i-1]: # 이전 값이 더 좋음
            # 그냥 이번 단계 item 은 포함 안시킴.
            W[i],V[i] = W[i-1],V[i-1]
            print(f'     keep, w {W[i]}, v {V[i]}')
        else:
            W[i],V[i] = Wsum,Vmax
            print(f'     add, w {W[i]}, v {V[i]}')

    return V[num_items-1]



def solve(K:int, items:List[Tuple[int,int]]):
    '''
        개선
        항목이 하나 추가될 때 마다, 모든 가능한 W 에 대해서 이력을 기록 관리해야 함.
            item[i] 가 추가 고려 할 때
            item[0:i] 까지의 부분 솔루션에다
            새로 추가된 item[i] 를 고려하여 상태를 갱신한다.
        메모리
            모든 가능한 W는 0 ~ K 까지 총 K+1 개.
            따라서 테이블의 크기는 (K+1)*N*sizeof(int64) = 100K x 100 x 8 = 80MB
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


'''
예제 입력 1
4 7
6 13
4 8
3 6
5 12

예제 출력 1
14

( cat <<EOF
4 7
6 13
4 8
3 6
5 12
EOF
) | python3 a.py

시간초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,K = 100,100_000
print(N, K)
for _ in range(N):
    print(randint(1, K),randint(1, 1000))
EOF
) | time python3 a.py

python3 a.py  0.31s user 0.02s system 99% cpu 0.335 total

'''