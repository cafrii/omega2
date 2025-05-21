

import sys
from typing import Callable

input = sys.stdin.readline
def log(fmt, *args): print(fmt % args, file=sys.stderr)

N = int(input().strip())


# construct tree
tree = {}
for _ in range(N):
    n,lf,rg = input().split()
    if lf == '.': lf = None
    if rg == '.': rg = None
    tree[n] = (lf,rg)


def traverse(order:str, root:str, visit:Callable[[str],None]):
    if order == 'pre':
        stack = [ root ]
        while stack:
            node = stack.pop()
            visit(node)
            lf,rg = tree[node]
            # left 를 먼저 순회 하기 위해 rg 를 먼저 push
            if rg: stack.append(rg)
            if lf: stack.append(lf)

    if order == 'in':
        stack = [ (root, 0) ] # (node, perform_visit_action)
        while stack:
            node,act = stack.pop()
            if act:
                visit(node)
                continue
            lf,rg = tree[node]
            if rg: stack.append((rg, 0))
            stack.append((node, 1))
            if lf: stack.append((lf, 0))

    if order == 'post':
        stack = [ (root, 0) ]
        while stack:
            node,act = stack.pop()
            if act:
                visit(node)
                continue
            lf,rg = tree[node]
            stack.append((node, 1))
            if rg: stack.append((rg, 0))
            if lf: stack.append((lf, 0))



tries = [ ('pre',[]), ('in',[]), ('post',[]) ]
for order,res in tries:
    traverse(order, 'A', lambda node: res.append(node))
    print(''.join(res))


'''
예제 입력 1
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
예제 출력 1
ABDCEFG
DBAECFG
DBEGFCA

echo '7\nA B C\nB D .\nC E F\nE . .\nF . G\nD . .\nG . .' | python3 1991a.py

echo '1\nA . .' | python3 1991a.py
A
A
A

echo '2\nA X .\nX . .' | python3 1991a.py
->
AX
XA
XA

echo '3\nA X Y\nX . .\nY . .' | python3 1991a.py
->
AXY
XAY
XYA


26
A B .
B C .
C D .
D E .
E F .
F G .
G H .
H I .
I J .
J K .
K L .
L M .
M N .
N O .
O P .
P Q .
Q R .
R S .
S T .
T U .
U V .
V W .
W X .
X Y .
Y Z .
Z . .

ABCDEFGHIJKLMNOPQRSTUVWXYZ
ZYXWVUTSRQPONMLKJIHGFEDCBA
ZYXWVUTSRQPONMLKJIHGFEDCBA

echo '26\nA B .\nB C .\nC D .\nD E .\nE F .\nF G .\nG H .\nH I .\nI J .\nJ K .\nK L .\nL M .\nM N .\nN O .\nO P .\nP Q .\nQ R .\nR S .\nS T .\nT U .\nU V .\nV W .\nW X .\nX Y .\nY Z .\nZ . .' \
 | python3 1991a.py


'''
