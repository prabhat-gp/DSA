# Inorder Traversal

def inOrder(root):
    if root is None:
        return
    
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)



# PreOrder Traversal
def preOrder(root):
    if root is None:
        return
    
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)


# PostOrder Traversal
def postOrder(root):
    if root is None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)



