'''
큰 수 구성하기

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	9035	2731	2149	30.775%

2025/3/2 제줄 했으나 틀림 판정.
반례는 확보.
아직 적절한 아이디어 찾지 못함.
모든 경우의 수를 다 뒤지는 것이 아닌, 뭔가 더 효율적인 방법이 있을 것 같은데...


문제

N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오.
K의 모든 원소는 1부터 9까지의 자연  수로만 구성된다.

예를 들어 N=657이고, K={1, 5, 7}일 때 답은 577이다.

입력
첫째 줄에 N, K의 원소의 개수가 공백을 기준으로 구분되어 자연수로 주어진다.
(10 ≤ N ≤ 100,000,000, 1 ≤ K의 원소의 개수 ≤ 3)
둘째 줄에 K의 원소들이 공백을 기준으로 구분되어 주어진다.
각 원소는 1부터 9까지의 자연수다.

단, 항상 K의 원소로만 구성된 N보다 작거나 같은 자연수를 만들 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 N보다 작거나 같은 자연수 중에서, K의 원소로만 구성된 가장 큰 수를 출력한다.
'''


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



'''
예제 입력 1
657 3
1 5 7

예제 출력 1
577

---------
112 3
1 2 3
112


3333 3
1 2 3
3333

100 3
1 2 3
33

300 3
7 2 3
277


73 2
7 4
47

15 2
9 9
9

100000000 1
1

11111111


'''