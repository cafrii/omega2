S = input()
r = [-1] * 26
for i,a in enumerate('abcdefghijklmnopqrstuvwxyz'):
    if a in S:
        r[i] = S.index(a)
print(' '.join(map(str, r)))
