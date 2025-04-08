
from heapq import heappop, heappush
import sys
def log(fmt, *args):
    print(fmt % args, file=sys.stderr)


MAX_NK = 100_000


def solve(N, K):
    if N == K:
        return 0
    if K < N:
        return N-K

    que = []
        # element of que is tuple of (cost, node, ...)
        # cost: number of seconds elapsed since start.

    # COST_MAX = K - N + 1
    COST_MAX = MAX_NK + 1
    min_cost = [ COST_MAX ] * (MAX_NK + 1)

    heappush(que, (0, N, -1) )
    iter_count = 0 # it is also debugging purpuse
    last_cost = -1

    while que:
        # log('Q: %s', que)

        cost, now, prev = heappop(que)

        # 버그: 이게
        if now == K:
            log('reached K %d, cost %d, prev %d', K, cost, prev)
            return cost

        # if visited[v]: # for safety. it should not happen.
        #     continue
        if min_cost[now] < cost:
            # log('skip. min_cost[%d] is %d', now, min_cost[now])
            continue

        if last_cost != cost:
            last_cost = cost
            log('--------------------------')

        iter_count += 1
        log('(%d) node %d, cost %d, prev %d', iter_count, now, cost, prev)

        # consider next
        # 1. jump case, only when we are ahead of K
        if True: # impl 1
            while 0 < now < K:
                next_node, next_cost = 2*now, cost
                if next_node < 0 or next_node > MAX_NK:
                    break
                if min_cost[next_node] <= next_cost:
                    break
                min_cost[next_node] = next_cost
                heappush(que, (next_cost, next_node, now))
                log('add x2 node %d, cost %d', next_node, next_cost)
                break
        else:
            # improve 3
            next_node, next_cost = now, cost
            while True:
                if K < next_node:
                    break
                next_node = next_node * 2
                if not (0 < next_node <= MAX_NK): # drop 0
                    break
                if min_cost[next_node] <= next_cost: # already visited
                    continue
                min_cost[next_node] = next_cost
                heappush(que, (next_cost, next_node, now))

        # 2. walk case
        choices = [ now-1, now+1 ] if now < K else [ now-1 ]
        for next_node in choices:
            next_cost = cost + 1
            if next_node < 0 or next_node > MAX_NK:
                continue
            if min_cost[next_node] <= next_cost:
                continue
            min_cost[next_node] = next_cost
            heappush(que, (next_cost, next_node, now))
            log('add next node %d, cost %d', next_node, next_cost)

    # cannot reach K
    return -1




def bfs(start,end):
    from collections import deque
    if start==end:
        print(0)
        return
    que = deque()
    que.append((0,start))
    visited = set()
    visited.add(start)
    while que:
        step,position = que.popleft()
        #print(que)
        a,b,c = position-1,position+1,position*2
        if c <= 100000 and c not in visited:
            if c == end:
                return step
            que.appendleft((step,c))
            visited.add(c)

        if a >0 and a not in visited:
            if a == end:
                return step+1
            que.append((step+1,a))
            visited.add(a)
        if b <= 100000 and b not in visited:
            if b == end:
                return step+1
            que.append((step+1,b))
            visited.add(b)


'''
5 17


1차 구현:
-> iter 25

2차 개선: now 가 K를 넘어서면 now+1 은 고려 안하기
-> iter 24

echo '0 100000' | time python3 13549.py
echo '0 10000' | time python3 13549.py
echo '0 1000' | time python3 13549.py
iter 54609, 3824, 373

3차 개선: x2 경우를 미리 다 집어 넣어두기.
echo '0 100000' | time python3 13549.py
echo '0 10000' | time python3 13549.py
echo '0 1000' | time python3 13549.py
iter 65035, 3824, 373
-> 결과가 더 나빠짐??


'''

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(solve(N, K))


'''
5 17
-> 2

3 22
-> 1

1 10000
-> 3

1 100000
-> 5

0 5
-> 2

echo '64298 76127' | time python3 13549.py 2> /dev/null
-> 11829

echo '0 100000' | time python3 13549.py 2> /dev/null
-> 6

'''

def test():
    import time
    from random import seed,randint
    seed(time.time())
    for cnt in range(1,100000):
        N,K = randint(0,100000),randint(0,100000)
        a1 = solve(N, K)
        # a2 = solve2(N, K)
        a2 = bfs(N, K)
        if a1 != a2:
            print(f'N:{N}, K:{K}, solve1 {a1}, solve2 {a2}')
            sys.exit(1)
        if cnt % 100 == 0:
            print(f'cnt: {cnt}')

'''
solve1 과 solve2 비교

(python3 <<EOF
# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
mod = __import__('13549')
getattr(mod, 'test')()
EOF
) 2> /dev/null

'''



