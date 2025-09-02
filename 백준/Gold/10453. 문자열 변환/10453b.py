'''
좀 더 빠른 다른 구현인데... 원리를 잘 모르겠음.

https://www.acmicpc.net/source/97084966

98052700 cafrii     10453 맞았습니다!! 41508MB 996ms Python 3  1470B   <- my code
97084966 junu_jeon  10453 맞았습니다!! 38984MB 444ms Python 3   312B   <- this code


그닥 중요한 알고리즘은 아닌듯 하여 그냥 넘어감.

'''

import sys

input=sys.stdin.readline
T=int(input())

for _ in range(T):
    A,B=map(str,input().split())
    if len(A) != len(B):
        print(-1)
        continue
    a=[i for i,x in enumerate(A) if x=='b']
    b=[i for i,x in enumerate(B) if x=='b']
    diff=sum(abs(x-y) for x,y in zip(a,b))
    print(diff)


