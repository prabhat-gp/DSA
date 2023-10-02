# 2 Sum (1)

# Brute Force
def twoSum(arr, k):
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                return [i, j]
    return [-1]


# Optimal
def twoSum(arr, k):
    map = {}
    n = len(arr)
    for i in range(n):
        temp = k - arr[i]
        if temp in map:
            return {map[temp], i}
        map[arr[i]] = i
    return {}





# 2 Sum Sorted (167)
def twoSum(arr, k):
    n = len(arr)
    low = 0
    high = n - 1
    for i in range(n):
        target = arr[low] + arr[high]
        if target == k:
            return [low + 1, high + 1]
        elif target < k:
            low += 1
        elif target > k:
            high -= 1
    return []




# Max Sum of k-sum pairs (1679)

# Approach 1
def maxOperations(arr, k):
    arr.sort()
    n = len(arr)
    low = 0
    high = n - 1
    cnt = 0
    while low < high:
        target = arr[low] + arr[high]
        if target == k:
            cnt += 1
            low += 1
            high -= 1
        elif target < k:
            low += 1
        elif target > k:
            high -= 1
    return cnt
            
            
# Approach 2
def maxOperations(arr, k):
    map = {}
    cnt = 0
    n = len(arr)
    for i in range(n):
        temp = k - arr[i]
        if temp in map and map[temp] > 0:
            cnt += 1
            map[temp] -= 1
        else:
            map[arr[i]] = map.get(arr[i], 0) + 1
    return cnt



# 653. Two Sum IV - Input is a BST
def inOrder(root, res):
    if root is None:
        return

    inOrder(root.left, res)
    res.append(root.data)
    inOrder(root.right, res)

def findTarget(root, k):
    res = []
    inOrder(root, res)
    low = 0
    high = len(res) - 1

    while low < high:
        target = res[low] + res[high]
        if target == k:
            return True
        elif target < k:
            low += 1
        else:
            high -=1
    
    return False


# 170. Two Sum III - Data Structure Design
# 1214. Two Sum BSTs
# BST Downward Traversal
# Floor and Ceil in BST 

