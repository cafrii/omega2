'''
또 다른 구현
https://www.acmicpc.net/source/96317009


'''

import sys
I=sys.stdin.readline
for _ in range(int(I())):
    t={}              # 트리. child-parent 관계를 dict 로 표현
    for _ in range(int(I())-1):
        a,b=map(int,I().split())
        t[b]=a
    x,y=map(int,I().split())
    p,q=[x],[y]    # root 까지 거슬러 올라가는 경로 정보 생성.
    while True:
        if(p[-1] not in t): break
        p.append(t[p[-1]])
    while True:
        if(q[-1] not in t): break
        q.append(t[q[-1]])
    q=set(q)      # 그 중 하나의 경로 list를 set 로 만들고
    for e in p:   # 다른 경로의 중간 노드를 set 와 비교하며 탐색
        if(e in q): print(e); break
