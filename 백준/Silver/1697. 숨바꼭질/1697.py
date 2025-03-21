'''
1697번

숨바꼭질 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	282132	84485	53818	26.383%

문제

수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약,
수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

'''



import sys
def log(fmt, *args):
    print(fmt % args, file=sys.stderr)



from collections import deque

MAX_NK = 100_000

def solve(N, K):

    if N == K:
        return 0
    if K < N:
        return N-K

    que = deque()
        # element of que is tuple of (node, trace_history).
        # trace history is for debugging purpose only.
        # if memory exceed limit, try with removing it.
    visited = [ 0 ] * (MAX_NK+1)
        # 1 if we visited this node.
        # it is possible that this list contains step count also.
        # however, we are using trace history, so just bool (0 or 1) is enough.

    que.append( (N,[]) )
    visited[N] = 1
    iter_count = 0 # it is also debugging purpuse

    while que:
        v,hist = que.popleft()
        if v == K:
            log('reached K %d, %s', K, hist)
            return len(hist) # skip first start node

        # if visited[v]: # for safety. it should not happen.
        #     continue

        hist = hist + [ v ]
        # visited[v] = 1
        iter_count += 1
        log('(%d) v %d, hist: %s', iter_count, v, hist)

        # consider next
        for w in [ v-1, v+1, 2*v ]:
            if w < 0 or w > MAX_NK:
                continue
            if visited[w]:
                continue
            # que.append(w)
            visited[w] = 1
            que.append( (w, hist) )

    # cannot reach K
    return -1


# import tracemalloc
# tracemalloc.start()

N, K = map(int, input().split())
print(solve(N, K))

# print(tracemalloc.get_traced_memory(),
#     #   file=sys.stderr # current, peak
#     )
# tracemalloc.stop()


'''
예제 입력 1
5 17
예제 출력 1
4

echo '5 17' | python3 1697.py
4

echo '0 100000' | time python3 1697.py
...
reached K 100000, [0, 1, 2, 3, 6, 12, 24, 48, 49, 98, 196, 195, 390, 780, 781, 1562, 3124, 3125, 6250, 12500, 25000, 50000]
22
21.28s

# after improvement
22
0.17s

echo '100000 0' | time python3 1697.py


1 56783
[1, 2, 3, 6, 7, 14, 28, 56, 112, 111, 222, 444, 888, 887, 1774, 3548, 3549, 7098, 14196, 14197, 28394, 56788]
22


'''

