# 268. Missing Number
# Approach 1
def missingNumber(arr, n):
    arr.sort()
    low = 0
    high = n 
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > mid:
            high = mid
        else:
            low = mid + 1
    
    return low


# Approach 2
def missingNumber(arr):
    n = len(arr)
    total_sum = (n * (n + 1)) // 2

    for i in range(n):
        total_sum -= arr[i]
    
    return total_sum

# Bit Manipulation
# def missingNumber(arr):



# --------------------------------------------------


# 41. First Missing Positive
# Cycle Sort Question

# Using map 
def firstMissingPositive(arr, n):
    map = {}
    for i in range(n):
        map[arr[i]] = map.get(arr[i], 0) + 1
    
    for i in range(1, n + 2):
        cnt = map.get(i, 0)
        if cnt == 0:
            return i
        else:
            map[i] -= 1
    
    return -1

 

# --------------------------------------------------


# 136. Single Number -> 137. Single Number II -> 260. Single Number III
