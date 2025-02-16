import sys
input = sys.stdin.readline

N = int(input().rstrip())

stack = []

for i in range(N):
    s = list(map(int, input().rstrip().split()))

    if s[0] == 1:
        stack.append(s[1]) if len(s) == 2 else None
    elif s[0] == 2:
        print(stack.pop()) if stack else print(-1)
    elif s[0] == 3:
        print(len(stack))
    elif s[0] == 4:
        print(0) if stack else print(1)
    elif s[0] == 5:
        print(stack[-1]) if stack else print(-1)
