def sugar(N):
    # i: number of 5-kg bags
    for i in range(N//5, -1, -1):
        if (N - 5*i) % 3 == 0:
            return i + (N - 5*i) // 3
    return -1

N = int(input().strip())
print(sugar(N))
