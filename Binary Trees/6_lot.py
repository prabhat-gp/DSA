import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 102. Binary Tree Level Order Traversal
def levelOrderTraversal(root):
    if root is None:
        return []
    
    res = []
    qu = queue.Queue()
    qu.put(root)

    while not qu.empty():
        curr = qu.get()
        res.append(curr.data)

        if curr.left:
            qu.put(curr.left)
        
        if curr.right:
            qu.put(curr.right)

    return res



# 107. Binary Tree Level Order Traversal (Reverse LOT)
def reverseLevelOrder(root):
    if root is None:
        return []
    
    qu = queue.Queue()
    qu.put(root)
    ans = []

    while not qu.empty():
        v = []
        size = qu.qsize()

        for i in range(size):
            curr = qu.get()
            v.append(curr.data)

            if curr.left:
                qu.put(curr.left)
            
            if curr.right:
                qu.put(curr.right)

        ans = v + ans
    
    return ans

        

# 637. Average of Levels in Binary Tree


# 958. Check Completeness of a Binary Tree
def isCompleteTree(root):
    if root is None:
        return True

    qu = queue.Queue()
    qu.put(root)
    gap = False

    while not qu.empty():
        curr = qu.get()
        if curr == None:
            gap = True
            continue

        qu.put(curr.left)
        qu.put(curr.right)

        if gap:
            return False
    
    return True
        


# 1161. Maximum Level Sum of Binary Tree
def maxLevelSum(root):
    if root is None:
        return 0

    qu = queue.Queue()
    qu.put(root)
    level = 1
    maxLevel = 1
    maxSum = root.data

    while not qu.empty():
        currSum = 0
        currLevel = qu.qsize()


        for i in range(currLevel):
            curr = qu.get()
            currSum += curr.data

            if curr.left:
                qu.put(curr.left)
            
            if curr.right:
                qu.put(curr.right)
          
        if currSum > maxSum:
            maxSum = currSum
            maxLevel = level

        level += 1
    
    return maxLevel


# 2583. kth Largest Sum in Binary Tree
def kthLargestLevelSum(root, k):
    if root is None:
        return -1

    qu = queue.Queue()
    qu.put(root)
    levelSum = []

    while not qu.empty():
        currSum = 0
        currLevel = qu.qsize()

        for i in range(currLevel):
            curr = qu.get()
            currSum += curr.data

            if curr.left:
                qu.put(curr.left)
            
            if curr.right:
                qu.put(curr.right)

        levelSum.append(currSum)

    levelSum.sort(reverse = True)

    if k <= len(levelSum):
        return levelSum[k - 1]
    
    return -1