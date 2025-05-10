
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

mems = list(map(int,input().split()))
costs = list(map(int,input().split()))


'''
    보통의 일반적인 접근 방법:
        dp[index][mem] 2d 배열을 준비하고
        index를 0부터 증가시켜가면서 dp[][] 에 최소 cost 값을 채워감.

    그런데 mem 의 값의 범위가 너무 크기 때문에, dense array로는 메모리 감당이 안된다.
    sparse-array 로 하더라도, mem 경우의 수가 너무 많아지면 결국 현실적이지 않다.

    반대로 cost의 경우는 좀 더 경우의 수가 적다.
    단일 cost는 범위가 0~100 이고, 100개의 요소이면 최대 10000 이므로,
    그냥 모든 가능한 cost 합의 dense array를 사용하는 것도 가능하다.
    좀 더 생각해 보면, cost의 범위가 아닌, cost 조합 case를 관리해야 한다.
    sparse-list 또는 dict 형태의 데이터 구조가 필요하다. 여기서는 dict로..

    cost 중복 경우 처리 예시:
        i0 i1 i2 i3 i4
        m: 30 10 20 35 40
        c: 3  0  3  5  4

        N=5 인 위의 예시에서, c=3에 도달하는 네가지 경우의 수가 존재.
            i0: m=30, c=3
            i2: m=20, c=3
            i0,i1: m=30+10=40, c=3
            i1,i2: m=20+10=30, c=3

        c=3 에 대한 m의 경우의 수는 20, 30, 40 총 세가지.
        이 중에서 최대값인 40을 유지 관리해야 한다.

    주어진 m에 대해서는 최소 비용 c 정보가 필요하고
    주어진 c에 대해서는 최대 메모리 m 정보가 필요하다.

'''

def solve(N:int, M:int, mems:list, costs:list) -> int:
    # cost-to-memory dict.
    # 누적 cost 별 memory 총합 매핑
    c2m:dict = {0:0}

    for i in range(N):
        # 이번에 처리할 항목(item)의 cost 와 memory
        ci,mi = costs[i],mems[i]

        # 기존까지의 모든 costs 조합에 대해서, (ci,mi)를 반영하여 업데이트 한다.
        # 새로운 cost 케이스 이면 그냥 저장하고,
        # 기존 cost 케이스가 있다면 기존 mem 보다 더 큰 경우에만 업데이트 한다.

        # 중간에 dict 가 변경되므로, enumeration 시에 주의 필요.
        # dict 업데이트에 의해 for loop 가 영향을 받으면 안된다.
        # 아래 for 의 reverse 순서가 중요함. 루프 전반부의 c 갱신에 의해 뒷부분의 c2m 값이 변경되어 버리면 안됨.
        # for c in list(c2m.keys()):
        for c in sorted(c2m.keys(), reverse=True):
            m = c2m[c]
            if m >= M: # 추가 관리 불필요.
                continue
            c2m[c+ci] = max(c2m.get(c+ci, 0), m+mi)

    # M 이상의 최소 cost 검색. 정렬된 cost 목록에서 앞에서부터 검사.
    for c,m in sorted(c2m.items()):
        if m >= M:
            return c

    return 99999 # no solution

print(solve(N, M, mems, costs))

