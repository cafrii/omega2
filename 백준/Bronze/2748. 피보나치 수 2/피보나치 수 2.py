def solve(n:int):
    # 문제 정의 상, a[i] 는 i번째 수열.
    #  a[0] 은 0번째 수열.
    #  구해야 하는 n번째 수열은 a[n]
    a = [0, 1] + ([0] * (n-1))
    for i in range(2,n+1):
        a[i] = a[i-2] + a[i-1]
    return a[n]

n = int(input().strip())
print(solve(n))
