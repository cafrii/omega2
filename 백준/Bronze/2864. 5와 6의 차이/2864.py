# 2864.py

A,B = input().split()
sum1 = int(A.replace('6', '5'))+int(B.replace('6', '5'))
sum2 = int(A.replace('5', '6'))+int(B.replace('5', '6'))
print(sum1, sum2)


'''
다른 구현들..
ss = input().split()
print(sum(map(lambda s: int(s.replace('6','5')), ss)),\
      sum(map(lambda s: int(s.replace('5','6')), ss)))


예제 입력 1
11 25
예제 출력 1
36 37

예제 입력 2
1430 4862
예제 출력 2
6282 6292

예제 입력 3
16796 58786
예제 출력 3
74580 85582

'''
