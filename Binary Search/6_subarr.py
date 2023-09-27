# 209. Minimum Size Subarray Sum

# Sliding Window and Binary Search Approach
def window(arr, n, mid, k):
    i = 0
    j = 0
    currSum = 0
    minSize = float("-inf")

    while j < n:
        currSum += arr[j]
        if j - i + 1 < mid:
            j += 1
        elif j - i + 1 == mid:
            minSize = max(minSize, currSum)
            currSum -= arr[i]
            i += 1
            j += 1
    
    return minSize >= k

def minSubArrayLen(arr, n, k):
    low = 1
    high = n
    res = 0

    while low <= high:
        mid = low + (high - low) // 2
        if window(arr, n, mid, k):
            high = mid - 1
            res = mid
        else:
            low = mid + 1
    
    return res if res > 0 else 0



# Sliding Window Approach
def minSubArrayLen(arr, n, k):
    i = 0
    j = 0
    currSum = 0
    minSize = float("-inf")

    while j < n:
        currSum += arr[j]
        while currSum >= k:
            currSum -= arr[i]
            minSize = min(j - i + 1, minSize)
            i += 1
        
        j += 1

    if currSum == float("inf"):
        return 0
    
    return minSize


