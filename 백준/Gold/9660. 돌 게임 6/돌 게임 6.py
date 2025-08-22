N = int(input().rstrip())
w = 'CSCSSSS'[N % 7]
print('SK' if w=='S' else 'CY')
