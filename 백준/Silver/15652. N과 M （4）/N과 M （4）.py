
N, M = map(int, input().split())
ans = [0] * M

def populate(index) -> bool:
    if index >= M:
        print(*ans)
        return

    for k in range(1, N+1):
        # check if k is allowed to be placed on [index]
        if index >= 1:
            if ans[index-1] > k:
                continue # not allowed
        ans[index] = k
        populate(index + 1)

populate(0)
