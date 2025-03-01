T = int(input().strip())

for _ in range(T):

    S = input().strip()

    left = [] # string before cursor
    right = [] # string on and after cursor, reversed

    for c in S:
        if c == '<':
            if left:
                right.append(left.pop())
                # append to right list at the tail, not insert to head!
        elif c == '>':
            if right:
                left.append(right.pop())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)

    left.extend(reversed(right))
    print(''.join(left))
