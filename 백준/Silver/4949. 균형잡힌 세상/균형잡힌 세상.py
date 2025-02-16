input = __import__('sys').stdin.readline
while True:
    s = input().rstrip() #.strip()
    if s == '.':
        break

    stack = []
    for c in s:
        if c in '([':
            stack.append(c)
        elif c in ')]':
            if not stack:
                print('no')
                break
            if (c == ')' and stack[-1] == '(') or (c == ']' and stack[-1] == '['):
                stack.pop()
            else:
                print('no')
                break
    else:
        print('yes') if not stack else print('no')