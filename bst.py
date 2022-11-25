from collections import deque
class node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value

def insertAfter(root,value):
    if not root:
        return node(value)
    elif value>root.value:
        root.right = insertAfter(root.right,value)
    elif value<root.value:
        root.left = insertAfter(root.left,value)
    return root

def search(root, target):
    if not root:
        return False
    elif target > root.value:
        return search(root.right, target)
    elif target < root.value:
        return search(root.left, target)
    else:
        return True

def minvaluenode(root):
    while(root and root.left):
        root = root.left
    return root

def remove(root,value):
    if not root:
        return None
    if value>root.value:
        root.right = remove(root.right,value)
    elif value<root.value:
        root.left = remove(root.left,value)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            findmin = minvaluenode(root.right)
            root.value = findmin.value
            root.right = remove(root,findmin.value)
    return root

#-------DFS-------

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.value)

#-------BFS-------

def bfs(root):
    queue = deque()
    if root:
        queue.append(root)
    level = 0
    while(len(queue)>0):
        # print(level) we can print the level if we need
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level+=1
if __name__=='__main__':
    root = node(10)
    # key = 2
    insertAfter(root,2)
    insertAfter(root,1)
    insertAfter(root, 3)
    insertAfter(root, 11)
    insertAfter(root, 12)
    insertAfter(root, 14)
    # print(search(root,4))
    # inorder(root)
    bfs(root)