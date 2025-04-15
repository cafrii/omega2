A,B = input().split()
sum1 = int(A.replace('6', '5'))+int(B.replace('6', '5'))
sum2 = int(A.replace('5', '6'))+int(B.replace('5', '6'))
print(sum1, sum2)
