


def solve2(data:list[int]):
    #
    # 포도주의 잔을 하나씩 늘려 가면서 계산.
    # n 번째 단계, 즉 n 개의 포도주 잔 조건에서의 최대 양.
    # 세 가지 서로 다른 경우가 있음.
    #
    # mv___x: 마지막 n 번째 잔을 take 하지 않은 경우.
    #            _ x |
    # mv_x_o: 마지막 n 번째 잔을 take 한 경우에서의 최대 양.
    #            x O |
    # mv_o_o: n, n-1 번째 잔을 모두 다 take 한 경우.
    #            O O |

    mv___x, mv_x_o, mv_o_o = [0], [0], [0]
    # 1-based. [0] 은 미사용.
    # 즉, 첫번째 잔 -> [1]

    for i in range(1, len(data) + 1): # 1 ~ len

        # i 번째 와인잔을 take 하는 경우.
        # _o 로 끝나는 경우임. x_o 이거나 o_o 에 해당.
        #
        x_o = mv___x[i-1] + data[i-1]
            # 직전 단계가 x 인 경우. ok. 현재 잔 용량 추가
        o_o = mv_x_o[i-1] + data[i-1]
            # 직전이 o 인 경우에 더할 수 있음.
            # x_o 와 o_o 중에서 x_o 만 가능. o_o 에다는 하나 더 추가할 수 없음.

        # i 번째 와인잔을 take 하지 않은 경우. _x 로 끝나는 경우임.
        # 직전 단계가 무슨 경우이건 상관 없이 선택 가능함.
        __x = max(mv___x[i-1], mv_x_o[i-1], mv_o_o[i-1])

        # [i] 번째 결과를 추가
        mv___x.append(__x)
        mv_x_o.append(x_o)
        mv_o_o.append(o_o)

    return max(mv___x[-1], mv_x_o[-1], mv_o_o[-1])


N = int(input().strip())
A = [ int(input().strip()) for _ in range(N) ]

print(solve2(A))
