
A, B = input().split()
A = int(A[::-1]) # reverse 3-digit number and convert to integer
B = int(B[::-1])
print(A if A > B else B)
