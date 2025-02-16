
A = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# convert to hash map
d = {}
for i in range(len(A)):
    for a in A[i]:
        d[a] = i + 3 # 'ABC' need 3 sec.

s = input()
result = 0
for c in s:
    result += d[c]
print(result)
