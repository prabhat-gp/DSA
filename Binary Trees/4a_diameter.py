# 543. Diameter of Binary Tree (Width)
# Diameter = Longest Path between any 2 nodes

class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    
    left = height(root.left)
    right = height(root.right)

    ans = max(left, right) + 1
    return ans

def diameter(root):
    if root is None:
        return 0
    
    op1 = diameter(root.left)
    op2 = diameter(root.right)
    op3 = height(root.left) + height(root.right) + 1

    ans = max(op1, max(op2, op3))
    return ans

# T.C = O(N^2)
# S.C = O(N)

# Optimal Solution
def diameterFast(self, root):
    if root is None:
        return (0, 0)
        
    left = self.diameterFast(root.left)
    right = self.diameterFast(root.right)
        
    op1 = left[0]
    op2 = right[0]
    op3 = left[1] + right[1] + 1
        
    ans = (max(op1, max(op2, op3)), max(left[1], right[1]) + 1)
        
    return ans
    
def diameter(self, root):
    return self.diameterFast(root)[0]

# (left[0], left[1]) = (diameter, height) = (int, int)

# T.C = O(N)

