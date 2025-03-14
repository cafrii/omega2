
'''
후위 표기식

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	55210	21452	16408	38.371%


문제
수식은 일반적으로 3가지 표기법으로 표현할 수 있다. 연산자가 피연산자 가운데 위치하는 중위 표기법(일반적으로 우리가 쓰는 방법이다),
연산자가 피연산자 앞에 위치하는 전위 표기법(prefix notation), 연산자가 피연산자 뒤에 위치하는 후위 표기법(postfix notation)이 그것이다.
예를 들어 중위 표기법으로 표현된 a+b는 전위 표기법으로는 +ab이고, 후위 표기법으로는 ab+가 된다.

이 문제에서 우리가 다룰 표기법은 후위 표기법이다. 후위 표기법은 위에서 말한 법과 같이 연산자가 피연산자 뒤에 위치하는 방법이다.
이 방법의 장점은 다음과 같다. 우리가 흔히 쓰는 중위 표기식 같은 경우에는 덧셈과 곱셈의 우선순위에 차이가 있어 왼쪽부터 차례로 계산할 수 없지만
후위 표기식을 사용하면 순서를 적절히 조절하여 순서를 정해줄 수 있다.
또한 같은 방법으로 괄호 등도 필요 없게 된다.
예를 들어 a+b*c를 후위 표기식으로 바꾸면 abc*+가 된다.

중위 표기식을 후위 표기식으로 바꾸는 방법을 간단히 설명하면 이렇다.
우선 주어진 중위 표기식을 연산자의 우선순위에 따라 괄호로 묶어준다.
그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.

예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다.
그 다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 (a+bc*)가 된다.
마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.

다른 예를 들어 그림으로 표현하면 A+B*C-D/E를 완전하게 괄호로 묶고 연산자를 이동시킬 장소를 표시하면 다음과 같이 된다.

결과: ABC*+DE/-

이러한 사실을 알고 중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램을 작성하시오

입력
첫째 줄에 중위 표기식이 주어진다. 단 이 수식의 피연산자는 알파벳 대문자로 이루어지며 수식에서 한 번씩만 등장한다.
그리고 -A+B와 같이 -가 가장 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 주어지지 않는다.
표기식은 알파벳 대문자와 +, -, *, /, (, )로만 이루어져 있으며, 길이는 100을 넘지 않는다.

출력
첫째 줄에 후위 표기식으로 바뀐 식을 출력하시오

'''




def solve(E) -> str:
    '''
        A+B -> AB+
        A*B+C -> AB*C+
        A+B*C -> ABC*+
        (A+B)*C -> AB+C*
        (xxxxx)+(yyy) -> xxxxxyyy+
    '''
    if type(E) == str: # convert to list
        E = [ x for x in E ]

    # print(f"########### {E}")
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
    # print(f'---- () removed: {E}')
    # print(E)

    # 곱셈, 나눗셈 처리
    # print(f'---- multiply, divide ----')
    idx = 0
    end = len(E)
    while idx < end:
        e = E[idx]
        # print(f'idx: {idx}, e: {e}, end: {end}, E: {E}')
        if e == '*' or e == '/':
            E[idx-1:idx+2] = [ E[idx-1] + E[idx+1] + e ]
            # 3개 원소를 1개로 바꾸었으므로 idx 는 그대로이고 end 는 2 줄어듦.
            end -= 2; idx -= 2
        idx += 1
        # print(f"    ({idx}) '{e}': <{end}, {E}")

    # 모든 곱셈, 나눗셈 처리 되었음.
    # print(f'---- multiply, divide ended ----')
    # print(f"---- mul/div end: {E}")

    # print(f'---- plus, minus ----')
    # 덧셈, 뺄셈 처리. 앞에서부터 순서대로 하면 됨.
    stack = []
    result = ''
    for idx, e in enumerate(E):
        # print(f'idx: {idx}, e: {e}')
        if e == '+' or e == '-':
            stack.append(e)
            # print(f"    ({idx}) '{e}': stack: {stack}, result: {result}")
        elif stack and (stack[-1] == '+' or stack[-1] == '-'):
            result += e
            result += stack.pop()
            # print(f"    ({idx}) '{e}': stack: {stack}, result: {result}")
        else:
            result += e
            # print(f"    ({idx}) '{e}': stack: {stack}, result: {result}")

    # print(f'---- plus, minus ended ----')
    # print(f"---- plus/mius end: '{result}'")
    return result



# without recursion, more simple

def solve2(E:str):
    stack = []
    result = ''
    for e in E:
        if e.isalpha():
            result += e
        elif e == '(':
            stack.append(e)
        elif e == '*' or e == '/':
            while stack and stack[-1] == '*' or stack[-1] == '/':
                result += stack.pop()
            stack.append(e)
        elif e == '+' or e == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(e)
        else: # ')'
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        # print(f"{e}, {stack}, '{result}'")

    while stack:
        result += stack.pop()

    return result



E = input().strip()
# print(solve(E))
print(solve2(E))

'''
A+B-C
AB+C-

A+B*C
ABC*+

A+B*(C-D)-E
ABCD-*+E-


'''




'''
예제 입력 1
A*(B+C)
예제 출력 1
ABC+*

예제 입력 2
A+B
예제 출력 2
AB+
예제 입력 3
A+B*C
예제 출력 3
ABC*+
예제 입력 4
A+B*C-D/E
예제 출력 4
ABC*+DE/-
'''