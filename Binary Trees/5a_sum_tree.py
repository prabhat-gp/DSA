# Sum Tree
# Return true if, for every node X in the tree other than the leaves, its value is equal to the sum of its left subtree's value and its right subtree's value. 
# Else return false.
# An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0. 
# A leaf node is also considered a Sum Tree.

# 112. Path Sum 

def isSumTreeFast(root):
    if root is None:
        return (True, 0)
    
    # Don't check leaves
    if root.left is None and root.right is None:
        return (True, root.data) 
    
    left = isSumTreeFast(root.left)
    right = isSumTreeFast(root.right)

    ans = (False, 0)

    if left[0] and right[0] and root.data == left[1] + right[1]:
        # ans = (True, root.data + left[1] + right[1])
        ans = (True, 2 * root.data)
    
    
    return ans

def isSumTree(root):
    return isSumTreeFast(root)[0]
    
# (left[0], left[1]) = (isSumTree, sum of left subtree) = (bool, int) 
# (right[0], right[1]) = (isSumTree, sum of right subtree) = (bool, int) 

# T.C = O(N)
# S.C = O(height)

# 113. Path Sum II 
# 437. Path Sum III