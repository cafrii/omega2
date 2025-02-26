
def solve(A:str) -> str:
    '''
    '''
    stack = []
    for a in A:
        if a == '(':
            stack.append(a)
        else: # ')'
            if stack:
                stack.pop()
            else:
                return 'NO'
    else:
        return ('YES' if not stack else 'NO')


T = int(input())
for _ in range(T):
    A = input()
    print(solve(A))
