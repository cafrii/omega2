
'''
수행 속더가 더 빠른 다른 solution 인데, 원리는 잘 모르겠음.
수학적 지식 필요한 듯.

https://www.acmicpc.net/source/67437837

67437837	kangkunma	2737	연속 합	맞았습니다!!	31256	52	Python 3	216	  <- 이 사람 답변
94731847	cafrii  	2737	연속 합	맞았습니다!!	32412	84	Python 3	1047  <- 내 답변


'''

def sol(n):
    temp,ans=n,0
    while temp%2==0: temp//=2
    for i in range(1,int(temp**.5)+1): ans+=(temp%i==0)*2
    ans-=(i**2==temp)
    return ans-1

for i in range(int(input())):
    print(sol(int(input())))
