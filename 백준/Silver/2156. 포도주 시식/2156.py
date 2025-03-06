'''
포도주 시식

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	158327	54483	39484	32.840%

문제
효주는 포도주 시식회에 갔다. 그 곳에 갔더니, 테이블 위에 다양한 포도주가 들어있는 포도주 잔이 일렬로 놓여 있었다.
효주는 포도주 시식을 하려고 하는데, 여기에는 다음과 같은 두 가지 규칙이 있다.

포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
효주는 될 수 있는 대로 많은 양의 포도주를 맛보기 위해서 어떤 포도주 잔을 선택해야 할지 고민하고 있다.
1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오.

예를 들어 6개의 포도주 잔이 있고, 각각의 잔에 순서대로 6, 10, 13, 9, 8, 1 만큼의 포도주가 들어 있을 때,
첫 번째, 두 번째, 네 번째, 다섯 번째 포도주 잔을 선택하면 총 포도주 양이 33으로 최대로 마실 수 있다.

입력
첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 ≤ n ≤ 10,000)
둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.

출력
첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.

'''


def solve(data:list[int]):
    #
    # 포도주의 잔을 하나씩 늘려 가면서 계산.
    # n 번째 단계, 즉 n 개의 포도주 잔 조건에서의 최대 양.
    # 세 가지 서로 다른 경우가 있음.
    #
    # mv___x: 마지막 n 번째 잔을 take 하지 않은 경우.
    #            ? x |
    # mv_x_o: 마지막 n 번째 잔을 take 한 경우에서의 최대 양.
    #            x O |
    # mv_o_o: n, n-1 번째 잔을 모두 다 take 한 경우.
    #            O O |

    mv___x, mv_x_o, mv_o_o = [0] * len(data), [0] * len(data), [0] * len(data)
    mv___x[0] = 0
    mv_x_o[0] = data[0]
    mv_o_o[0] = data[0]

    print(f"(0) {mv___x[0]}, {mv_x_o[0]}, {mv_o_o[0]}")

    # 모든 것은 0-based 로 명명함.

    for i in range(1, len(data)):
        print(f"---- {data[i]}")
        # i 번째 와인잔 (vol) 을 take 하는 경우.
        # _o 로 끝나는 경우임. x_o 이거나 o_o 에 해당.
        #
        mv_x_o[i] = mv___x[i-1] + data[i]
            #  직전 단계가 x 인 경우에 현재 잔 추가
        mv_o_o[i] = mv_x_o[i-1] + data[i]
            #  o_o 에다는 하나 더 추가할 수 없음. x_o 에만 추가 가능.

        # i 번째 와인잔을 take 하지 않은 경우. _x 로 끝나는 경우임.
        # 직전 단계가 무슨 경우이건 상관 없이 선택 가능함.
        mv___x[i] = max(mv___x[i-1], mv_x_o[i-1], mv_o_o[i-1])

        print(f"({i}) {mv___x[i]}, {mv_x_o[i]}, {mv_o_o[i]}")

    i = len(data) - 1  # last index
    return max(mv___x[i], mv_x_o[i], mv_o_o[i])


def solve2(data:list[int]):
    #
    # 포도주의 잔을 하나씩 늘려 가면서 계산.
    # n 번째 단계, 즉 n 개의 포도주 잔 조건에서의 최대 양.
    # 세 가지 서로 다른 경우가 있음.
    #
    # mv___x: 마지막 n 번째 잔을 take 하지 않은 경우.
    #            ? x |
    # mv_x_o: 마지막 n 번째 잔을 take 한 경우에서의 최대 양.
    #            x O |
    # mv_o_o: n, n-1 번째 잔을 모두 다 take 한 경우.
    #            O O |

    mv___x, mv_x_o, mv_o_o = [0], [0], [0]
    # 1-based. [0] 은 미사용.
    # 즉, 첫번째 잔 -> [1]

    for i in range(1, len(data) + 1): # 1 ~ len
        print(f"---- +{data[i-1]}")

        # i 번째 와인잔 (vol) 을 take 하는 경우.
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

        print(f"({i}) __x:{mv___x[-1]}, x_o:{mv_x_o[-1]}, o_o:{mv_o_o[-1]}")
        # [ print(a) for a in (mv___x, mv_x_o, mv_o_o) ]

    return max(mv___x[-1], mv_x_o[-1], mv_o_o[-1])


def solve3(data:list[int]):

    # i 번째 잔을 고려하기 위해 다음과 같은 조건의 경우의 수가 있음.
    #     i-2 i-1  i
    #              x   : take 하지 않음
    #          x   o   : 연속 1회 take
    #      x   o   o   : 연속 2회 take
    #
    #  mv[i-3] 까지 참조가 필요하므로 mv[3] 이 첫번째 와인 잔이 되도록 오프셋 고려.
    #
    len_data = len(data)
    data = [0, 0, 0] + data
    mv = [ 0 ] * (len_data + 3)

    for k in range(3, len_data + 3):
        # i 번째 와인잔 루프의 인덱스 k = i+3
        i = k - 3
        mv[k] = max(
                mv[k-1],
                mv[k-2] + data[k],
                mv[k-3] + data[k-1] + data[k],
            )
    return mv[-1]



N = int(input().strip())
A = [ int(input().strip()) for _ in range(N) ]

print(solve3(A))


'''
예제 입력 1
6
6
10
13
9
8
1

예제 출력 1
33
'''