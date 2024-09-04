# 트리 순회
import sys
input = sys.stdin.readline

pre_t = []
in_t = []
post_t = []

def preorder(root):
    pre_t.append(root)
    
    if tree[root][0] != '.': # 왼쪽 자식이 있으면
        preorder(tree[root][0])
        if tree[root][1] != '.':
            preorder(tree[root][1])
    elif tree[root][1] != '.': # 왼쪽 자식이 없고 오른쪽 자식이 있으면
        preorder(tree[root][1])

def inorder(root):
    if tree[root][0] != '.': # 왼쪽 자식이 있으면
        inorder(tree[root][0])
        in_t.append(root)
        if tree[root][1] != '.':
            inorder(tree[root][1])
    elif tree[root][1] != '.': # 왼쪽 자식이 없고 오른쪽 자식이 있으면
        in_t.append(root)
        inorder(tree[root][1])
    else:
        in_t.append(root)

def postorder(root):
    if tree[root][0] != '.': # 왼쪽 자식이 있으면
        postorder(tree[root][0])
        if tree[root][1] != '.':
            postorder(tree[root][1])
            post_t.append(root)
        else:
            post_t.append(root)           
    elif tree[root][1] != '.': # 왼쪽 자식이 없고 오른쪽 자식이 있으면
        postorder(tree[root][1])
        post_t.append(root)
    else:
        post_t.append(root)
N = int(input())
tree = dict()

for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder('A')
print(''.join(pre_t))

inorder('A')
print(''.join(in_t))

postorder('A')
print(''.join(post_t))