
import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = [0]*N
    for k in range(N):
        A[k] = int(input().rstrip())
    return A

def solve(A:list[int])->list[str]:
    '''
    '''
    result:list[str] = []
    k = 1
    stack = []
    for a in A:
        if a >= k:
            while k <= a:
                result.append('+')
                stack.append(k)
                k += 1
            result.append('-')
            stack.pop()
        else: # a < k
            if stack and stack[-1] == a:
                result.append('-')
                stack.pop()
            else:
                result = ['NO']
                break
    return result

if __name__ == '__main__':
    inp = get_input()
    for s in solve(inp):
        print(s)
