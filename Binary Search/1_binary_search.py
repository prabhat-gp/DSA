# 704. Binary Search
def binarySearch(arr, n, key):
    low = 0
    high  = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# "sorted" keyword -> Binary Search -> reduce T.C
# Binary Search is used to reduce search space. In case of linear search, as the length of array increases it's not feasible.
# low <= high if only 1 element is present in array


# --------------------------------------------------


# 35. Search Insert Position
def binarySearch(arr, n, key):
    low = 0
    high  = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    return low

# This example explains that low and high cross each other while searching. 
# When crossed, while condition no longer holds true and hence that low is the answer


# --------------------------------------------------


# 278. First Bad Version
def firstBadVersion(n):
    low = 0
    high = n - 1
    res = n

    while low <= high:
        mid = low + (high - low) // 2
        if isBadVersion(mid) == True:
            high = mid - 1
            res = min(res, mid)
        else:
            low = mid + 1
    
    return res



# 2529. Maximum Count of Positive Integer and Negative Integer
