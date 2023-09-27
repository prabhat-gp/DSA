# Search a row wise and column wise sorted matrix
# 74. Search in 2D Matrix
# 240. Search in 2D Matrix II
def search(matrix, n, m, key):
    # n rows
    # m cols
    n = len(matrix)
    m = len(matrix[0])

    i = 0
    j = m - 1

    while i >= 0 and i < n and j >= 0 and j < m:
        if matrix[i][j] == key:
            return 1
        elif matrix[i][j] > key:
            j -= 1
        else:
            i += 1
    
    return 0

# Move j from left to right and i from top to bottom


# --------------------------------------------------



# 1539. Kth Missing Positive Number
# Linear Approach
def findKthPositive(arr, n, k):
    cnt_miss = 0
    num = 1

    while cnt_miss < k:
        if num not in arr:
            cnt_miss += 1
        if cnt_miss == k:
            return num
        num += 1
    
    return -1


# Binary Search Approach
def findKthPositive(arr, n, k):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            low  = mid + 1
        else:
            high = mid - 1
    
    return low + k





# 378. Kth Smallest Element in a Sorted Matrix
# 215. Kth Largest Element in an Array -> Many Questions