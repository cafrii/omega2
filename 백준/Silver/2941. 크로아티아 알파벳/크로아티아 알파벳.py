s = input().strip()
ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
while s:
    if s[:3] in ca:
        s = s[3:]
    elif s[:2] in ca:
        s = s[2:]
    else:
        s = s[1:]
    count += 1
print(count)