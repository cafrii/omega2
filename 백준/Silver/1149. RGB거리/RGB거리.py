
def solve(n, exps):
    '''
    n: number of houses
    exps: list of expenses
        each expense is (R, G, B) tuple
        len(exps) should be n
    '''

    min_exp = [ exps[0] ]
    # min_exp[i]:Tuple[int,int,int]
    #   0 부터 i번째 집까지 칠했고 i번째 집이 각각 r, g, b 로 칠해졌을 때의 최소 비용

    # 1 부터 n-1 까지
    for i in range(1, n):
        # i번째 집을 r로 칠하려면 i-1번째 집이 g 또는 b 이어야 함.
        min_r = min(min_exp[i-1][1], min_exp[i-1][2]) + exps[i][0]
        # g
        min_g = min(min_exp[i-1][0], min_exp[i-1][2]) + exps[i][1]
        # b
        min_b = min(min_exp[i-1][0], min_exp[i-1][1]) + exps[i][2]

        # print(min_r, min_g, min_b)
        min_exp.append( (min_r, min_g, min_b) )

    return min(min_exp[-1])


N = int(input().strip())
E = []
for _ in range(N):
    E.append(tuple(map(int, input().split())))

print(solve(N, E))
