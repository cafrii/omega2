
'''
괄호 추가하기 3
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1.5 초 (추가 시간 없음)	512 MB	1721	748	597	47.306%
문제
길이가 N인 수식이 있다. 수식은 0보다 크거나 같고, 9보다 작거나 같은 정수와 연산자(+, -, ×)로 이루어져 있다. 곱하기의 연산자 우선순위가 더하기와 빼기보다 높기 때문에, 곱하기를 먼저 계산 해야 한다. 수식을 계산할 때는 왼쪽에서부터 순서대로 계산해야 한다. 예를 들어, 3+8×7-9×2의 결과는 41이다.

수식에 괄호를 추가하면, 괄호 안에 들어있는 식은 먼저 계산해야 한다. 예를 들어, 3+8×7-9×2에 괄호를 (3+8)×7-(9×2)와 같이 추가했으면, 식의 결과는 59가 된다. 중첩된 괄호도 사용할 수 있고, 괄호 안에 여러 개의 연산자가 들어 있어도 된다. 즉, 3+((8×7)-9)×2, 3+((8×7)-(9×2)), (3+8)×(7-9×2) 모두 올바른 식이고, 결과는 97, 41, -121이다.

수식이 주어졌을 때, 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값을 구하는 프로그램을 작성하시오. 추가하는 괄호 개수의 제한은 없으며, 추가하지 않아도 된다.

입력
첫째 줄에 수식의 길이 N(1 ≤ N ≤ 19)가 주어진다. 둘째 줄에는 수식이 주어진다. 수식에 포함된 정수는 모두 0보다 크거나 같고, 9보다 작거나 같다. 문자열은 정수로 시작하고, 연산자와 정수가 번갈아가면서 나온다. 연산자는 +, -, * 중 하나이다. 여기서 *는 곱하기 연산을 나타내는 × 연산이다. 항상 올바른 수식만 주어지기 때문에, N은 홀수이다.

출력
첫째 줄에 괄호를 적절히 추가해서 얻을 수 있는 결과의 최댓값을 출력한다. 정답은 231보다 작고, -231보다 크다.
'''


# def calc1(s) -> int:
#     if s[1] == '+':
#         return int(s[0]) + int(s[2])
#     elif s[1] == '-':
#         return int(s[0]) - int(s[2])
#     elif s[1] == '*':
#         return int(s[0]) * int(s[2])
#     else:
#         return 0

def calc2(a) -> int:
    # a[0] and a[2] are number, a[1] is operator
    if a[1] == '+':
        return a[0] + a[2]
    elif a[1] == '-':
        return a[0] - a[2]
    elif a[1] == '*':
        return a[0] * a[2]
    else:
        return 0


def get_max(expr:list)->int:
    # expr is list of number and operator character
    #   ex: [3, '+', 8, '*', 7, '-', 9, '*', 2]
    # the length of expr is always odd

    if len(expr) == 1: # it should be number
        return expr[0]

    num_op = len(expr) // 2
    if num_op == 1: # length of expr is 3
        return calc2(expr)

    results = []
    for i in range(num_op):
        # create new expression, removing i-th operator
        expr2 = expr[:i*2] + [calc2(expr[i*2:i*2+3])] + expr[i*2+3:]
        res = get_max(expr2)
        results.append(res)

    # print(f'({num_op})  expr: {expr}, results {results}, max: {max(results)}')
    return max(results)


def solve_recursive(E:str):
    # convert string to list of number and operator character
    expr = [int(E[0])]
    for i in range(1, len(E), 2):
        expr.append(E[i])
        expr.append(int(E[i+1]))
    # print(f'expr is {expr}')

    res = get_max(expr)
    # print(res)
    return res


N = int(input())
E = input()
# print(f'N: {N}, E: {E}')

print(solve_recursive(E))


'''
예제 입력 1
9
3+8*7-9*2
예제 출력 1
136

예제 입력 2
5
8*3+5
예제 출력 2
64

예제 입력 3
7
8*3+5+2
예제 출력 3
80

예제 입력 4
19
1*2+3*4*5-6*7*8*9*0
예제 출력 4
100

예제 입력 5
19
1*2+3*4*5-6*7*8*9*9
예제 출력 5
426384

예제 입력 6
19
1-9-1-9-1-9-1-9-1-9
예제 출력 6
32


19
1-9-1-9+1-9-1+9-1-9

'''