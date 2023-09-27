# 162. Find Peak Element
# 852. Find Index in Mountain Array
# A peak element is an element that is strictly greater than its neighbors.

def peakElement(arr, n):
    s = arr[0]
    index = 0
    for i in range(1, n):
        if s < arr[i]:
            s = arr[i]
            index = i
    return index

# T.C = O(N)


def peakElement(arr, n):
    low = 0 
    high = n - 1

    while low < high: # important
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
        
    return low

# T.C = O(logN) 
# Aux Space = O(1)


# --------------------------------------------------


# 1901. Find Peak Element II