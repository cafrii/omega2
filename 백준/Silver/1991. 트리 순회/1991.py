'''
1991

트리 순회 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	70947	46324	35618	67.181%

문제
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.


10:14~10:38


'''

import sys
input = sys.stdin.readline


N = int(input().strip())

tree = {}
for _ in range(N):
    n,lf,rg = input().split()
    tree[n] = (lf,rg)

list_pre, list_in, list_post = [],[],[]

NONE = '.'

# use recursive call
def traverse_preorder(node = 'A'):
    if node == NONE: return
    lf,rg = tree.get(node, (NONE, NONE))
    list_pre.append(node)
    traverse_preorder(lf)
    traverse_preorder(rg)

def traverse_inorder(node = 'A'):
    if node == NONE: return
    lf,rg = tree.get(node, (NONE, NONE))
    traverse_inorder(lf)
    list_in.append(node)
    traverse_inorder(rg)

def traverse_postorder(node = 'A'):
    if node == NONE: return
    lf,rg = tree.get(node, (NONE, NONE))
    traverse_postorder(lf)
    traverse_postorder(rg)
    list_post.append(node)

traverse_preorder()
print(''.join(list_pre))

traverse_inorder()
print(''.join(list_in))

traverse_postorder()
print(''.join(list_post))


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



echo '1\nA . .' | python3 1991.py
A
A
A

echo '2\nA X .\nX . .' | python3 1991.py
AX
XA
XA

echo '3\nA X Y\nX . .\nY . .' | python3 1991.py
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

'''
