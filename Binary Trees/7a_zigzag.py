# 103. Zig Zag Traversal of Binary Tree (Spiral Traversal)
# Similar to Level Order Traversal
import queue
from collections import deque

def zigzagTraversal(root):
    if root is None:
        return []
    
    res = []
    qu = queue.Queue()
    qu.put(root)
    leftToRight = True

    while not qu.empty():
        size = qu.qsize()
        ans = [0] * size

        for i in range(size):
            curr = qu.get()

            index = i if leftToRight else size - i - 1
            ans[index] = curr.data

            if curr.left:
                qu.put(curr.left)

            if curr.right:
                qu.put(curr.right)

        
        leftToRight = not leftToRight

        for i in ans:
            res.append(i)

    return res

# T.C = O(N)
# S.C = O(N)


# Using Deque
def zigzagTraversal(root):
    if root is None:
        return []
    
    res = []
    qu = deque()
    qu.append(root)
    leftToRight = True

    while qu:
        size = len(qu)
        ans = [0] * size

        for i in range(size):
            curr = qu.popleft()

            index = i if leftToRight else size - i - 1
            ans[index] = curr.data

            if curr.left:
                qu.append(curr.left)

            if curr.right:
                qu.append(curr.right)

        leftToRight = not leftToRight

        for i in ans:
            res.append(i)

    return res

