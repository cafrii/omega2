
def solve(L, R):
    def conv(N):
        # ex: 1234 -> [ 4, 3, 2, 1, ]
        # ex: 0 -> []
        res = []
        while N:
            res.append(N % 10)
            N = N // 10
        return res

    a1,a2 = conv(L),conv(R)

    # 리스트의 크기를 큰 쪽으로 통일시켜 확장. 늘어나는 자리는 0으로 채움.
    len0 = max(len(a1), len(a2))
    a1 = a1 + [0 for _ in range(len0-len(a1))]
    a2 = a2 + [0 for _ in range(len0-len(a2))]

    # reverse the list
    a1 = a1[::-1]
    a2 = a2[::-1]
    # print(a1, a2)
    # ex: 123 45678 -> [0,0,1,2,3], [4,5,6,7,8]

    # 앞 자리부터 비교.
    num_8 = 0
    for i in range(len0):
        if a1[i] != a2[i]:
            # 둘 다 8 일 수는 없으니, 8이 아닌 수를 선택할 수 있음.
            # 그 이후 부터는 8이 아닌 수를 선택하면 됨.
            break
        if a1[i] == 8:
            num_8 += 1
    return num_8

L, R = map(int, input().split())
print(solve(L, R))