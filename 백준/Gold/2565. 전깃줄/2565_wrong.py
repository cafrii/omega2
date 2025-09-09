'''

11:51~12:32

각 선 별로 겹치는 다른 선들의 마킹. 마킹 수가 제일 높은 것을 찾아서 제거.
이 작업을, 겹치는 것이 하나도 없을 때 까지 반복.
즉, greedy 알고리즘으로 시도.
하지만 틀림. 구현 오류는 아닌거 같고, 알고리즘 오류인듯.
현재 상황에서의 최적의 선택이, 나중에는 최적이 아니게 될 수도 있을 듯.

주어진 예제에서는 잘 동작하지만, 제출하면 실패 뜸.

-> 실제로 알고리즘에 문제가 있음이 쉽게 확인된다.

대안:
brute force 로 모든 가능한 선을 하나씩 제거해 보는 시도?

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
    # N 값은 a1 의 최대 값이며, a2 는 신경쓰지 않는다.

    # C = [ [0]*(N+1) for _ in range(N+1) ]
    # cross map
    # C[a][b]는 a에 연결된 전선이

    def crossing(j:int, k:int)->bool:
        j,k = min(j,k),max(j,k)
        j2,k2 = A[j],A[k]
        return k2 < j2

    cc = [0] * (N+1)  # cross count
    csum = 0
    for j in range(1,N):
        if A[j] == 0: continue
        for k in range(j+1,N+1):
            if A[k] == 0: continue
            if not crossing(j, k): continue
            cc[j] += 1
            cc[k] += 1
            csum += 2

    log("cc: %s", cc[1:])
    log("csum: %d", csum)

    # 가장 큰 cc 찾기
    num_removed = 0

    while csum > 0:
        ci = cc.index(max(cc))
        assert cc[ci] > 0, "wrong cc[ci]"

        log("cc %s, csum %d", cc[1:], csum)
        log("remove %d.. (cc %d)", ci, cc[ci])

        # remove line starting rom ci
        for k in range(1,N+1):
            if k == ci: continue
            if cc[k] == 0: continue
            if not crossing(ci, k): continue
            cc[k] -= 1
        csum -= cc[ci]*2
        cc[ci] = 0
        num_removed += 1

    return num_removed

if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
run=(python3 2565.py)

echo '8\n1 8\n3 9\n2 2\n4 1\n6 4\n10 10\n9 7\n7 6' | $run

예제 출력 1
3

echo '4\n5 7\n6 8\n7 5\n8 6' | $run
# 2

echo '6\n1 1\n2 2\n3 5\n4 3\n5 4\n6 6' | $run
# 1



'''

