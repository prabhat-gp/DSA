# 287. Find the Duplicate Number

# Brute Force
def findDuplicate(arr, n):
    for i in  range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return arr[i]

    return -1


# Using map
def findDuplicate(arr, n):
    map = {}

    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
        
        if arr[i] in map and map[arr[i]] > 1:
            return arr[i]
    
    return -1
        

# Sort
def findDuplicate(arr, n):
    arr.sort()
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            return arr[i]
    
    return  -1
 

# Binary Search       
def findDuplicate(arr, n):
    low = 1
    high = n - 1

    while low < high:
        mid = low + (high - low) // 2
        cnt = 0

        for i in range(n):
            if arr[i] <= mid:
                cnt += 1
        
        if cnt > mid:
            high = mid
        else:
            low = mid + 1
    
    return low


# Floyd Cycle Detection Algorithm
def findDuplicate(arr, n):
    slow = 0
    fast = 0

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    slow = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow




# --------------------------------------------------



# 540. Single Element in Sorted Array
def singleNonDuplicate(arr, n):
    low = 0
    high = n - 1

    while low < high:
        mid = low + (high - low) // 2
        if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 == 1 and arr[mid] == arr[mid - 1]):
            low = mid + 1
        else:
            high = mid

    return arr[low]
        



# --------------------------------------------------


