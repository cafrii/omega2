'''

10:18~12:03

'''

import sys
input = sys.stdin.readline

def solve(S):
    def parse(s:str, op:str)->list:
        toks = []
        for t in s.split(op):
            toks.append(op) if toks else None
            toks.append(t)
        return toks

    toks1 = parse(S, '+') # 1차
    toks = []
    for t in toks1:
        if t == '+':
            toks.append(t)
        else:
            toks.extend(parse(t, '-'))

    # 숫자로 변환
    expr = list(map(lambda t: int(t) if t not in '+-' else t, toks))


    # 결국 +, - 연산자를 적용하는 순서에 따라 결과가 달라진다.
    # 연산자의 인덱스는 1, 3, 5, .. 의 홀수.

    def calc_expr(expr:list)->tuple[int,int]:
        # return (min, max)
        if len(expr) == 1:
            return expr[0],expr[0]
        assert len(expr)%2 == 1 # 홀수 길이

        min_vals,max_vals = [],[]
        for k in range(1, len(expr), 2): # 연산자의 인덱스
            opr1 = expr[:k]
            opr2 = expr[k+1:]
            min1,max1 = calc_expr(opr1)
            min2,max2 = calc_expr(opr2)
            if expr[k] == '+':
                min_vals.append(min1 + min2)
                max_vals.append(max1 + max2)
            else:
                min_vals.append(min1 - max2)
                max_vals.append(max1 - min2)

        return min(min_vals),max(max_vals)


    # 아래 계산 코드는 틀린 답을 리턴한다!!
    def calc_expr2(expr:list)->tuple[int,int]:
        if len(expr) == 1:
            return expr[0],expr[0]
        assert len(expr)%2 == 1 # 홀수 길이
        mn,mx = calc_expr2(expr[2:])
        if expr[1] == '+':
            return expr[0]+mn, expr[0]+mx
        else:
            return expr[0]-mx, expr[0]-mn

    mn1 = calc_expr(expr)[0]
    mn2 = calc_expr2(expr)[0]
    print(f"{expr}: {mn1} {mn2}")
    assert mn1 == mn2
    return mn1



S = input().strip()
print(solve(S))


'''
예제 입력 1
55-50+40
예제 출력 1
-35

예제 입력 2
10+20+30+40
예제 출력 2
100

예제 입력 3
00009-00009
예제 출력 3
0


1+2+3+4+5+6+7+8
-> 36

1+2+3+4+5+6+7+8+9+10
-> 55
0.03s

1+2+3+4+5+6+7+8+9+1+2+3+4
->
0.14s


1+2+3+4+5+6+7+8+9+1+2+3+4+5+6+7
2.68s
timeout!!



(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
# 25개의 operand, 24개의 operator
a = [ str(randint(0,9)) ]
for i in range(24):
    a.append( '+-'[randint(0,1)] )
    a.append( str(randint(0,9)) )
print(''.join(a))
EOF
) | time python3 1541.py




'''
