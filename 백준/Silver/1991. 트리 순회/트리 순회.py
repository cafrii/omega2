
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
