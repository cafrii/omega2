while True:
    A = list(map(int, input().split()))
    if A == [0,0,0]:
        break
    # print(A)
    [a,b,c] = A
    if a==b and b==c:
        print('Equilateral')
    elif a+b <= c or b+c <= a or c+a <= b:
        print('Invalid')
    elif a==b or b==c or c==a:
        print('Isosceles')
    else:
        print('Scalene')
