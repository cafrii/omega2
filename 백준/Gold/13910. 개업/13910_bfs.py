'''

solve using bfs

'''



import sys
from collections import deque

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    W = list(map(int, input().split())) # wok sizes
    assert len(W) == M, "wrong wok num"
    return N,W

def solve_bfs(N:int, W:list[int])->int:
    '''
    Args
        N: target num to compose. <= 10_000
        W: list of wok sizes. len <= 100, 1<=w<=N
    '''
    ws = set(W) # wok size set. 단독 사용

    # 웍 두개 조합 사용. 총합 만 중요.
    for j in range(1, len(W)):
        for i in range(j):
            w2 = W[i] + W[j]
            if w2 <= N: ws.add(w2)

    ws = sorted(list(ws), reverse=True)

    INF = max(10_001, N+1)
    dist = [ INF ] * (N+1)
    dist[0] = 0

    que = deque()
    # for w in ws:
    #     if w <= N:
    #         que.append(w)
    que.extend(ws)
    for w in ws: dist[w] = 1

    if dist[N] < INF: return 1

    while que:
        cur = que.popleft()
        d = dist[cur]
        # log("(%d, dist %d)", cur, d)

        for w in ws:
            nxt = cur + w
            if nxt == N: dist[N] = d+1; break
            if nxt > N: continue
            if dist[nxt] < INF: continue # already visited
            que.append(nxt)
            dist[nxt] = d + 1

        if dist[N] < INF: break

    # log("ws: %s", ws)

    return dist[N] if dist[N]<INF else -1


if __name__ == '__main__':
    print(solve_bfs(*get_input()))







'''

run=(python3 13910_bfs.py)

echo '10000 100\n4706 2270 4793 3079 6039 2580 7372 966 2433 2687 2016 1931 1667 4722 9127 4374 6696 6429 4100 1182 9256 2343 1144 989 4587 6490 5688 8625 4738 566 8898 284 3219 2382 3207 4712 2405 5771 2687 9861 7944 7592 6628 5593 8199 4594 890 1651 2258 7202 5870 8318 6017 6192 9782 35 7948 4414 8674 9345 876 1212 1441 8234 6430 4341 3247 8970 2139 4571 6303 7883 2301 32 5321 7870 4117 6634 6074 4017 8187 2072 9088 5610 1146 7221 7645 2561 1657 2710 277 3289 2720 8642 5266 7154 83 3555 9568 6387' | $run
# 10000

echo '10000 100\n3014 7583 4769 9896 7955 4124 5480 7724 3516 2940 8924 7532 1879 2386 4293 3281 7284 5783 4940 5951 9372 1245 8460 7705 9065 1005 7163 9209 8275 1905 572 5844 3253 9060 8205 3518 71 7989 2993 9306 6101 6593 1855 9073 6035 2576 9969 6869 3960 2478 145 2212 2270 511 2138 1154 1765 7110 3202 2288 4909 1153 3634 3396 9527 5502 6777 7729 9945 8238 376 1698 450 4245 808 4637 699 9051 8097 2573 4737 7507 2248 3881 9130 6420 1928 2455 4186 705 2252 7476 3187 7218 797 5160 1675 961 1322 1037' | $run
#


'''

