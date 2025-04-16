
'''
문제
L과 R이 주어진다. 이때, L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 L과 R이 주어진다. L은 2,000,000,000보다 작거나 같은 자연수이고, R은 L보다 크거나 같고, 2,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을 작성하시오.
'''

# using greedy. but it will timeout!
def solve_greedy(L, R):
    min_cnt = 100
    for i in range(L,R+1):
        cnt = 0
        for s in str(i):
            if s == '8': cnt += 1
        min_cnt = min(cnt, min_cnt)
    return min_cnt

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

