# Boundary Traversal

def traverseLeft(root, ans):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        return
    
    ans.append(root.data)
    if root.left:
        traverseLeft(root.left, ans)
    else:
        traverseLeft(root.right, ans)


def traverseLeaf(root, ans):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        ans.append(root.data)
        return
    
    traverseLeaf(root.left, ans)
    traverseLeaf(root.right, ans)


def traverseRight(root, ans):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        return
    
    if root.right:
        traverseRight(root.right, ans)
    else:
        traverseRight(root.left, ans)

    ans.append(root.data)

def boundaryTraversal(root):
    if root is None:
        return
    
    ans = []
    ans.append(root.data)
    
    # Traverse left part & store
    traverseLeft(root.left, ans)

    # Traverse Leaf Nodes
    # Traverse left subtree
    traverseLeaf(root.left, ans)

    # Traverse right subtree
    traverseLeaf(root.right, ans)

    # Traverse right part & store
    traverseRight(root.right, ans)

    return ans
    


# T.C = O(N) 
# S.C = O(height)
