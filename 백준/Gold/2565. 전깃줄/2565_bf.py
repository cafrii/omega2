'''

다른 알고리즘으로 다시 시도.

----

dp[k]를 구할 때 dp[k-1], dp[k-2] 등의 정보를 활용하는 방식일텐데
k를 추가되는 전선의 index로 간주하는 방식으로는 아무리 생각해도 풀리지 않음.
dp[k-1]이 최소 제거 횟수와 같은 최종 결과만 저장할 경우 활용도가 떨어짐.
그 최소 제거 횟수를 만들어내는 전선 조합도 같이 저장해야만 활용할 수 있음.
하지만 동일한 결과를 내는 조합의 숫자가 너무 많아짐.
결국, 모든 경우를 다 계산하는 brute force와 다를 바 없게 됨.

----
결과:
구현은 완료. 하지만 N 값이 클 때 숫자의 배치에 따라 엄청나게 긴 시간이 소요되기도 함.
수행 시간은 랜덤. 하지만 대체로는 거의 종료 못 할 정도.
N 50 정도는 빨리 수행되며, 70~80 정도 가면 대략 십 수초 정도 까지도 걸리기도 함.

결과 자체는 정확함.

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)


MAX_N = 500

def get_input():
    input = sys.stdin.readline
    M = int(input().rstrip()) # M: 1 ~ 100
    # A = [0]*(MAX_N+1)
    L = [] # link array
    for _ in range(M):
        a,b = map(int, input().split())
        # A[a] = b
        L.append((a, b))
    return L,


def solve(L:list[tuple[int,int]])->int:
    '''
    '''
    N = 0
    A = [0] * (MAX_N+1)
    for a1,a2 in L:
        A[a1] = a2
        N = max(N, a1)
    # A[i] 는 i 위치에 연결된 전선의 반대쪽 위치
    # N 값은 a1 의 최대 값이며, a2 는 신경쓰지 않는다.

    log("%d\\n%s", len(L), '\\n'.join( f'{a} {b}' for a,b in L ) )


    B = [ [] for _ in range(N+1) ]
    # B[k] 는 교차되지 않는 k개의 전선 세트의 목록

    def crossing(j:int, k:int)->bool:
        j,k = min(j,k),max(j,k)
        j2,k2 = A[j],A[k]
        return k2 < j2

    def crossing2(j:int, ks:list[int])->bool:
        for k in ks:
            if crossing(j, k): return True
        return False

    max_sz = -1
    B[0].append([])

    for i in range(len(L)):
        # i 는 index. 0 부터 시작.
        a1,a2 = L[i]

        # log("(%d) a1 %d", i, a1)

        for j in range(i, -1, -1):
            # j 는 전선 개수. [0, i]

            # pruning:
            # (현재 포함) 앞으로 남은 단계: N-i
            # 향후 모든 단계에 klst 세트에 전선이 하나씩 추가된다고 하더라도
            # 현재까지의 가장 큰 세트의 크기를 넘어서지 못한다면 가망 없음.

            if j + (len(L)-i) < max_sz:
                continue

            for klst in B[j]:
                if crossing2(a1, klst): continue
                B[j+1].append(klst + [a1])
                max_sz = max(max_sz, j+1)

        # # logging
        # log("    B[%d] sz %d", max_sz, len(B[max_sz]))
        # for j in range(i+1, 0, -1):
        #     # for klst in B[j]: log("    %s", ' '.join(str() ))
        #     if not B[j]: continue
        #     log("-  %s", ' '.join(map(str, B[j])))

    # 가장 적게 전선을 제거한 경우가 정답. 즉, 가장 큰 전선 세트를 찾으면 됨.
    return len(L) - max_sz


if __name__ == '__main__':
    print(solve(*get_input()))



'''
예제 입력 1
run=(python3 2565_bf.py)

echo '8\n1 8\n3 9\n2 2\n4 1\n6 4\n10 10\n9 7\n7 6' | $run

예제 출력 1
3


echo '4\n5 7\n6 8\n7 5\n8 6' | $run
# 2 ?


echo '6\n1 1\n2 2\n3 5\n4 3\n5 4\n6 6' | $run
# 1


echo '50\n56 65\n54 25\n75 79\n81 9\n95 44\n70 24\n36 19\n3 88\n50 58\n12 37\n88 16\n8 46\n44 38\n53 55\n32 6\n47 60\n96 42\n17 27\n66 20\n59 89\n7 43\n69 51\n57 75\n91 63\n14 10\n74 80\n92 50\n73 87\n77 90\n1 7\n19 53\n72 64\n64 48\n86 97\n45 76\n68 91\n34 94\n99 52\n16 4\n63 11\n2 66\n25 56\n35 57\n80 39\n84 29\n49 13\n97 41\n93 30\n58 62\n40 22' | $run
# 38

echo '80\n91 57\n35 46\n12 66\n10 82\n61 84\n20 19\n3 59\n83 87\n86 53\n69 33\n66 42\n54 18\n72 55\n15 52\n32 64\n77 91\n29 90\n81 80\n74 11\n27 9\n19 10\n92 98\n37 48\n100 47\n6 44\n63 75\n41 65\n44 97\n58 78\n26 30\n25 36\n85 24\n11 29\n76 43\n79 49\n46 71\n99 41\n59 28\n56 3\n22 76\n34 17\n23 22\n80 68\n45 2\n28 72\n94 93\n73 60\n62 12\n4 7\n38 83\n13 62\n7 56\n48 63\n90 81\n39 1\n96 74\n24 69\n68 86\n75 25\n1 27\n82 95\n98 6\n64 51\n42 70\n47 34\n18 21\n21 38\n8 4\n36 5\n53 77\n87 31\n97 32\n33 14\n14 50\n31 96\n51 15\n57 8\n9 73\n70 20\n50 79' | $run
# 63



(python3 <<EOF
import time
from random import seed,randint,shuffle
seed(time.time())
N,M = 80,100
print(N)
R,S = list(range(1,M+1)),list(range(1,M+1))
shuffle(R); shuffle(S)
R,S = R[:N],S[:N]
print('\n'.join(f'{a} {b}' for a,b in zip(R,S)))
EOF
) | time $run



'''

