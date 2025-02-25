
def solve(E:list) -> str:
    # 괄호 부터 처리
    stack = []
    idx = 0; end = len(E)
    while idx < end:
        e = E[idx]
        if e == '(':
            stack.append(idx)
        elif e == ')':
            start = stack.pop()
            E[start:idx+1] = [ solve(E[start+1:idx]) ]
            # 길이 줄어듬 보정
            end -= ( idx - start ); idx = start
        idx += 1

    for idx, e in enumerate(E):
        if e == '(':
            stack.append(idx)
        elif e == ')':
            start = stack.pop()
            end = idx
            r = solve(E[start+1:end])
            E[start:end+1] = [r]

    assert len(stack) == 0, 'stack should be empty'
    # 모든 () 가 처리 되었음.

    # 곱셈, 나눗셈 처리
    idx = 0
    end = len(E)
    while idx < end:
        e = E[idx]
        if e == '*' or e == '/':
            E[idx-1:idx+2] = [ E[idx-1] + E[idx+1] + e ]
            # 3개 원소를 1개로 바꾸었으므로 idx 는 그대로이고 end 는 2 줄어듦.
            end -= 2; idx -= 2
        idx += 1

    # 덧셈, 뺄셈 처리. 앞에서부터 순서대로 하면 됨.
    stack = []
    result = ''
    for idx, e in enumerate(E):
        if e == '+' or e == '-':
            stack.append(e)
        elif stack and (stack[-1] == '+' or stack[-1] == '-'):
            result += e
            result += stack.pop()
        else:
            result += e

    return result


E = input().strip()
L = [ x for x in E ]
print(solve(L))

