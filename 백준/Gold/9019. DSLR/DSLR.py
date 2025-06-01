import sys
from collections import deque

input = sys.stdin.readline

NUM_NODE = 10000
MAX_COST = NUM_NODE+1

def solve(S:int, E:int)->str:
    '''
    S 에서 E 까지 변환할 수 있는 연산 경로 검색
    bfs 사용. 그래프는 문제의 주어진 조건을 활용하여 각 노드 별로 4개의 간선이 있는 것으로 간주.
    '''

    stat = [ [MAX_COST,-1,''] for e in range(NUM_NODE) ]
    # node status 리스트 : 0 ~ 9999 숫자 값을 인덱스로 사용.
    #  element: [cost, prev, op]
    #    cost: S 부터 시작하여 이 노드에 이르기까지의 경로 길이
    #    prev: 위 cost 경로에서 이 노드의 직전 노드
    #    op: prev->here 까지의 이동 시 사용한 연산

    que = deque()

    que.append(S)
    stat[S][:] = [0,-1,'']

    ops = { # operations 사전
        'D': lambda a: (2*a) % NUM_NODE, # double
        'S': lambda a: (a-1) % NUM_NODE, # subtract
        'L': lambda a: (a%1000)*10+a//1000, # left shift
        'R': lambda a: (a//10)+(a%10)*1000, # right shift
    }

    def backtrace(node):
        ans = []
        # node_path = []
        while node >= 0:
            assert len(ans) <= NUM_NODE
            # node_path.append(node) # node
            ans.append(stat[node][2]) # operation
            node = stat[node][1] # next
        return ''.join(reversed(ans))

    while que:
        here = que.popleft()
        cost = stat[here][0]

        if here == E: # reached to the goal
            # 역추적하여 결과 생성
            return backtrace(E)

        # aply operation
        for name,fn in ops.items():
            nxt = fn(here)
            if cost+1 < stat[nxt][0]:
                stat[nxt][0] = cost+1
                stat[nxt][1] = here
                stat[nxt][2] = name
                que.append(nxt)
    return 'None' # 정답 없음.


T = int(input().strip())
for _ in range(T):
    A,B = map(int, input().split())
    print(solve(A,B))
