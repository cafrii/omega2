'''
7579.py 의 정리 하기 전 버전.

- 로그 포함
- 선택된 항목 목록 정보 수집 기능 포함.
- early exit 버전은 시도하다가 실패.
  - solve_fast() 로 기록은 남겨둠.

'''

import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

MAX_N = 100
MAX_ci = 100

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

    sparse-list 또는 dict 형태의 데이터 구조가 필요하다.

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
    # cost 별 누적 최대 memory
    c2m:dict = {0:0}
    c2a:dict = {0:[]}

    for i in range(N):

        # 이번에 처리할 항목(item)의 cost 와 memory
        ci,mi = costs[i],mems[i]
        log('(%d) ---- ci %d, mi %d', i, ci, mi)

        # 기존까지의 모든 costs 조합에 대해서, mem 값을 업데이트 한다.
        # cost, mem 에 각각 ci, mi 가 더해지는 경우를 반영한다.
        # 새로운 cost 케이스 이면 그냥 저장하고,
        # 기존 cost 케이스가 있다면 기존 mem 보다 더 큰 경우에만 업데이트 한다.

        # 중간에 dict 가 변경되므로, enumeration 시에 주의 필요.
        # dict 업데이트에 의해 for loop 가 영향을 받으면 안된다.
        #
        # for c in list(c2m.keys()):
        for c in sorted(c2m.keys(), reverse=True):
            m = c2m[c]
            if m >= M: # 추가 관리 불필요. ci 가 음수가 아닌 이상..
                continue
            log('  (%d,%d)+ci/mi = (%d,%d)', c, m, c+ci, m+mi)
            # (c+ci, m+mi) 를 새롭게 c2m, c2a 에 추가/갱신 한다.
            if (c+ci) in c2m.keys():
                if c2m[c+ci] < m+mi:
                    c2m[c+ci] = m+mi
                    c2a[c+ci] = c2a[c] + [(ci,mi)]

                # c2m[c+ci] = max(c2m[c+ci], m+mi)
                # # 갱신이 되는 경우에는 (c,m) 의 list 에다 이번의 새 항목 (ci,mi) 를 더한 새 리스트를 만들어 등록한다.
                # c2a[c+ci] = c2a[c+ci] if c2m[c+ci]>=m+mi else (c2a[c]+[(ci,mi)])
            else:
                c2m[c+ci] = m+mi  # 신규 요소 추가
                c2a[c+ci] = c2a[c] + [(ci,mi)]
            log('      [%d] m %d, %s', c+ci, c2m[c+ci], c2a[c+ci])
            # 간단한 표현
            # c2m[c+ci] = max(c2m.get(c+ci, 0), m+mi)

        log('(%d)   %s', i, ' '.join([ f'{k}:{v}' for k,v in sorted(c2m.items()) ]))

    # M 이상의 최소 cost 검색
    # log('dict size %d, M %d', len(c2m), M)

    cms = list(zip(costs,mems))
    log('\nM %d\n%s', M, ' '.join([ f'({c}, {m})' for c,m in cms ]))

    for c,m in sorted(c2m.items()):
        if m >= M:
            log('===> (%d:%d) min_cost %d\n   %s', c, m, c, c2a[c])
            return c
    return 99999 # no solution

'''
[(82, 240), (77, 2560), (81, 434), (6, 577), (53, 500)]
c = 82+77+81+6+53 = 299
m = 240+2560+434+577+500 = 4311

'''



'''
    early exit 는 불가능한 것으로 판명됨.
    조기 종료 조건이 되었더라고 하더라도,
    cmr 비율이 더 높은 후순위 항목이 거의 조건 충족된 항목과 합해져서 더 나은(적은) cost를 만들 가능성이 있다.

'''
def solve_fast(N:int, M:int, mems:list, costs:list) -> int:
    # 단위 cost 당 memory 비율 순서대로 정렬. 큰 것 부터.
    # cost 는 0을 수 있으므로, c/m 비율을 ascending 으로 정렬하자.
    # cmlist = sorted(zip(costs,mems), key=lambda r: r[1]/r[0], reverse=True)
    cmlist = sorted(zip(costs,mems), key=lambda r: r[0]/r[1])

    # cost 별 누적 최대 memory
    c2m:dict = {0:0}
    prev_cmr = -1

    MAX_COST_SUM = 99999 # MAX_N * MAX_ci + 1
    min_cost = MAX_COST_SUM

    for i in range(N):
        # 이번에 처리할 항목(item)의 cost 와 memory
        ci,mi = cmlist[i] # costs[i],mems[i]
        cmr = ci/mi
        log('(%d) cost %d, mem %d, cmr %f', i, ci, mi, cmr)

        if min_cost < MAX_COST_SUM and cmr != prev_cmr:
            log('early exit')
            break

        for c in list(c2m.keys()):
            m = c2m[c]
            if m > M: continue

            c2m[c+ci] = max(c2m.get(c+ci, 0), m+mi)
            if m+mi >= M:
                min_cost = min(min_cost, c+ci)

        log('   %s', ' '.join([ f'{k}:{v}' for k,v in sorted(c2m.items()) ]))
        prev_cmr = cmr
        log('   cmr %f, min_cost %d', cmr, min_cost)

    return min_cost


cms = list(zip(costs,mems))
log('%s', cms)

print(solve(N, M, mems, costs))
# print(solve_fast(N, M, mems, costs))


'''
echo '5 60\n30 10 20 35 40\n3 0 3 5 4' | python3 7579.py
-> 6

echo '5 60\n30 10 20 35 60\n3 0 3 5 2' | python3 7579.py
-> 2

4 60
10 5 100 50
1  4 4   2
-> 3

echo '4 60\n10 5 100 50\n1  4 4   2' | python3 7579.py
-> 3

100 100
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
-> 0


5 100
20 20 20 20 20
0 0 0 0 0
-> 0

7 120
20 91 92 93 94 95 100
1 2 2 2 2 2 2
-> 3

24 1
1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576 2097152 4194304 8388608
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
-> 1

19 20169
240 2560 434 6 31 577 500 2715 2916 952 2490 258 1983 1576 3460 933 1660 2804 2584
82 77 81 0 36 6 53 78 49 82 82 33 66 8 60 0 98 91 93
-> 299

echo '19 20169\n240 2560 434 6 31 577 500 2715 2916 952 2490 258 1983 1576 3460 933 1660 2804 2584\n82 77 81 0 36 6 53 78 49 82 82 33 66 8 60 0 98 91 93' | python3 7579.py
-> 484

5 60
30 10 20 35 40
0 1 0 0 0
-> 0

7 120
20 91 92 93 94 95 100
1 2 2 2 2 2 2
-> 3



(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 20
mlist = [ randint(1,100_000) for k in range(N) ]
M = randint(1,sum(mlist))
print(N, M)
print(' '.join([ str(m) for m in mlist ]))
print(' '.join([ str(randint(0,100)) for k in range(N) ]))
EOF
) | time python3 7579.py 2> /dev/null

0.02s user 0.01s system 60% cpu 0.041 total


'''


