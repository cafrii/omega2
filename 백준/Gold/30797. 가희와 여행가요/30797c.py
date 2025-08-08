'''
질문 게시판에 소개된 문제의 코드.
그다지 좋은 코드는 아닌데, 이 코드가 통과 되었다고 하니 이것을 좀 분석해 보았음.
역시나 시간 factor는 알고리즘에 큰 영향을 주지 않는다.

'''

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,Q=map(int,input().split())
parent=[0]*(n+1)
for i in range(n+1):
    parent[i]=i


def findParent(parent:list,x:int)->int:
    if(parent[x]!=x):
        parent[x]=findParent(parent,parent[x])
    return parent[x]

def unionParent(parent:list,a:int,b:int)->None:
    a=findParent(parent,a)
    b=findParent(parent,b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b

edges=[]

totalCost=0
completedTime=0
for _ in range(Q):
    fr,to,co,tm=map(int,input().split())
    edges.append((co,tm,fr,to))

edges.sort(key=lambda x:(x[0],x[1]))

for i in range(Q):
    fr=edges[i][2]
    to=edges[i][3]
    if(findParent(parent,fr)!=findParent(parent,to)):
        unionParent(parent,fr,to)
        totalCost+=edges[i][0]
        # completedTime=edges[i][1]
        completedTime=max(completedTime, edges[i][1]) # yhlee modified

# if(parent[1]!=parent[-1]):
#     print(-1)
#     exit(0)

selfReference=0
for i in range(1,n+1):
    if(i==parent[i]):
        selfReference+=1
if(selfReference>1):
    print(-1)
    exit(0)


print(completedTime,totalCost)



