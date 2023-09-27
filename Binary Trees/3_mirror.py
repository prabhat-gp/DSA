# 226. Convert a BT to its mirror (Invert of BT)

# Approach 1
def mirror(root):
    if root is None:
        return
    
    mirror(root.left)
    mirror(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp

    return root


# Approach 2
def mirror(root):
    if root is None:
        return
    
    root.left, root.right = root.right, root.left

    mirror(root.left)
    mirror(root.right)
    return root




# 2415. Reverse Odd Levels (Values) of Binary Tree
def traverse(root1, root2, level):
    if root1 is None or root2 is None:
        return
    
    if level % 2 == 1:
        temp = root1.val
        root1.val = root2.val
        root2.val = temp
    
    traverse(root1.left, root2.right, level + 1)
    traverse(root1.right, root2.left, level + 1)

def reverseOddLevels(root):
    if root is None:
        return
    
    traverse(root.left, root.right, 1)
    return root





# 101. Symmetric Tree is BT which is a Mirror image of itself.
def solve(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    
    if root1.data != root2.data:
        return False
    
    x = solve(root1.left, root2.right)
    y = solve(root1.right, root2.left)
    return x and y
    # return (left.data == right.data) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

def isSymmetric(root):
    if root is None:
        return True
    
    return solve(root.left, root.right)




# 100. Same Tree
def isSameTree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None or root1.data != root2.data:
        return False
    
    left = isSameTree(root1.left, root2.left)
    right = isSameTree(root1.right, root2.right)

    return left and right



# 654. Maximum Binary Tree
# 998. Maximum Binary Tree II