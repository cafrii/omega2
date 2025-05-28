import sys
input = sys.stdin.readline

def eval2(s:str)->int:
    # s: + 로만 구성된 수식
    oprs = [] # operands
    for t in s.split('+'):
        oprs.append(int(t))
    return sum(oprs)

A = input().strip().split('-')
value = eval2(A[0])
for i in range(1,len(A)):
    value -= eval2(A[i])

print(value)
