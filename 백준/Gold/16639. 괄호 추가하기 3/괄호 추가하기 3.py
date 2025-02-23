

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

    return max(results)


def solve_recursive(E:str):
    # convert string to list of number and operator character
    expr = [int(E[0])]
    for i in range(1, len(E), 2):
        expr.append(E[i])
        expr.append(int(E[i+1]))

    res = get_max(expr)
    return res


N = int(input())
E = input()

print(solve_recursive(E))
