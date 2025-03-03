
def solve(N:int, A:list):
    answer = ''
    # 숫자로 답을 찾아가는 대신, 문자열로 하나씩 답을 찾아가는 방식이다.
    A = list(sorted(A, reverse=True))
    str_n = str(N)

    for i in range(len(str_n)):
        # N 의 각 자리에 있는 수를 하나씩 반복 순회.

        max_digit = -1
        # N 의 해당 자리에 있는 수를 초과하지 않는 A 에서 가장 큰수

        for digit in A:
            # if int(str_n[i]) >= digit:
            #     max_digit = digit
            #     break
            # 현재 자리 만 고려해서는 안된다!! 지금까지 결정된 숫자들까지 포함해서 비교해야 한다!
            if int(str_n[:i+1]) >= int(answer + str(digit)):
                max_digit = digit
                break

        if max_digit >= 0:
            answer += str(max_digit)
            continue

        # 발견 실패. A 의 모든 수가 N 의 현재 자리 수 보다 큼.
        # 백트래킹.
        for j in range(i - 1, -1, -1):
            for digit in A:
                if int(answer[j]) > digit:
                    answer = answer[:j] + str(digit)
                    answer += str(A[0]) * (len(str_n) - len(answer))
                    return int(answer)

        # 최악의 경우. 백트래킹으로도 적절한 수를 찾지 못했음.
        # 아예 N 보다 자릿수를 하나 더 작은 수로 만들어야 함. 여기서 결정 후 종료.
        # 자리수가 적기 때문에 최대 숫자로 채울 수 있음.
        return int(str(A[0]) * (len(str_n) - 1))

    return int(answer)


N, K = map(int, input().split())
A = list(map(int, input().split()))

print(solve(N, A))

