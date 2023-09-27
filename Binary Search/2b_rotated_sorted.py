# 153. Find Minimum in Rotated Sorted Array or Find K Rotations
# Approach: Index of array rotated = Index of min element
# ans = mid is smaller than both of its neighbours
# low to mid =  unsorted; mid to high = sorted


# Approach 1
def findKRotation(arr, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        prev = (mid + n - 1) % n
        next = (mid + 1) % n 

        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        elif arr[mid] >= arr[high]:
            low = mid + 1
        elif arr[mid] <= arr[low]:
            high = mid - 1
        else:
            high -= 1
        
    return 0


# Approach 2 (Only arr[mid], not index)
def findMin(arr, n):
    low = 0
    high = n - 1
    res = float("inf")

    while low <= high:
        mid = low + (high - low) // 2
        res = min(res, arr[mid])

        if arr[mid] >= arr[high]:
            low = mid + 1
        else:
            high = mid - 1
    return res




# --------------------------------------------------



# 154. Find Minimum in Rotated Sorted Array II (Contains Duplicates) Works for I also
# Works for all cases (minimum, k, duplicates)
def findMin(arr, n):
    low = 0
    high = n - 1

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] == arr[high]:
            high -= 1
        elif arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    
    return arr[low]




# 710. Random Pick with Blacklist
# 1574. Shortest Subarray to be Removed to Make Array Sorted
