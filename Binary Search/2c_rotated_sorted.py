# 33. Search in Rotated Sorted Array (Doesn't handle duplicates)
# Approach: Index of array rotated = Index of min element
# ans = mid is smaller than both of its neighbours
# low to mid =  unsorted; mid to high = sorted


def binarySearch(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1


def findKRotations(arr, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        prev = (mid - 1 + n) % n
        next = (mid + 1) % n

        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        if arr[low] <= arr[mid]:
            low = mid + 1
        elif arr[high] <= arr[mid]:
            high = mid - 1
        else:
            high -= 1
    
    return 0


def Search(arr, n, key):
    indx = findKRotations(arr,  n)
    temp1 = binarySearch(arr, 0, indx - 1, key)
    temp2 = binarySearch(arr, indx, n - 1, key)

    if temp1 == -1 and temp2 == -1:
        return -1
    elif temp1 == -1:
        return temp2
    else:
        return temp1


# --------------------------------------------------


# 81. Search in Rotated Sorted Array II (Contains duplicates)
# In case of duplicates, can't tell mid is in left part or right part

def search(arr, n, k):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        # If the middle element is equal to the target, return True
        if arr[mid] == k:
            return True
        
        # Handle duplicates by moving the pointers inward
        while low < mid and arr[low] == arr[mid]:
            low += 1
        while mid < high and arr[mid] == arr[high]:
            high -= 1

        # Check which half is sorted and perform binary search accordingly
        if arr[low] <= arr[mid]:
            # The left half is sorted
            if arr[low] <= k < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        else:
            # The right half is sorted
            if arr[mid] < k <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return False


# If k belongs to [low, mid) = left half is sorted
# If k belongs to (mid, high] = right half is sorted
