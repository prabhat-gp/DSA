# 34. Find First and Last Position of Element in Sorted Array
# First and Last Occurence of an Element (Array Sorted) -> Binary Search
# Approach 1
def searchRange(arr, n, k):
    low = -1
    high = -1
    for i in range(n):
        if arr[i] == k:
            low = i
            break
    
    for i in range(n - 1, 0, -1):
        if arr[i] == k:
            high = i
            break

    return [low, high]


# Approach 2
def binarySearch(arr, n, k):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

def searchRange(arr, n, k):
    index = binarySearch(arr, n, k)
    left = index
    right = index

    while left > 0 and arr[left - 1] == k:
        left -= 1
    while right < n - 1 and arr[right + 1] == k:
        right += 1
    
    return [left, right]


    
# --------------------------------------------------



# 2089. Find Target Indices After Sorting Array (Count Occurences)
# This Solution also solves above problem (34)
# Works if the array is sorted
def firstOcc(arr, n, key):
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            res = mid
            high = mid - 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    
    return res

def lastOcc(arr, n, key):
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            res = mid
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    
    return res 

def targetIndices(arr, n, key):
    first = firstOcc(arr, n, key)
    last = lastOcc(arr, n, key)

    if first == -1 and last == -1:
        return 0
    else:
        return last - first + 1



# Approach 2
# def targetIndices(arr, n, k):