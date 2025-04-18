while True:
    A,B,C = map(int, input().split())
    if (A,B,C) == (0,0,0):
        break
    if A*A == B*B + C*C or \
        B*B == A*A + C*C or \
        C*C == A*A + B*B:
        print("right")
    else:
        print("wrong")
